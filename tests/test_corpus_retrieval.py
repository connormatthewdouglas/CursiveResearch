from __future__ import annotations

import importlib.util
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

MODULE_PATH = Path(__file__).resolve().parents[1] / "tools" / "corpus_retrieval.py"
spec = importlib.util.spec_from_file_location("corpus_retrieval", MODULE_PATH)
corpus_retrieval = importlib.util.module_from_spec(spec)
sys.modules["corpus_retrieval"] = corpus_retrieval
assert spec.loader is not None
spec.loader.exec_module(corpus_retrieval)


def write_sample_repo(root: Path) -> None:
    (root / "chapters").mkdir(parents=True)
    (root / "sources").mkdir(parents=True)
    (root / ".cursive-research-rag").mkdir(parents=True)
    (root / "README.md").write_text("# Sample Corpus\n\nIntro text.\n", encoding="utf-8")
    (root / "CHANGELOG.md").write_text(
        "# Changelog\n\nFounder-risk retrieval fallback changed here, but this is process metadata.\n",
        encoding="utf-8",
    )
    (root / "chapters" / "01-measurement.md").write_text(
        "# Measurement Trust\n\n"
        "The measurement daemon owns organism truth.\n\n"
        "## Natural-language shell boundary\n\n"
        "The shell may read measurement state but must not write organism truth.\n",
        encoding="utf-8",
    )
    (root / "sources" / "source-register.md").write_text(
        "# Source Register\n\nBBR fairness and retransmit risk remain review flags.\n",
        encoding="utf-8",
    )
    (root / "chapters" / "02-economics.md").write_text(
        "# Economics\n\n"
        "Founder cut is none; the founder is paid as a normal contributor.\n"
        "Sensor evidence, not governance theater, controls value.\n",
        encoding="utf-8",
    )
    (root / ".cursive-research-rag" / "ignored.md").write_text(
        "# Generated Cache\n\nThis should not be indexed.\n",
        encoding="utf-8",
    )


class CorpusRetrievalTests(unittest.TestCase):
    def test_index_search_show_and_status(self) -> None:
        with tempfile.TemporaryDirectory(prefix="corpus-retrieval-test-") as tmp:
            root = Path(tmp)
            write_sample_repo(root)
            index_path = root / ".cursive-research-rag" / "index.sqlite"

            summary = corpus_retrieval.build_index(root, index_path)
            self.assertEqual(summary["documents"], 5)
            self.assertGreaterEqual(summary["chunks"], 4)

            results = corpus_retrieval.search_index(index_path, "shell organism truth", limit=5, mode="all")
            self.assertTrue(results)
            self.assertEqual(results[0].path, "chapters/01-measurement.md")
            self.assertLessEqual(results[0].start_line, results[0].end_line)
            self.assertIn("shell", results[0].snippet.lower())

            chunk = corpus_retrieval.get_chunk(index_path, results[0].id)
            self.assertTrue(chunk["citation"].startswith("chapters/01-measurement.md:"))
            self.assertIn("must not write organism truth", chunk["text"])

            status = corpus_retrieval.corpus_status(root, index_path)
            self.assertTrue(status["up_to_date"])
            self.assertEqual(corpus_retrieval.changed_status(status)["new"], [])

            (root / "chapters" / "02-new.md").write_text("# New\n\nFresh research.\n", encoding="utf-8")
            status = corpus_retrieval.corpus_status(root, index_path)
            self.assertFalse(status["up_to_date"])
            self.assertEqual(status["new"], ["chapters/02-new.md"])

    def test_search_path_and_heading_filters(self) -> None:
        with tempfile.TemporaryDirectory(prefix="corpus-retrieval-test-") as tmp:
            root = Path(tmp)
            write_sample_repo(root)
            index_path = root / ".cursive-research-rag" / "index.sqlite"
            corpus_retrieval.build_index(root, index_path)

            source_results = corpus_retrieval.search_index(
                index_path,
                "BBR retransmit",
                limit=5,
                path_filters=("sources/",),
                heading_filters=("Source Register",),
            )
            self.assertTrue(source_results)
            self.assertTrue(all(result.path.startswith("sources/") for result in source_results))
            self.assertIn("Source Register", source_results[0].heading)

            chapter_results = corpus_retrieval.search_index(index_path, "BBR retransmit", limit=5, path_filters=("chapters/",))
            self.assertEqual(chapter_results, [])

    def test_query_expansion_falls_back_to_rare_anchor_term(self) -> None:
        with tempfile.TemporaryDirectory(prefix="corpus-retrieval-test-") as tmp:
            root = Path(tmp)
            write_sample_repo(root)
            index_path = root / ".cursive-research-rag" / "index.sqlite"
            corpus_retrieval.build_index(root, index_path)

            direct = corpus_retrieval.search_index(index_path, "founder dependency", limit=5, mode="all")
            self.assertEqual(direct, [])

            response = corpus_retrieval.search_index_with_fallback(index_path, "founder dependency", limit=5, mode="all")
            self.assertTrue(response.expanded)
            self.assertEqual(response.strategy, "relaxed-rare-term:founder")
            self.assertTrue(response.results)
            self.assertEqual(response.results[0].path, "chapters/02-economics.md")

    def test_cli_explains_expanded_search_fallback(self) -> None:
        with tempfile.TemporaryDirectory(prefix="corpus-retrieval-test-") as tmp:
            root = Path(tmp)
            write_sample_repo(root)
            index_path = root / ".cursive-research-rag" / "index.sqlite"
            subprocess.run(
                [sys.executable, str(MODULE_PATH), "index", "--repo-root", str(root), "--index", str(index_path), "--json"],
                check=True,
                text=True,
                capture_output=True,
            )

            explained = subprocess.run(
                [
                    sys.executable,
                    str(MODULE_PATH),
                    "search",
                    "founder dependency",
                    "--match",
                    "all",
                    "--repo-root",
                    str(root),
                    "--index",
                    str(index_path),
                    "--explain",
                    "--json",
                ],
                check=True,
                text=True,
                capture_output=True,
            )
            payload = json.loads(explained.stdout)
            self.assertEqual(payload["strategy"], "relaxed-rare-term:founder")
            self.assertTrue(payload["expanded"])
            self.assertEqual(payload["results"][0]["path"], "chapters/02-economics.md")

            unexpanded = subprocess.run(
                [
                    sys.executable,
                    str(MODULE_PATH),
                    "search",
                    "founder dependency",
                    "--match",
                    "all",
                    "--expand",
                    "never",
                    "--repo-root",
                    str(root),
                    "--index",
                    str(index_path),
                    "--json",
                ],
                check=True,
                text=True,
                capture_output=True,
            )
            self.assertEqual(json.loads(unexpanded.stdout), [])

    def test_cli_json_search_and_status_ergonomics(self) -> None:
        with tempfile.TemporaryDirectory(prefix="corpus-retrieval-test-") as tmp:
            root = Path(tmp)
            write_sample_repo(root)
            index_path = root / ".cursive-research-rag" / "index.sqlite"
            subprocess.run(
                [sys.executable, str(MODULE_PATH), "index", "--repo-root", str(root), "--index", str(index_path), "--json"],
                check=True,
                text=True,
                capture_output=True,
            )
            skipped = subprocess.run(
                [sys.executable, str(MODULE_PATH), "index", "--if-stale", "--repo-root", str(root), "--index", str(index_path), "--json"],
                check=True,
                text=True,
                capture_output=True,
            )
            self.assertTrue(json.loads(skipped.stdout)["skipped"])

            status = subprocess.run(
                [sys.executable, str(MODULE_PATH), "status", "--changed-only", "--repo-root", str(root), "--index", str(index_path), "--json"],
                check=True,
                text=True,
                capture_output=True,
            )
            self.assertEqual(json.loads(status.stdout), {"up_to_date": True, "new": [], "stale": [], "missing": []})

            proc = subprocess.run(
                [
                    sys.executable,
                    str(MODULE_PATH),
                    "search",
                    "BBR retransmit",
                    "--repo-root",
                    str(root),
                    "--index",
                    str(index_path),
                    "--path",
                    "sources/",
                    "--heading",
                    "Source Register",
                    "--json",
                ],
                check=True,
                text=True,
                capture_output=True,
            )
            results = json.loads(proc.stdout)
            self.assertTrue(results)
            self.assertTrue(results[0]["citation"].startswith("sources/source-register.md:"))

    def test_retrieval_audit_accepts_expected_source_areas(self) -> None:
        with tempfile.TemporaryDirectory(prefix="corpus-retrieval-test-") as tmp:
            root = Path(tmp)
            write_sample_repo(root)
            index_path = root / ".cursive-research-rag" / "index.sqlite"
            corpus_retrieval.build_index(root, index_path)

            report = corpus_retrieval.retrieval_audit(
                index_path,
                cases=(
                    {
                        "name": "sample source caveat",
                        "query": "BBR fairness retransmit",
                        "match": "all",
                        "expect_paths": ("sources/source-register.md",),
                    },
                ),
            )
            self.assertTrue(report["passed"])
            self.assertEqual(report["passed_cases"], 1)

    def test_git_checkout_respects_ignore_rules_but_includes_new_markdown(self) -> None:
        with tempfile.TemporaryDirectory(prefix="corpus-retrieval-git-test-") as tmp:
            root = Path(tmp)
            subprocess.run(["git", "init"], cwd=root, check=True, text=True, capture_output=True)
            (root / ".gitignore").write_text("ignored.md\n", encoding="utf-8")
            (root / "README.md").write_text("# Tracked\n", encoding="utf-8")
            (root / "draft.md").write_text("# New untracked corpus note\n", encoding="utf-8")
            (root / "ignored.md").write_text("# Ignored local note\n", encoding="utf-8")
            subprocess.run(["git", "add", ".gitignore", "README.md"], cwd=root, check=True, text=True, capture_output=True)

            files = [path.relative_to(root).as_posix() for path in corpus_retrieval.iter_markdown_files(root)]
            self.assertEqual(files, ["draft.md", "README.md"])


if __name__ == "__main__":
    unittest.main()
