#!/usr/bin/env python3
"""Convert preserved DOCX research sources into navigable Markdown chapters.

The conversion intentionally keeps source wording intact. It only introduces
Markdown heading markers for Word heading styles, table syntax for Word
tables, and a provenance header identifying the immutable source document.
"""

from __future__ import annotations

import hashlib
import re
import sys
from pathlib import Path

from docx import Document
from docx.table import Table
from docx.text.paragraph import Paragraph


ROOT = Path(__file__).resolve().parents[1]
SOURCE_DIR = ROOT / "sources" / "original-docx"
OUTPUT_DIR = ROOT / "chapters"

CHAPTERS = {
    "Research Master.docx": ("Research Master", "00-research-master.md"),
    "CursiveOS_First_Principles_Report.docx": (
        "First Principles and Strategy",
        "01-first-principles-and-strategy.md",
    ),
    "1. TAO-OS Research and Viability Report.docx": (
        "Market and Viability",
        "02-market-and-viability.md",
    ),
    "2. Linux kernel optimizations.docx": (
        "Linux Kernel Optimization",
        "03-linux-kernel-optimization.md",
    ),
    "3. GPU Kernel Tweaks for Mining_AI.docx": (
        "GPU and Accelerator Tuning",
        "04-gpu-and-accelerator-tuning.md",
    ),
    "5. ai guided tuning_.docx": ("AI-Guided Tuning", "05-ai-guided-tuning.md"),
    "6. Hardening linux.docx": (
        "Security and Hardening",
        "06-security-and-hardening.md",
    ),
    "4. Tokenomics_.docx": (
        "Tokenomics and Incentives",
        "07-tokenomics-and-incentives.md",
    ),
}


def blob_sha(path: Path) -> str:
    content = path.read_bytes()
    return hashlib.sha1(f"blob {len(content)}\0".encode() + content).hexdigest()


def iter_blocks(document: Document):
    for child in document.element.body.iterchildren():
        if child.tag.endswith("}p"):
            yield Paragraph(child, document)
        elif child.tag.endswith("}tbl"):
            yield Table(child, document)


def heading_prefix(style_name: str) -> str | None:
    match = re.match(r"Heading\s+(\d+)", style_name or "", flags=re.IGNORECASE)
    if match:
        return "#" * int(match.group(1))
    return None


def escape_cell(text: str) -> str:
    clean = re.sub(r"\s*\n\s*", "<br>", text.strip())
    return clean.replace("|", r"\|")


def render_table(table: Table) -> list[str]:
    rows = [[escape_cell(cell.text) for cell in row.cells] for row in table.rows]
    if not rows:
        return []
    width = max(len(row) for row in rows)
    rows = [row + [""] * (width - len(row)) for row in rows]
    lines = ["| " + " | ".join(rows[0]) + " |"]
    lines.append("| " + " | ".join("---" for _ in range(width)) + " |")
    lines.extend("| " + " | ".join(row) + " |" for row in rows[1:])
    return lines


def convert(source: Path, title: str, destination: Path) -> None:
    document = Document(str(source))
    lines = [
        "<!--",
        "Generated from a preserved DOCX source; wording is retained from the source.",
        f"Source: sources/original-docx/{source.name}",
        f"Git blob SHA: {blob_sha(source)}",
        "-->",
        "",
        f"# {title}",
        "",
    ]
    blank_pending = False
    for block in iter_blocks(document):
        if isinstance(block, Paragraph):
            text = block.text.rstrip()
            if not text.strip():
                blank_pending = True
                continue
            if blank_pending and lines[-1] != "":
                lines.append("")
            blank_pending = False
            prefix = heading_prefix(block.style.name if block.style else "")
            if "\n" in text:
                lines.extend(["```bash", text, "```"])
            elif prefix and not text.lstrip().startswith("#"):
                lines.append(f"#{prefix} {text.strip()}")
            elif text.lstrip().startswith("#"):
                lines.append(f"#{text}")
            else:
                lines.append(text)
            lines.append("")
        else:
            if lines[-1] != "":
                lines.append("")
            lines.extend(render_table(block))
            lines.append("")
    destination.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")


def normalized(text: str) -> str:
    text = text.replace(r"\|", "|").replace("<br>", " ")
    text = re.sub(r"^#+\s+", "", text, flags=re.MULTILINE)
    return re.sub(r"\s+", " ", text).strip()


def verify(source: Path, destination: Path) -> tuple[int, int]:
    document = Document(str(source))
    markdown = normalized(destination.read_text(encoding="utf-8"))
    checked = 0
    missing: list[str] = []
    for block in iter_blocks(document):
        values: list[str]
        if isinstance(block, Paragraph):
            values = [block.text]
        else:
            values = [cell.text for row in block.rows for cell in row.cells]
        for value in values:
            candidate = normalized(value)
            if not candidate:
                continue
            checked += 1
            if candidate not in markdown:
                missing.append(candidate[:100])
    if missing:
        print(f"FAIL {source.name}: {len(missing)} blocks missing from {destination.name}")
        for excerpt in missing[:5]:
            print(f"  missing: {excerpt}")
        return checked, len(missing)
    print(f"PASS {source.name}: {checked} text/table blocks retained")
    return checked, 0


def main() -> int:
    OUTPUT_DIR.mkdir(exist_ok=True)
    failures = 0
    total_blocks = 0
    for source_name, (title, output_name) in CHAPTERS.items():
        source = SOURCE_DIR / source_name
        destination = OUTPUT_DIR / output_name
        if not source.exists():
            print(f"FAIL missing source: {source}")
            failures += 1
            continue
        convert(source, title, destination)
        checked, missing = verify(source, destination)
        total_blocks += checked
        failures += missing
    if failures:
        print(f"Coverage verification failed: {failures} missing blocks.")
        return 1
    print(f"Coverage verification passed: {total_blocks} non-empty source blocks retained.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
