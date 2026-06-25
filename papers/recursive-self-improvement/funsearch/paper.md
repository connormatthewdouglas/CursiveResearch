# Mathematical discoveries from program search with large language models (FunSearch) — Full Text

**Source:** https://www.nature.com/articles/s41586-023-06924-6
**PDF:** https://www.nature.com/articles/s41586-023-06924-6.pdf
**Retrieved:** 2026-06-25
**License:** Creative Commons Attribution 4.0 International (CC BY 4.0), per Nature article page.
**Rights Status:** full-text allowed for corpus storage and redistribution with attribution under CC BY 4.0.
**Extraction:** PDF text extracted with `pdftotext -layout`; formatting/line breaks are not authoritative.

---

Article

Mathematical discoveries from program
search with large language models

https://doi.org/10.1038/s41586-023-06924-6  Bernardino Romera-Paredes1,4, Mohammadamin Barekatain1,4, Alexander Novikov1,4,
Received: 12 August 2023                    Matej Balog1,4, M. Pawan Kumar1,4, Emilien Dupont1,4, Francisco J. R. Ruiz1,4,
Accepted: 30 November 2023                  Jordan S. Ellenberg2, Pengming Wang1, Omar Fawzi3, Pushmeet Kohli1 & Alhussein Fawzi1,4
Published online: 14 December 2023
Open access                                 Large language models (LLMs) have demonstrated tremendous capabilities in solving
                                            complex tasks, from quantitative reasoning to understanding natural language.
    Check for updates                       However, LLMs sometimes suffer from confabulations (or hallucinations), which can
                                            result in them making plausible but incorrect statements1,2. This hinders the use of
                                            current large models in scientific discovery. Here we introduce FunSearch (short for
                                            searching in the function space), an evolutionary procedure based on pairing a
                                            pretrained LLM with a systematic evaluator. We demonstrate the effectiveness of
                                            this approach to surpass the best-known results in important problems, pushing
                                            the boundary of existing LLM-based approaches3. Applying FunSearch to a central
                                            problem in extremal combinatorics--the cap set problem--we discover new
                                            constructions of large cap sets going beyond the best-known ones, both in finite
                                            dimensional and asymptotic cases. This shows that it is possible to make discoveries
                                            for established open problems using LLMs. We showcase the generality of FunSearch
                                            by applying it to an algorithmic problem, online bin packing, finding new heuristics
                                            that improve on widely used baselines. In contrast to most computer search
                                            approaches, FunSearch searches for programs that describe how to solve a problem,
                                            rather than what the solution is. Beyond being an effective and scalable strategy,
                                            discovered programs tend to be more interpretable than raw solutions, enabling
                                            feedback loops between domain experts and FunSearch, and the deployment of such
                                            programs in real-world applications.

Many problems in mathematical sciences are `easy to evaluate', despite     leading to important improvements on diverse synthetic problems16,
being typically `hard to solve'. For example, in computer science,         searching for neural network architectures1719 and solving puzzles20.
NP-complete optimization problems admit a polynomial-time evalu-           Our proposed method, FunSearch, pushes the boundary of LLM-guided
ation procedure (measuring the quality of the solution), despite the       evolutionary procedures to a new level: the discovery of new scien-
widespread belief that no polynomial-time algorithms to solve such         tific results for established open problems and the discovery of new
problems exist. We focus in this paper on problems admitting an effi-      algorithms. Surpassing state-of-the-art results on established open
cient `evaluate' function, which measures the quality of a candidate       problems provides a clear indication that the discoveries are truly new,
solution. Prominent examples include the maximum independent               as opposed to being retrieved from the LLM's training data.
set problem and maximum constraint satisfaction problems (such
as finding the ground state energy of a Hamiltonian). Our goal is to          FunSearch (short for searching in the function space) combines a
generate a `solve' program, such that its outputs receive high scores      pretrained (frozen) LLM, whose goal is to provide creative solutions,
from the `evaluate' function (when executed on inputs of interest), and    with an evaluator, which guards against confabulations and incor-
ultimately improve on the best-known solutions.                            rect ideas. FunSearch iterates over these two components, evolving
                                                                           initial low-scoring programs into high-scoring ones discovering new
   Whereas large language models (LLMs) have recently seen nota-           knowledge. Key to the success of this simple procedure is a combina-
ble improvements in their coding capabilities48, with applications        tion of several essential ingredients. First, we sample best performing
including debugging9,10, solving code competitions11,12 and improving      programs and feed them back into prompts for the LLM to improve on;
code performance13, synthesizing `solve' programs for open problems        we refer to this as best-shot prompting. Second, we start with a program
requires finding new ideas that are verifiably correct. This is very hard  in the form of a skeleton (containing boilerplate code and potentially
for LLMs, as they tend to confabulate or ultimately fall short of going    known structure about the problem), and only evolve the part govern-
beyond existing results. To surpass the `nominal' capabilities of LLMs,    ing the critical program logic. For example, by setting a greedy program
recent studies3 have combined them with evolutionary algorithms14,15,      skeleton, we evolve a priority function used to make decisions at every

1Google DeepMind, London, UK. 2Department of Mathematics, University of Wisconsin-Madison, Madison, WI, USA. 3Laboratoire de l'Informatique du Paralllisme, University of Lyon (Inria, ENS

Lyon, UCBL, LIP), Lyon, France. 4These authors contributed equally: Bernardino Romera-Paredes, Mohammadamin Barekatain, Alexander Novikov, Matej Balog, M. Pawan Kumar, Emilien
Dupont, Francisco J. R. Ruiz, Alhussein Fawzi. e-mail: brp@google.com; pushmeet@google.com; afawzi@google.com

468|Nature|Vol 625|18 January 2024
                                            FunSearch                             Evaluation
                       Pretrained LLM

Speci cation                                                                                  New program
        ??

                    ?

              Prompt

                       Programs
                       database

Fig. 1 | Overview of FunSearch. The input to FunSearch is a specification of the  fed to the pretrained LLM and new programs are created. Newly created
problem in the form of an `evaluate' function, an initial implementation of the   programs are then scored and stored in the programs database (if correct),
function to evolve, which can be trivial, and potentially a skeleton. At each     thus closing the loop. The user can at any point retrieve the highest-scoring
iteration, FunSearch builds a prompt by combining several programs sampled        programs discovered so far.
from the programs database (favouring high-scoring ones). The prompt is then

step. Third, we maintain a large pool of diverse programs by using an             program in the form of a skeleton (containing boilerplate code and
island-based evolutionary method that encourages exploration and                  previous knowledge of the problem in the form of a program structure),
avoids local optima. Finally, leveraging the highly parallel nature of            and only use FunSearch to evolve the critical part that governs its logic.
FunSearch, we scale it asynchronously, considerably broadening the                Fig. 2a shows an example in which the skeleton takes the form of a
scope of this approach to find new results, while keeping the overall             simple greedy algorithm, and the crucial part to evolve by FunSearch is
cost of experiments low.                                                          the priority function that is used to make the greedy decision at every
                                                                                  step. This delegates to FunSearch precisely the part that is usually the
   We show the surprising effectiveness of FunSearch on several use               hardest to come up with. Whereas a fixed skeleton may constrain the
cases. We consider a fundamental problem in extremal combina-                     space of programs that can be discovered, we find it improves over-
torics, namely, the cap set problem21,22. FunSearch demonstrates the              all results because it focuses the LLM resources on only evolving the
existence of hitherto unknown constructions that go beyond existing               critical part, instead of also using the LLM to recreate already known
ones, including the largest improvement in 20years to the asymptotic              program structures (with more opportunities for mistakes that would
lower bound. This demonstrates that it is possible to make a scientific           render the entire program incorrect). If available, the user can option-
discovery--a new piece of verifiable knowledge about a notorious                  ally provide extra known information about the problem at hand, in the
scientific problem--using an LLM. Using FunSearch, we also find new               form of docstrings, relevant primitive functions or import packages,
algorithms for the online bin packing problem that improve on tradi-              which FunSearch may use.
tional ones on well-studied distributions of interest23,24, with potential
applications to improving job scheduling algorithms.                              Pretrained LLM

   Whereas most computer search techniques output directly what the               The LLM is the creative core of FunSearch, in charge of coming up with
solution is (for example, a list of vectors forming a cap set), FunSearch         improvements to the functions presented in the prompt and sending
produces programs generating the solution. For structured problems,               these for evaluation. We obtain our results with a pretrained model,
such programs tend to be more interpretable--facilitating interac-                that is, without any fine-tuning on our problems. We use Codey, an LLM
tions with domain experts--and concise--making it possible to scale               built on top of the PaLM2 model family25, which has been fine-tuned
to large instances--compared to a mere enumeration of the solution.               on a large corpus of code and is publicly accessible through its API26.
In addition, decision procedures (such as for bin packing) described              Because FunSearch relies on sampling from an LLM extensively, an
by code in a standard programming language are crucially easier to                important performance-defining tradeoff is between the quality of the
deploy compared to other types of descriptions (for example, neural               samples and the inference speed of the LLM. In practice, we have cho-
networks), which typically require specialized hardware and for which             sen to work with a fast-inference model (rather than slower-inference,
verifying design specifications is notoriously hard.                              higher-quality), and the results in the paper are obtained using a total
                                                                                  number of samples on the order of 106. Beyond this tradeoff, we have
FunSearch                                                                         empirically observed that the results obtained in this paper are not too
                                                                                  sensitive to the exact choice of LLM, as long as it has been trained on a
An overview of FunSearch is shown in Fig. 1, and its components are               large enough corpus of code. See Supplementary Information Appen-
described in more detail below. For more details and ablations showing            dix A for a comparison to StarCoder6, a state-of-the-art open-source
the importance of each component, see Methods and Supplementary                   LLM for code.
Information Appendix A.

Specification                                                                     Evaluation

The input to FunSearch is a specification of the problem in the form of           Programs generated by the LLM are evaluated and scored on a set of
an `evaluate' function, which scores candidate solutions. In addition,            inputs. For example, in the cap set problem (`Extremal combinatorics'
we provide an initial program (which can be trivial) to evolve. Although          section) the inputs are the values of the dimensionality n that we are
in principle these are the minimum requirements, we found that per-               interested in, and in combinatorial optimization (`Bin packing' section),
formance tends to improve significantly if we write the initial `solve'           the inputs correspond to different bin packing instances. The scores

                                                                                              Nature|Vol 625|18 January 2024|469
Article

         a                                                                            b

         """Finds large cap sets."""                                                  """Finds good assignment for online 1d bin
         import numpy as np                                                            packing."""
         import utils_capset                                                          import numpy as np
                                                                                      import utils_packing
         # Function to be executed by FunSearch.
         def main(n):                                                                 # Function to be executed by FunSearch.
                                                                                      def main(problem):
            """Runs `solve` on `n`-dimensional cap set and
             evaluates the output."""                                                    """Runs `solve` on online 1d bin packing instance,
            solution = solve(n)                                                            and evaluates the output."""
            return evaluate(solution, n)                                                 bins = problem.bins
                                                                                         # Packs `problem.items` into `bins` online.
         def evaluate(candidate_set, n):                                                 for item in problem.items:
            """Returns size of candidate_set if it is a cap
             set, None otherwise."""                                                        # Extract bins that have space to fit item.
            if utils_capset.is_capset(candidate_set, n):                                    valid_bin_indices =
               return len(candidate_set)                                                      utils_packing.get_valid_bin_indices(item,
            else:                                                                             bins)
               return None                                                                  best_index = solve(item,
                                                                                              bins[valid_bin_indices])
         def solve(n):                                                                      # Add item to the selected bin.
            """Builds a cap set of dimension `n` using                                      bins[valid_bin_indices[best_index]] -= item
             `priority` function."""                                                     return evaluate(bins, problem)
            # Precompute all priority scores.
            elements = utils_capset.get_all_elements(n)                               def evaluate(bins, problem):
            scores = [priority(el, n) for el in elements]                                """Returns the negative of the number of bins
            # Sort elements according to the scores.                                       required to pack items in `problem`."""
            elements = elements[np.argsort(scores,                                       if utils_packing.is_valid_packing(bins, problem):
             kind='stable')[::-1]]                                                              return -utils_packing.count_used_bins(bins,
                                                                                                 problem)
            # Build `capset` greedily, using scores for                                  else:
             prioritization.                                                                return None
            capset = []
            for element in elements:                                                  def solve(item, bins):
                                                                                         """Selects the bin with the highest value according
               if utils_capset.can_be_added(element, capset):                              to `heuristic`."""
                  capset.append(element)                                                    scores = heuristic(item, bins)
                                                                                            return np.argmax(scores)
            return capset
                                                                                      # Function to be evolved by FunSearch.
         # Function to be evolved by FunSearch.                                       def heuristic(item, bins):
         def priority(element, n):
                                                                                         """Returns priority with which we want to add
            """Returns the priority with which we want to add                              `item` to each bin."""
             `element` to the cap set."""                                                return -(bins - item)
            return 0.0
                                                                                     evaluation procedure by connecting the pieces together. Specifically, it uses
Fig. 2 | Examples of FunSearch specifications for two problems. The
`evaluate' function takes as input a candidate solution to the problem, and          the `solve' function to solve the problem and then scores the resulting solutions
returns a score assessing it. The `solve' function contains the algorithm
skeleton, which calls the function to evolve that contains the crucial logic.        using the `evaluate' function. In the simplest cases, `main' just executes `solve'
a, Cap set. The function to evolve is called `priority'. b, Online bin packing. The
function to evolve is called `heuristic'. The `main' function implements the         once and uses `evaluate' to score the output, for example, a. In specific settings

                                                                                     such as online algorithms, the `main' function implements some more logic, for

                                                                                     example, b.

across different inputs are then combined into an overall score of the               according to the procedure described above. Sampled programs are
program using an aggregation function, such as the mean. The scored                  then sorted according to their score, and a version is assigned to each
programs are then sent to the programs database. Programs that were                  (`v0' for the lowest scoring program, `v1' for the second lowest scoring
incorrect (that did not execute within the imposed time and memory                   and so on). These programs are then combined into a single prompt--
limits, or produced invalid outputs) are discarded, and the remaining                with the version appended as a suffix to the function name; for example,
scored programs are then sent to the programs database.                              in the case of Fig. 2a, this would be `priority_v0', `priority_v1', ...--and the
                                                                                     header of the function we wish to generate (for example, `priority_vk') is
Programs database                                                                    added to the end of the prompt. In practice, we set k=2, as two functions
The programs database keeps a population of correct programs, which                  lead to better results compared to just one, with diminishing returns
are then sampled to create prompts. Preserving and encouraging diver-                beyond that. Constructing a prompt by combining several programs
sity of programs in the database is crucial to enable exploration and                (as opposed to only one) enables the LLM to spot patterns across the
avoid being stuck in local optima. To encourage diversity, we adopt an               different programs and generalize those. Related approaches to prompt
islands model, also known as a multiple population and multiple-deme                 building have been recently considered, for example ref. 16, and were
model27,28, which is a genetic algorithm approach. Several islands, or               shown to perform well on different domains.
subpopulations, are created and evolved independently. To sample
from the program database, we first sample an island and then sample                 Distributed approach
a program within that island, favouring higher-scoring and shorter                   We implement FunSearch as a distributed system that has three types of
programs (see Methods for the exact mechanism). Crucially, we let                    workers--a programs database, samplers and evaluators--which com-
information flow between the islands by periodically discarding the                  municate asynchronously. The programs database stores and serves
programs in the worst half of the islands (corresponding to the ones                 programs, samplers generate new functions using the pretrained LLM
whose best individuals have the lowest scores). We replace the pro-                  and evaluators assess programs, as shown in Supplementary Fig. F.26.
grams in those islands with a new population, initialized by cloning                 In the example shown in Fig. 2a, the programs database stores priority
one of the best individuals from the surviving islands.                              functions, samplers generate new implementations of `priority' and
                                                                                     evaluators score the proposals by executing the `main' function on
Prompt                                                                               user-specified inputs. Our distributed system offers several advan-
New prompts are created by `best-shot prompting' from the programs                   tages. First, it naturally leverages parallelism across different tasks: for
database, and are then fed to the LLM to generate a new program. We                  example, LLM sampling and evaluation are performed concurrently.
first sample k programs from a single island in the programs database,               Second, it enables scaling to more than one sampler and evaluator,

470|Nature|Vol 625|18 January 2024
Fig. 3 | Diagram of a cap set of size four in Z23. The circles are the elements of Z23  immediately led to a series of other combinatorial results, for example,
with the ones belonging to the cap set shown in blue. The possible lines in Z23 are     on the ErdsRadio sunflower problem32.
also shown (with colours indicating lines that wrap around in arithmetic
modulo 3). No three elements of the cap set are in a line.                                 The exact size of the largest possible cap set in n dimensions is known

which would be a very limiting setup, considering that evaluation can                   only for n6. A brute force approach is not practical as the search space
take minutes for many problems of interest. Running evaluators in                       quickly becomes enormous with growing n, for example, around 31,600
parallel considerably broadens the scope of this approach to such
problems. The distributed setting enables the running of many evalu-                    for n=8. Previous methods impose potentially suboptimal restrictions
ator nodes on inexpensive CPU hardware, whereas few samplers run                        on the search space33,34. By contrast, we search the full space by means
on machines with accelerators for fast LLM inference; this keeps the                    of an algorithm skeleton that uses a function `priority' : Zn3  R. Intui-
overall cost and energy usage of experiments low. In our experiments,                   tively, this function provides a priority with which each x  Zn3 should
we typically use 15 samplers and 150 CPU evaluators (can be served                      be included in the cap set. Our algorithm starts with an empty set and
on five CPU servers each running 32 evaluators in parallel). See Sup-                   iteratively adds the vector x  Zn3 with the highest priority that does
plementary Information Appendix A for more details. Also, because of                    not violate the cap set constraint; Fig. 2a. Starting from a trivial constant
the randomness of LLM sampling and the evolutionary procedure, for
some problems we run several experiments to get the best reported                       function, we evolve the crucial `priority' component of our approach
results. See Methods and Supplementary Information Appendix A.3
for a full statistical analysis.                                                        to result in large cap sets.

   We now describe some of the new discoveries made by FunSearch in                        Using this approach, we discovered cap sets of sizes shown in Fig. 4a.
two different fields: pure mathematics and applied computer science.
Further discoveries on other problems (namely, the corners problem                      Notably, in dimension n=8, FunSearch found a larger cap set than what
and Shannon capacity of cycle graphs) are presented in Supplementary
Information Appendix B. The full discovered programs are available                      was previously known, thus illustrating the power of FunSearch to
in Supplementary Information Appendix C.
                                                                                        discover new constructions. This also shows the scalability of FunSearch
Extremal combinatorics
                                                                                        to larger dimensions, in which the previously best-known construction
We apply FunSearch to two related problems in extremal combinato-                       relied on a complex combination of cap sets in lower dimensions33,34.
rics: a branch of mathematics that studies the maximal (or minimal)
possible sizes of sets satisfying certain properties.                                   By contrast, FunSearch discovered a larger cap set from scratch, with-

Cap sets                                                                                out having to be explicitly taught any way of combining cap sets.
The cap set problem21, once described by Terence Tao as `perhaps my
favourite open question'29, refers to the task of finding the largest pos-              Moreover, we do not just discover the set of 512 eight-dimensional
sible set of vectors inZn3 (known as a cap set) such that no three vectors
sum to zero. Geometrically, no three points of a cap set are in a line (see             vectors in itself, but a program that generates it: we show this program
Fig. 3 for an example with n=2).
                                                                                        in Fig. 4b. Through inspecting the code, we obtain a degree of under-
   The problem has drawn much interest for a variety of reasons. For
one, it is an analogue of the classical number theory problem of finding                standing of what this set is: specifically, manual simplification of Fig. 4b
large subsets of primes in which no three are in arithmetic progres-
sion. For another, it differs from many problems in combinatorics in                    provides the construction in Fig. 4c. Some properties of this construc-
that there is no consensus among mathematicians about what the                          tion are similar to the construction of the Hill cap35,36, which results in
right answer should be. Finally, the problem serves as a model for the                  the optimal 112-cap in Z36.
many other problems involving `three-way interactions'. For instance,
progress towards improved upper bounds for the cap set problem30,31                     Admissible sets

                                                                                        Beyond finding the size of the largest cap set cn in dimension n, a fun-

                                                                                        damental problem in additive combinatorics22 is determining the
                                                                                        capacityC = sup cn1/n. The breakthrough result from ref. 31 established
                                                                                        an upper bounnd of C2.756. In this work, we are interested in lower

                                                                                        bounds on C. To this end, we use the framework of constant weight
                                                                                        admissible sets (or admissible sets for short)34,37, which has established

                                                                                        the current state-of-the-art.

                                                                                        Formally, admissible sets A(n, w)are collections of vectors in {0,1,2}n

                                                                                        satisfying two properties: (1) each vector has the same number w of
                                                                                        ( ) non-zero elements but a unique support (thereforeA n
                                                                                                                                               w       ); (2) for

                                                                                        any three distinct vectors there is a coordinate in which their three

                                                                                        respective values are {0,1,2},{0,0,1} or {0,0,2}. Informally, an admis-

                                                                                        sible set describes how to combine cap sets in smaller dimensions into

                                                                                        large cap sets in higher dimensions34. We denote the set of full-size
                                                                                        ( ) admissible sets (withA =n
                                                                                                                    w  ) as I(n, w). The current state-of-the-art38

                                                                                        has relied on SAT solvers to construct large admissible sets.

                                                                                        As before, we evolve a function `priority' :{0, 1, 2}n  R, which is used

                                                                                        to iteratively grow admissible sets. Starting from a trivial constant

                                                                                        function, we discover one that provides us with an I(12, 7) admissible

                                                                                        set; the discovered program is shown in Fig. 5b. This discovery alone

                                                                                        already improves the lower bound on the cap set capacity from 2.2180

                                                                                        (ref. 38) to 2.2184. Yet, interpreting the program found by FunSearch

                                                                                        (Fig. 5b) helps us significantly push the boundaries of what admissible

                                                                                        sets we can construct. Specifically, we notice that the discovered

                                                                                        `priority' function treats the n coordinates in a highly symmetric way,

                                                                                        and indeed it turns out that the admissible set it constructs is preserved

                                                                                        under independent cyclic permutations of coordinates within four

                                                                                        disjoint groups of coordinate triples. Hereinafter we call such admis-

                                                                                        sible sets symmetric (see Supplementary Information Appendix D for

                                                                                        a formal definition).

                                                                                        We now use FunSearch to directly search for symmetric admissible

                                                                                        sets. Note that this is a more restricted and also much smaller search

                                                                                        space, which allows for significantly higher dimensions and weights

                                                                                        than were previously possible. This led us to discovering a full-size

                                                                                                                       Nature|Vol 625|18 January 2024|471
Article

         a

                                    n           3  4                                    5   6    7    8

            Best known 9                           20                                   45  112  236  496
            FunSearch 9
                                                   20                                   45  112  236  512

         b                                      c

         def priority(el: tuple[int,...],       def build_512_cap() -> list[tuple[int,...]]:
          n: int) -> float:                        5HWXUQV D FDS VHW RI VL]H  LQ CQ C GLPHQVLRQV
                                                   n=8
            score = n                              V = np.array(list(itertools.product(range(3), repeat=n)), dtype=np.int32)
            in_el = 0                              support = lambda v: tuple(i for i in range(n) if v[i] !=0)
            el_count = el.count(0)                 reflections = lambda v:sum (1 for i in range(1, n// 2) if v[i] == v[-i])

            if el_count == 0:                       $GG DOO  ZHLJKW YHFWRUV WKDW KDYH !  UHIOHFWLRQV
               score += n**2                       weight8_vectors = [v for v in V
               if el[1] == el[-1]:
                  score *= 1.5                                                       if np.count_nonzero(v) == 8  :HLJKW LV 
               if el[2] == el[-2]:                                                   and reflections(v) >= 2]  $W OHDVW  UHIOHFWLRQV
                  score *= 1.5
               if el[3] == el[-3]:                  $GG DOO  ZHLJKW YHFWRUV WKDW KDYH VSHFLILF VXSSRUW
                  score *= 1.5                     supports_16 = [(0, 1, 2, 3), (0, 1, 2, 5), (0, 3, 6, 7), (0, 5, 6, 7),

            else:                                                             (1, 3, 4, 6), (1, 4, 5, 6), (2, 3, 4, 7), (2, 4, 5, 7)]
               if el[1] == el[-1]:                 weight4_vectors = [v for v in V
                  score *= 0.5
               if el[2] == el[-2]:                                                   if support(v) in supports_16]
                  score *= 0.5
                                                    $GG DOO  ZHLJKW YHFWRUV ZLWK VSHFLILF VXSSRUW DQG  UHIOHFWLRQ
            for e in el:                           supports_8 = [(0, 1, 2, 7), (0, 1, 2, 6), (0, 1, 3, 7), (0, 1, 6, 7),
               if e == 0:
                  if in_el == 0:                                            (0, 1, 5, 7), (0, 2, 3, 6), (0, 2, 6, 7), (0, 2, 5, 6),
                     score *= n * 0.5                                       (1, 2, 4, 7), (1, 2, 4, 6), (1, 3, 4, 7), (1, 4, 6, 7),
                  elif in_el == el_count - 1:                               (1, 4, 5, 7), (2, 3, 4, 6), (2, 4, 6, 7), (2, 4, 5, 6)]
                     score *= 0.5                  weight4_vectors_2 = [v for v in V
                  else:
                     score *= n * 0.5 ** in_el                                           if support(v) in supports_8
                  in_el += 1                                                             and reflections(v) == 1]  ([DFWO\  UHIOHFWLRQ
               else:
                  score += 1                        $GG  ZHLJKW YHFWRUV ZLWK   UHIOHFWLRQV DQG RQH PRUH FRQGLWLRQ
                                                   allowed_zeros = [(0, 4, 7), (0, 2, 4), (0, 1, 4), (0, 4, 6),
            if el[1] == el[-1]:
               score *= 1.5                                                       (1, 2, 6), (2, 6, 7), (1, 2, 7), (1, 6, 7)]
                                                   weight5_vectors = [
            if el[2] == el[-2]:
               score *= 1.5                              v for v in V
                                                         if tuple(i for i in range(n) if v[i] == 0) in allowed_zeros
            return score                                 and reflections(v) <= 1  $W PRVW  UHIOHFWLRQ
                                                         and (v[1] * v[7]) % 3 != 1 and (v[2] * v[6]) % 3 != 1]

                                                   return weight8_vectors + weight4_vectors + weight4_vectors_2 +
                                                    weight5_vectors

Fig. 4 | Result of applying FunSearch to the cap set problem. a, Size of the               This motivates the notion of reflections, used in c. c, An explicit construction
largest cap set in Z3n for different dimensions n. b, The function `priority' : Zn3  R     of this new 512-cap, which we were able to manually construct thanks to having
discovered by FunSearch that results in a cap set of size 512 in n=8 dimensions.           discovered the cap set by searching in function space. See Supplementary
                                                                                           Information Appendix E.2 for more details and for relation to Hill cap.
One feature to note is that the priority is affected by whether the same entry

appears in positions i and -i (-i denotes the ith position counting from the end).

I(15, 10) admissible set (indicating C2.219486) and a partial admis-                       is crucial for obtaining strong performance, but designing a good heu-
sible set in A(24, 17) of size 237,984, which implies a new lower bound                    ristic is difficult in practice. In this section, we show that FunSearch can
on the cap set capacity of 2.2202 (Fig. 5a). Although this is a great                      be used to discover effective heuristics for one of the central problems
improvement to the lower bound compared to research in the last                            in combinatorial optimization: bin packing39.
20years, we note it is still far from the upper bound and we hope our
results inspire future work on this problem.                                                  The goal of bin packing is to pack a set of items of various sizes into
                                                                                           the smallest number of fixed-sized bins. Bin packing finds applications
   Not only does FunSearch scale to much larger instances than tradi-                      in many areas, from cutting materials to scheduling jobs on compute
tional combinatorial solvers (Supplementary Information Appendix                           clusters. We focus on the online setting in which we pack an item as
A.4), but it is also a unique feature of searching in function space that we               soon as it is received (as opposed to the offline setting in which we have
were able to inspect the code discovered by FunSearch and infer a new                      access to all items in advance). Solving online bin packing problems
insight into the problem, in the form of a new symmetry. The procedure                     then requires designing a heuristic for deciding which bin to assign
we followed in this section is a concrete example of how LLM-based                         an incoming item to.
approaches can be used in mathematical sciences: FunSearch suggests
a solution, which is examined by researchers, who may note features of                        Heuristics for online bin packing are well studied and several variants
interest. These features are used to refine the search, leading to better                  exist with strong worst case performance4045. However, they often
solutions. This process can be iterated, with both human and search                        show poor performance in practice39. Instead, the most commonly
consistently in the loop.                                                                  used heuristics for bin packing are first fit and best fit. First fit places
                                                                                           the incoming item in the first bin with enough available space, whereas
Bin packing                                                                                best fit places the item in the bin with least available space where the
                                                                                           item still fits. Here, we show that FunSearch discovers better heuristics
Combinatorial optimization is a subfield of mathematics that plays an                      than first fit and best fit on simulated data.
important role across a wide range of areas, from theoretical computer
science to practical problems in logistics and scheduling. Whereas                            To achieve this, we define a heuristic as a program that takes as
many combinatorial optimization problems are provably hard to solve                        input an item and an array of bins (containing the remaining capacity
for large instances, it is typically possible to achieve strong performance                of each bin) and returns a priority score for each bin. The `solve' func-
using heuristics to guide the search algorithm. The choice of a heuristic                  tion picks the bin with the highest score according to the heuristic
                                                                                           (Fig. 2b). FunSearch is then used to evolve this heuristic, starting from
                                                                                           best fit.

472|Nature|Vol 625|18 January 2024
a                                                                                    Table 1 | Online bin packing results

   Bound   Admissible set  Source                                                               OR1 OR2 OR3 OR4 Weibull Weibull Weibull
    on &      ingredient

   2.2101  ! (90, 89)      Ref. 37                                                                                         5k  10k  100k
   2.2173  ! (10, 5)       Ref. 34
   2.2180  ! (11, 7)       Ref. 38                                                   First fit  6.42% 6.45% 5.74% 5.23% 4.23% 4.20% 4.00%

                                                                                     Best fit   5.81% 6.06% 5.37% 4.94% 3.98% 3.90% 3.79%

            ! (12, 7)                                                                FunSearch 5.30% 4.19% 3.11% 2.47% 0.68% 0.32% 0.03%
           ! (15, 10)
   2.2184   (24, 17)       FunSearch                                                 Fraction of excess bins (lower is better) for various bin packing heuristics on the OR and Weibull
   2.2194                  FunSearch                                                 datasets. FunSearch outperforms first fit and best fit across problems and instance sizes.
   2.2202                  FunSearch

       b                                                                             for 100,000 items). In addition, FunSearch is robust and consistently
                                                                                     outperforms these baselines as shown in the statistical analysis in the
               def priority (el: tuple[int, ...], n: int, w: int) -> float:          Supplementary Information Appendix A.3.
                  score = 0.0
                  for i in range(n):                                                    We observed that several heuristics discovered by FunSearch use
                     if el[i] == 1:                                                  the same general strategy for bin packing (see Fig. 6 for an example).
                                                                                     Instead of packing items into bins with the least capacity (such as best
                         score -= 0.9 ** ( i % 4 )                                   fit), the FunSearch heuristics assign items to least capacity bins only if
                                                                                     the fit is very tight after placing the item. Otherwise, the item is typi-
                     if el[i] == 2:                                                  cally placed in another bin, which would leave more space after the
                                                                                     item is placed. This strategy avoids leaving small gaps in bins that are
                         score -= 0.98 ** (30 - ( i % 4 ))                           unlikely to ever be filled (see Supplementary Information Appendix E.5
                                                                                     for example visualizations of such packings).
                     if el[i] == 1 and el[i - 4] == 1:
                                                                                        As this example demonstrates, the benefits of FunSearch extend
                         score -= 0.98 ** (30 - ( i % 4 ))                           beyond theoretical and mathematical results to practical problems
                                                                                     such as bin packing. Indeed, bin packing, and related combinatorial
                     if el[i] == 2 and el[i - 4] != 0:                               optimization problems, are ubiquitous and find applications across a
                                                                                     range of industries. We are optimistic that FunSearch could be applied
                         score -= 0.98 ** (30 - ( i % 4 ))                           to several such use cases with potential for real-world impact.

                     if el[i] == 2 and el[i - 4] == 1 and el[i - 8] == 2:            Discussion

                         score -= 0.98 ** (30 - ( i % 4 ))                           The effectiveness of FunSearch in discovering new knowledge for hard
                         score -= 6.3                                                problems might seem intriguing. We believe that the LLM used within
                     if el[i] == 2 and el[i - 4] == 2 and el[i - 8] == 1:            FunSearch does not use much context about the problem; the LLM
                                                                                     should instead be seen as a source of diverse (syntactically correct)
                         score -= 0.98 ** (30 - ( i % 4 ))                           programs with occasionally interesting ideas. When further con-
                                                                                     strained to operate on the crucial part of the algorithm with a program
                     if el[i] == 2 and el[i - 4] == 1 and el[i - 8] == 1:            skeleton, the LLM provides suggestions that marginally improve over
                         score -= 6.3                                                existing ones in the population, which ultimately results in discover-
                                                                                     ing new knowledge on open problems when combined with the evo-
                     if el[i] == 2 and el[i - 4] == 0 and el[i - 8] == 2:            lutionary algorithm. Another crucial component of the effectiveness
                         score -= 6.3                                                of FunSearch is that it operates in the space of programs: rather than
                                                                                     directly searching for constructions (which is typically an enormous
                     if el[i] == 1 and el[i - 4] == 1 and el[i - 8] == 0:            list of numbers), FunSearch searches for programs generating those
                         score -= 2.2                                                constructions. Because most problems we care about are structured
                                                                                     (highly non-random), we believe that solutions are described more
                  return score                                                       concisely with a computer program, compared to other representa-
                                                                                     tions. For example, the trivial representation of the admissible set
Fig. 5 | Results on the cap set problem through admissible sets. a, Summary          A(24, 17) consists of more than 200,000 vectors, but the program
of lower bounds on the cap set capacity C. b, The `priority' function {0, 1, 2}n  R  generating this set consists of only a few lines of code. Because Fun-
discovered by FunSearch that results in an I(12, 7) admissible set. The source       Search implicitly encourages concise programs, it scales to much
code shows that when n=12, the function treats the four triples of coordinates       larger instances compared to traditional search approaches in struc-
{0,4,8}, {1,5,9}, {2,6,10} and {3,7,11} together. We then checked that the           tured problems. In a loose sense, FunSearch attempts to find solutions
admissible set is in fact symmetric under independent cyclic permutations of         that have low Kolmogorov complexity4850 (which is the length of the
coordinates within each of these four triples. See Supplementary Information         shortest computer program that produces a given object as output),
Appendices D and E.3 for more details.                                               whereas traditional search procedures have a very different inductive
                                                                                     bias. We believe that such Kolmogorov-compressed inductive bias is
   We first evaluate FunSearch on the well-known OR-Library bin packing              key to FunSearch scaling up to the large instances in our use cases.
benchmarks23, consisting of four datasets, OR1 to OR4, containing bin                In addition to scale, we have empirically observed that FunSearch
packing instances with an increasing number of items (see Supplemen-                 outputs programs that tend to be interpretable: that is, they are clearly
tary Information Appendix E.4 for details). We evolve our heuristic                  easier to read and understand compared to a list of numbers. For
on a training set of generated bin packing instances with the same                   example, by scrutinizing FunSearch's output for the admissible set
number of items as those in OR1 and, after the evolutionary process                  problem, we found a new symmetry, which was then subsequently
is concluded, test it on the OR1 to OR4 datasets. We measure perfor-                 used to improve the results even further. Despite the rarity of
mance as the fraction of excess bins used over the L2 lower bound46 of
the optimal offline packing solution (which is generally not achievable
in the online setting).

   As can be seen in Table 1, FunSearch outperforms both first fit and
best fit across all datasets. Further, the learned heuristic generalizes:
even though it has only seen instances of the same size as OR1 during
training, it generalizes across problem sizes, performing even better on
large instances and widening the gap to best fit. In addition to the OR
benchmarks, we also use FunSearch to evolve heuristics on bin packing
instances sampled from a Weibull distribution, as these closely follow
many real-world scheduling problems24,47 (see Supplementary Informa-
tion Appendix E.4 for details). As shown in Table 1, the performance of
FunSearch is very strong on this dataset, significantly outperforming
first fit and best fit across instances, as well as scaling gracefully to
large instances (being only 0.03% off the lower bound on the optimum

                                                                                                Nature|Vol 625|18 January 2024|473
Article

         def heuristic(item: float, bins: np.ndarray) -> np.ndarray:
            """Online bin packing heuristic discovered with FunSearch."""
            score = 1000 * np.ones(bins.shape)
            # Penalize bins with large capacities.
            score -= bins * (bins-item)
            # Extract index of bin with best fit.
            index = np.argmin(bins)
            # Scale score of best fit bin by item size.
            score[index] *= item
            # Penalize best fit bin if fit is not tight.
            score[index] -= (bins[index] - item)**4
            return score

Fig. 6 | Example of a short online bin packing heuristic discovered by                         encourages packing the item only if the fit is tight. Comments in the code were
FunSearch for the OR dataset. This example illustrates frequently observed                     manually added. See Supplementary Information Appendix C for more
behaviour: instead of always packing items into the best fit bin, the heuristic                discovered heuristics.

symmetric solutions, we observe that FunSearch preferred symmet-                               12. Zelikman, E., Huang, Q., Poesia, G., Goodman, N. D. & Haber, N. Parsel: a (de-)
ric ones, as these are more parsimonious (that is, they require less                                  compositional framework for algorithmic reasoning with language models. Preprint at
information to specify), in addition to the natural bias of LLMs (trained                             https://arxiv.org/abs/2212.10561 (2023).
on human-produced code) in outputting code with similar traits to
human code. This is in contrast to traditional genetic programming                             13. Madaan, A. et al. Learning performance-improving code edits. Preprint at https://arxiv.
that does not have this bias (and in addition requires hand-tuning the                                org/abs/2302.07867 (2023).
mutation operators51).
                                                                                               14. Goldberg, D. E. Genetic Algorithms in Search, Optimization and Machine Learning
   We note that FunSearch, at present, works best for problems having                                 (Addison-Wesley, 1989).
the following characteristics: (1) availability of an efficient evaluator;
(2) a `rich' scoring feedback quantifying the improvements (as opposed                         15. Koza, J. R. Genetic programming as a means for programming computers by natural
to a binary signal) and (3) ability to provide a skeleton with an isolated                            selection. Stat. Comput. 4, 87112 (1994).
part to be evolved. For example, the problem of generating proofs
for theorems5254 falls outside this scope, because it is unclear how                          16. Meyerson, E. et al. Language model crossover: variation through few-shot prompting.
to provide a rich enough scoring signal. By contrast, for MAX-SAT,                                    Preprint at https://arxiv.org/abs/2302.12170 (2023).
the number of satisfied clauses can be used as a scoring signal. In this
paper, we have explicitly striven for simplicity and we are confident                          17. Chen, A., Dohan, D. M. & So, D. R. EvoPrompting: language models for code-level neural
that FunSearch can be further extended to improve its performance                                     architecture search. Preprint at https://arxiv.org/abs/2302.14838 (2023).
and be applicable to more classes of problems. In addition, the rapid
development of LLMs is likely to result in samples of far superior quality                     18. Zheng, M. et al. Can GPT-4 perform neural architecture search? Preprint at https://arxiv.
at a fraction of the cost, making FunSearch more effective at tackling                                org/abs/2304.10970 (2023).
a broad range of problems. As a result, we foresee that automatically
tailored algorithms will soon become common practice and deployed                              19. Nasir, M. U., Earle, S., Togelius, J., James, S. & Cleghorn, C. LLMatic: neural architecture
in real-world applications.                                                                           search via large language models and quality-diversity optimization. Preprint at https://
                                                                                                      arxiv.org/abs/2306.01102 (2023).
Online content
                                                                                               20. Haluptzok, P., Bowers, M. & Kalai, A. T. Language models can teach themselves to
Any methods, additional references, Nature Portfolio reporting summa-                                 program better. In International Conference on Learning Representations (2023).
ries, source data, extended data, supplementary information, acknowl-
edgements, peer review information; details of author contributions                            21. Grochow, J. New applications of the polynomial method: the cap set conjecture and
and competing interests; and statements of data and code availability                                 beyond. Bull. Am. Math. Soc. 56, 2964 (2019).
are available at https://doi.org/10.1038/s41586-023-06924-6.
                                                                                               22. Tao, T. & Vu, V. H. Additive Combinatorics Vol. 105 (Cambridge Univ. Press, 2006).
1. Bang, Y. et al. A multitask, multilingual, multimodal evaluation of ChatGPT on reasoning,   23. Beasley, J. E. OR-library: distributing test problems by electronic mail. J. Oper. Res. Soc.
       hallucination, and interactivity. Preprint at https://arxiv.org/abs/2302.04023 (2023).
                                                                                                      41, 10691072 (1990).
2. Borji, A. A. categorical archive of ChatGPT failures. Preprint at https://arxiv.org/        24. Castieiras, I., De Cauwer, M. & O'Sullivan, B. Weibull-based benchmarks for bin packing.
       abs/2302.03494 (2023).
                                                                                                      In Proc. International Conference on Principles and Practice of Constraint Programming
3. Lehman, J. et al. in Handbook of Evolutionary Machine Learning (eds Banzhaf, W. et al.)            207222 (Springer, 2012).
       331366 (Springer, 2023).                                                               25. Anil, R. et al. Palm 2 technical report. Preprint at https://arxiv.org/abs/2305.10403 (2023).
                                                                                               26. Code models overview. Vertex AI, Google Cloud https://cloud.google.com/vertex-ai/
4. Chen, M. et al. Evaluating large language models trained on code. Preprint at https://             docs/generative-ai/code/code-models-overview (2023).
       arxiv.org/abs/2107.03374 (2021).                                                        27. Tanese, R. Distributed Genetic Algorithms for Function Optimization. PhD thesis, Univ.
                                                                                                      Michigan (1989).
5. Austin, J. et al. Program synthesis with large language models. Preprint at https://arxiv.  28. Cant-Paz, E. A survey of parallel genetic algorithms. Calculateurs Paralleles, Reseaux et
       org/abs/2108.07732 (2021).                                                                     Systemes Repartis 10, 141171 (1998).
                                                                                               29. Tao, T. Open question: best bounds for cap sets. WordPress Blog https://terrytao.
6. Li, R. et al. StarCoder: may the source be with you! Preprint at https://arxiv.org/                wordpress.com/2007/02/23/open-question-best-bounds-for-cap-sets/ (2009).
       abs/2305.06161 (2023).                                                                  30. Croot, E., Lev, V. F. & Pach, P. P. Progression-free sets in are exponentially small. Ann. Math.
                                                                                                      185, 331337 (2017).
7. Fried, D. et al. Incoder: a generative model for code infilling and synthesis. In Proc.     31. Ellenberg, J. S., Gijswijt, D. On large subsets of Fqn with no three-term arithmetic
       International Conference on Learning Representations (2022).                                   progression. Ann. Math. 185, 339343 (2017).
                                                                                               32. Naslund, E. & Sawin, W. Upper bounds for sunflower-free sets. Forum Math. Sigma 5, e15
8. Nijkamp, E. et al. CodeGen: an open large language model for code with multi-turn                  (2017).
       program synthesis. In Proc. International Conference on Learning Representations        33. Edel, Y. & Bierbrauer, J. Large caps in small spaces. Des. Codes Cryptogr. 23, 197212
       (2022).                                                                                        (2001).
                                                                                               34. Edel, Y. Extensions of generalized product caps. Des. Codes Cryptogr. 31, 514 (2004).
9. Chen, X., Lin, M., Schrli, N. & Zhou, D. Teaching large language models to self-debug.     35. Hill, R. On the largest size of cap in S5,3. Rend Lincei. Sci. Fis. Mat. Nat. 54, 378384
       Preprint at https://arxiv.org/abs/2304.05128 (2023).                                           (1973).
                                                                                               36. Cameron, P. J. & Van Lint, J. H. Designs, Graphs, Codes and Their Links Vol. 3 (Cambridge
10. Liventsev, V., Grishina, A., Hrm, A. & Moonen, L. Fully autonomous programming with             Univ. Press, 1991).
       large language models. Preprint at https://arxiv.org/abs/2304.10423 (2023).             37. Calderbank, A. R. & Fishburn, P. C. Maximal three-independent subsets of {0,1,2} n. Des.
                                                                                                      Codes Cryptogr. 4, 203211 (1994).
11. Li, Y. et al. Competition-level code generation with alphacode. Science 378, 10921097     38. Tyrrell, F. New lower bounds for cap sets. Discrete Analysis https://doi.org/10.19086/
       (2022).                                                                                        da.91076 (2023).
                                                                                               39. Coffman, E. G., Garey, M. R. & Johnson, D. S. in Algorithm Design for Computer System
                                                                                                      Design (eds Ausiello, G. et al.) 49106 (Springer, 1984).
                                                                                               40. Lee, C. C. & Lee, D. T. A simple on-line bin-packing algorithm. J. ACM 32, 562572
                                                                                                      (1985).
                                                                                               41. Ramanan, P., Brown, D. J., Lee, C.-C. & Lee, D.-T. On-line bin packing in linear time. J.
                                                                                                      Algorithm. 10, 305326 (1989).
                                                                                               42. Seiden, S. S. On the online bin packing problem. J. ACM 49, 640671 (2002).
                                                                                               43. Balogh, J., Bksi, J., Dsa, G., Sgall, J. & Stee, R. V. The optimal absolute ratio for online
                                                                                                      bin packing. In Proc. Twenty-Sixth Annual ACM-SIAM Symposium on Discrete Algorithms,
                                                                                                      SIAM (ed. Chekuri, C.) 14251438 (SIAM, 2014).
                                                                                               44. Balogh, J., Bksi, J., Dsa, G., Epstein, L. & Levin, A. A new and improved algorithm for
                                                                                                      online bin packing. In Proc. 26th Annual European Symposium on Algorithms (ESA 2018)
                                                                                                      5:15:14 (Schloss DagstuhlLeibniz-Zentrum fuer Informatik, 2018).

474|Nature|Vol 625|18 January 2024
45. Coffman, E. G., Csirik, J., Galambos, G., Martello, S. & Vigo, D. in Handbook of               54. Jiang, A. Q. et al. THOR: wielding hammers to integrate language models and automated
       Combinatorial Optimization (eds Pardalos, P. M. et al.) 455531 (Springer, 2013).                  theorem provers. Adv. Neural Info. Process. Syst. 35, 83608373 (2022).

46. Martello, S. & Toth, P. Lower bounds and reduction procedures for the bin packing              Publisher's note Springer Nature remains neutral with regard to jurisdictional claims in
       problem. Discrete Appl. Math. 28, 5970 (1990).                                             published maps and institutional affiliations.

47. Angelopoulos, S., Kamali, S. & Shadkami, K. Online bin packing with predictions. J. Artif.                           Open Access This article is licensed under a Creative Commons Attribution
       Intell. Res. 36, 45744580 (2022).                                                                                4.0 International License, which permits use, sharing, adaptation, distribution
                                                                                                                         and reproduction in any medium or format, as long as you give appropriate
48. Chaitin, G. J. On the length of programs for computing finite binary sequences. J. ACM 13,     credit to the original author(s) and the source, provide a link to the Creative Commons licence,
       547569 (1966).                                                                             and indicate if changes were made. The images or other third party material in this article are
                                                                                                   included in the article's Creative Commons licence, unless indicated otherwise in a credit line
49. Li, M. et al. An Introduction to Kolmogorov Complexity and its Applications Vol. 3 (Springer,  to the material. If material is not included in the article's Creative Commons licence and your
       2008).                                                                                      intended use is not permitted by statutory regulation or exceeds the permitted use, you will
                                                                                                   need to obtain permission directly from the copyright holder. To view a copy of this licence,
50. Solomonoff, R. J. A formal theory of inductive inference. Part I. Inf. Control 7, 122         visit http://creativecommons.org/licenses/by/4.0/.
       (1964).
                                                                                                    The Author(s) 2023
51. O'Neill, M., Vanneschi, L., Gustafson, S. & Banzhaf, W. Open issues in genetic
       programming. Genet. Program. Evolvable Mach. 11, 339363 (2010).

52. Polu, S. & Sutskever, I. Generative language modeling for automated theorem proving.
       Preprint at https://arxiv.org/abs/2009.03393 (2020).

53. Polu, S. et al. Formal mathematics statement curriculum learning. In International
       Conference on Learning Representations (2023).

                                                                                                   Nature|Vol 625|18 January 2024|475
Article                                                                       the program's scores on each of the inputs (for example, the cap set
                                                                              size for each input n). Programs with the same signature are clustered
Methods                                                                       together. When sampling a program within an island, we first sample an
                                                                              island's cluster and then a program within that cluster (Extended Data
Implementation details of FunSearch                                           Fig. 3). This approach, which aims to preserve diversity55,56, is related
Distributed system. We implement FunSearch as a distributed system            to Lexicase57 in that both approaches consider a set of test cases for
that has three types of workers: a programs database, samplers and            scoring an individual, and it is related to fitness uniform optimiza-
evaluators. The programs database stores the initial user-provided            tion58, which also clusters individuals on the basis of their fitness value;
program, as well as all programs received from the evaluators. The sam-       however, we sample the clusters on the basis of their score instead of
plers are in charge of performing the LLM inference step; to do so they       uniformly, as detailed next.
repeatedly query the programs database for prompts. To achieve higher
sampling throughput, samplers generate several samples from each                 When sampling a cluster, we favour those with larger score values.
prompt. The samples from the LLM (that is, the generated programs)            Specifically, let si denote the score of the ith cluster, defined as an
are sent to the evaluators, which score programs by executing them on         aggregation (for example, mean) of all the scores in the signature that
inputs of interest and assessing the outputs using `evaluate'. Programs       characterizes that cluster. The probability Pi of choosing cluster i is
that are correct are sent to the programs database to be stored. Each of
the three FunSearch components is provided as both Python code and            Pi  =    exp(si /Tcluster)  ,  Tcluster =  T01  -  n  mod  N  ,  (1)
pseudocode (Supplementary Information Appendix F).                                   i exp(si /Tcluster)                              N

Prompt building. When queried for a prompt, the programs data-                where Tcluster is the temperature parameter, n is the current number of
base samples k programs to encourage the LLM to merge ideas from              programs in the island, and T0 and N are hyperparameters (given in
them (we typically set k=2; Supplementary Information Appendix E.1).          Supplementary Information Appendix E.1). This approach is sometimes
Programs are sorted according to their score in increasing order, start-      referred to as the Boltzmann selection procedure59.
ing from version 0 (`v0'). Using these k programs, the prompt is built
as explained next.                                                               When sampling a program within a cluster, we favour shorter pro-
                                                                              grams. In particular, let i denote the negative length of the ith program
   For the sake of clarity, we use here the problem specification from        within the chosen cluster (measured as the number of characters), and
Fig. 2a to precisely describe the prompting mechanism. The overall            lteoteix=p(miaiix/-Tmipiir+no1g0ir-a6m.)W, wehseertethTeprpogrroambiasbailtietymopfeeraacthurperohgypraemrpparroapmoertteior.nal
structure of the prompt mimics the structure of the program skeleton,
with the following differences: (1) the `priority' function is stripped out   Robustness. Owing to randomness in LLM sampling and in the evolu-
and replaced with the k=2 programs sampled, first `priority_v0' and           tionary procedure, repeating an experiment can lead to different
then `priority_v1'. (2) After that, a `priority_v2' function with no body     results. For some problems (for example, cap set through the admis-
is appended: the LLM will be in charge of completing the body of that         sible set problem and online bin packing) every single run of FunSearch
function. (3) All other functions that appear before `priority_v0' are        surpasses the baseline, with only some variation in the magnitude of
removed. See Extended Data Fig. 1 for an example of the structure of          the difference. For example, all experiments on admissible sets improve
a prompt.                                                                     on the previous best capacity lower bound, with 60% of experiments
                                                                              on I(12, 7)finding a full-size admissible set. For other problems, many
Evolutionary method and program selection. Another key feature                independent repetitions of an experiment may be necessary to improve
of FunSearch is the method used for evolution of the population of            on previous best results. In particular, the case of cap set by direct
programs from the programs database, as well as for program selection:        construction in n=8 dimensions is particularly challenging, with only
that is, how the programs database samples programs when queried              four out of 140 experiments discovering a cap set of size 512. See Sup-
for a prompt. For this, we use the islands model, a parallel genetic algo-    plementary Information Appendix A.3 for more details.
rithm27,28. Specifically, we split the population into m separate groups
or islands. Each island is initialized with a copy of the user-provided       Related work
initial program and is evolved separately. That is, whenever a prompt
is required, we first uniformly sample an island and then sample k=2          LLMs. The rise of powerful LLMs such as that in ref. 60 has been followed
programs from that island to build the prompt. The programs gener-            by systems in which an LLM core has been enveloped by a `program-
ated from the LLM on the basis of that prompt will later be stored in the     matic scaffold'61, and several LLM calls were connected in some way to
same island. Every 4h, we discard all the programs from the m/2 islands       accomplish larger and more intricate tasks beyond what would be pos-
whose best instances have the lowest score. Each of these islands is          sible using a single prompt and the raw LLM, possibly by using external
then seeded with a single program, obtained by first choosing one of          tools or external memory streams6266. LLMs have also been paired with
the surviving m/2 islands uniformly at random and then retrieving the         evaluators; for example, refs. 20,67 fine-tuned an LLM on data that had
highest-scoring program from that island (breaking ties in favour of          been previously generated by the LLM itself (respectively on puzzle
older programs). The evolutionary process is then restarted from this         problems and solutions, and on justifications and/or explanations for
state, in which the reset islands contain one high-performing program         answers to questions), and they used an evaluator to assess the correct-
each (Extended Data Fig. 2).                                                  ness of this data, ensuring that the fine-tuning dataset contained only
                                                                              correct solutions and/or explanations. More related to our approach
   This method has several advantages. First, drawing the analogy in          is the use of LLMs as mutation operators on code, and ref. 3 was the
which an island corresponds to an experiment, this approach effectively       first study to show that coupling an LLM with a programmatic way of
allows us to run several smaller experiments in parallel instead of a         scoring a solution can lead to a self-improvement loop. In refs. 1619,
single large experiment. This is beneficial because single experiments        the LLM was used as a crossover operator rather than a mutation one,
can get stuck in local minima, in which most programs in the popula-          that is, the LLM prompts are composed of several functions, similarly
tion are not easily mutated and combined into stronger programs.              to FunSearch. In refs. 3,16, the task was to improve code that generated
The multiple island approach allows us to bypass this and effectively         bidimensional virtual robots that could move as far as possible in a given
kill off such experiments to make space for new ones starting from            simulated terrain (ref. 16 also considered the tasks of symbolic regres-
more promising programs. Second, promising experiments are run for            sion, natural language sentences and image generation). In refs. 1719
longer, as the islands that survive a reset are the ones with higher scores.

   Within each island, we further cluster programs according to their
signature. We define the signature of a program as the tuple containing
the task was to find neural network architectures (described with Py-        scheduling as well as discovering new mathematical constructions, all
thon code), and in ref. 68 the task was continuous exploration in the        within a single pipeline without problem-specific tuning.
game of Minecraft. By contrast, in this paper, we tackle open problems
in mathematics and algorithm design, and we surpass human-designed           Program superoptimization and software engineering. Searching
constructions. We achieve that by combining several ingredients: a           for the best way of modifying source code is a task that appears in sev-
distributed system with many samplers and evaluators that commu-             eral branches of computer science and software development. These
nicate asynchronously, a user-provided program specification and             occurrences can be broadly classified into two groups: first, in which the
skeleton, as well as an evolutionary mechanism based on islands that         goal is to find semantic-preserving modifications (this arises in program
preserves the diversity of programs. FunSearch achieves that using an        optimization and superoptimization, in which the aim is to modify the
off-the-shelf LLM without fine-tuning.                                       program so that it executes faster while maintaining its inputoutput
                                                                             behaviour), and second, in which the goal is to find programs with dif-
   More broadly, LLMs have been used for program synthesis as one of         ferent semantics (this arises, for example, in automatic program repair
its main applications48. There are many use cases being explored, such      and mutation testing). With some exceptions discussed below, most of
as automatically editing code to improve performance13, automatically        these areas use relatively simple and hard-coded mutation operators
debugging code9,10, generating code from natural language descrip-           on either the source code directly (such as deleting or swapping lines)
tions6971 and doing so to solve problems in code competitions11,12. Unlike  or on the abstract syntax tree.
the above approaches that provide tools to increase the productivity
of software engineers, we combine in this paper the creativity of LLMs          Machine learning approaches have been used for program superopti-
with the power of evolutionary procedures to push the boundaries of          mization. For example, ref. 86 used reinforcement learning to learn the
human knowledge through solving open hard problems. Another line             sampling probabilities used within a hierarchical probabilistic model
of research uses LLMs to guide the search for formal proofs for auto-        of simple program edits introduced by STOKE87. Neural networks have
matic theorem proving5254. Although this approach has the potential         also been proposed as a mutation operator for program optimization
to eventually find new knowledge, the achievements of these methods          in ref. 88. These studies operated on code written in Assembly (perhaps
still lag behind the frontier of human knowledge.                            because designing meaningful and rich edit distributions on programs
                                                                             in higher-level languages is challenging). More recently, ref. 13 used
Genetic programming. Genetic programming is a subfield of com-               LLMs to find performance-improving edits to code written in C++ or
puter science concerned with automatically generating or discover-           Python. We also note that reinforcement learning has recently been
ing computer programs using evolutionary methods15,72,73 and is used         applied to discover new faster algorithms for fundamental operations
for symbolic regression applications74,75 and discovery of optimiza-         such as matrix multiplication89 and sorting90.
tion algorithms76 among others. In this broad sense, combining LLMs
with evolution can be seen as an instance of genetic programming                In this paper, we have not explicitly explored semantic-preserving
with the LLM acting as a mutation and crossover operator. However,           applications such as discovering performance-improving code edits,
using an LLM mitigates several issues in traditional genetic program-        but we believe that FunSearch could be an effective method for that
ming51, as shown in Supplementary Information Appendix A and                 setting too. In both use cases presented in the main text, the goal is to
discussed in ref. 3. Indeed, genetic programming methods require             evolve programs with new semantics, but the application is different
defining several parameters, chief among them the set of allowed             from program repair or mutation testing: in the `Extremal combinato-
mutation operations (or primitives)15. Designing such a set of opera-        rics' section, we used FunSearch to discover a program that constructs
tions is non-trivial and problem specific, requiring domain knowl-           a previously unknown mathematical object, and in the `Bin packing'
edge about the problem at hand or its plausible solution51. Although         section, we used FunSearch to discover a program that corresponds
research has been done to mitigate this limitation, through, for ex-         to a more efficient heuristic for online bin packing.
ample, the reuse of subprograms77 or modelling the distribution of
high-performing programs78, designing effective and general code             Data availability
mutation operators remains difficult. By contrast, LLMs have been
trained on vast amounts of code and as such have learned about com-          The experiments carried out in this paper do not require any data cor-
mon patterns and routines from human-designed code. The LLM can              pus other than the publicly available OR-Library bin packing bench-
leverage this, as well as the context given in the prompt, to generate       marks23. The output functions of interest produced by FunSearch are
more effective suggestions than the random ones typically used in            shown across the main paper and in text files in the Supplementary
genetic programming.                                                         Information.

   Related to genetic programming, the field of hyper-heuristics79,80        Code availability
seeks to design learning methods for generating heuristics applied to
combinatorial optimization problems. In practice, these heuristics are       The discovered functions as well as the evolutionary algorithm, code
often programs discovered through genetic programming, typically             manipulation routines and a single-threaded implementation of the
by evolving a heuristic on a set of instances of a given combinatorial       FunSearch pipeline are available as Python code in the Supplementary
optimization problem, such as bin packing81. Indeed, like FunSearch,         Information and at https://github.com/google-deepmind/funsearch.
hyper-heuristics have also been applied to online bin packing, with          Furthermore, the software library launchpad91 and a sandbox for safely
the learned heuristics able to match the performance of first fit82 and      executing generated code on our internal distributed system were used.
best fit83 on a set of generated bin packing instances. Augmenting the       No training or fine-tuning of a LLM is required; API access for inference
heuristics with memory of previously seen items can even lead to heu-        is sufficient. We used Codey26, which is available through its API, and
ristics outperforming best fit84. In addition, these evolved heuristics      StarCoder6, which is open source.
can sometimes generalize to larger instances than the ones they were
trained on85, similar to the learned FunSearch heuristics. However, as is    55. Mouret, J.-B. & Doncieux, S. Overcoming the bootstrap problem in evolutionary robotics
the case with genetic programming, one of the fundamental limitations               using behavioral diversity. In Proc. 2009 IEEE Congress on Evolutionary Computation
of hyper-heuristics is that the components of the evolved heuristic                 11611168 (IEEE, 2009).
must be manually defined by the user and often need to be tailored
to a specific problem to be effective. The LLM in FunSearch allows us        56. Pugh, J. K., Soros, L. B. & Stanley, K. O. Quality diversity: a new frontier for evolutionary
to bypass this limitation and learn heuristics for bin packing and job              computation. Front. Robotics AI 3, 40 (2016).

                                                                             57. Helmuth, T., Spector, L. & Matheson, J. Solving uncompromising problems with lexicase
                                                                                    selection. IEEE Trans. Evol. Comput. 19, 630643 (2015).
Article

58. Hutter, M. & Legg, S. Fitness uniform optimization. IEEE Trans. Evol. Comput. 10, 568589       83. Burke, E. K., Hyde, M. R., Kendall, G. & Woodward, J. Automatic heuristic generation with
       (2006).                                                                                             genetic programming: evolving a jack-of-all-trades or a master of one. In Proc. 9th Annual
                                                                                                           Conference on Genetic and Evolutionary Computation 15591565 (ACM, 2007).
59. de la Maza, M. An analysis of selection procedures with particular attention paid to
       proportional and Boltzmann selection. In Proc. Fifth International Conference on Genetic     84. Burke, E. K., Hyde, M. R. & Kendall, G. Providing a memory mechanism to enhance the
       Algorithms (Morgan Kaufmann, 1993).                                                                 evolutionary design of heuristics. In Proc. IEEE Congress on Evolutionary Computation 18
                                                                                                           (IEEE, 2010).
60. OpenAI, GPT-4 technical report. Preprint at https://arxiv.org/abs/2303.08774 (2023).
61. Millidge, B. Scaffolded LLMs as natural language computers. Beren's Blog https://www.           85. Burke, E. K., Hyde, M., Kendall, G. & Woodward, J. R. The scalability of evolved on line bin
                                                                                                           packing heuristics. In Proc. 2007 IEEE Congress on Evolutionary Computation 25302537
       beren.io/2023-04-11-Scaffolded-LLMs-natural-language-computers (2023).                              (IEEE, 2007).
62. Schick, T. et al. Toolformer: language models can teach themselves to use tools. Preprint
                                                                                                    86. Bunel, R., Desmaison, A., Kohli, P., Torr, P. H. & Kumar, M. P. Learning to superoptimize
       at https://arxiv.org/abs/2302.04761 (2023).                                                         programs. In Proc. International Conference on Learning Representations (2017).
63. Park, J. S. et al. Generative agents: interactive simulacra of human behavior. In Proc. 36th
                                                                                                    87. Schkufza, E., Sharma, R. & Aiken, A. Stochastic superoptimization. ACM SIGARCH Comp.
       Annual ACM Symposium on User Interface Software and Technology122 (ACM, 2023).                     Archit. News 41, 305316 (2013).
64. Wu, J. et al. Recursively summarizing books with human feedback. Preprint at https://
                                                                                                    88. Shypula, A. et al. Learning to superoptimize real-world programs. In Proc. Deep Learning
       arxiv.org/abs/2109.10862 (2021).                                                                    for Code Workshop (ICLR 2022 Workshop) (2022).
65. Nye, M. et al. Show your work: scratchpads for intermediate computation with language
                                                                                                    89. Fawzi, A. et al. Discovering faster matrix multiplication algorithms with reinforcement
       models. In Deep Learning for Code Workshop, International Conference on Learning                    learning. Nature 610, 4753 (2022).
       Representations (2022).
66. Yao, S. et al. ReAct: dynergizing reasoning and acting in language models. In Proc.             90. Mankowitz, D. J. et al. Faster sorting algorithms discovered using deep reinforcement
       International Conference on Learning Representations (2023).                                        learning. Nature 618, 257263 (2023).
67. Zelikman, E., Wu, Y., Mu, J. & Goodman, N. Star: bootstrapping reasoning with reasoning.
       Adv. Neural Info. Process. Syst. 35, 1547615488 (2022).                                     91. Yang, F. et al. Launchpad: a programming model for distributed machine learning
68. Wang, G. et al. Voyager: an open-ended embodied agent with large language models.                      research. Preprint at https://arxiv.org/abs/2106.04516 (2021).
       Preprint at https://arxiv.org/abs/2305.16291 (2023).
69. Yin, P. et al. Natural language to code generation in interactive data science notebooks.       Acknowledgements We thank R. Anil, V. Feinberg, E. Taropa, T. Hubert, J. Schrittwieser and
       Preprint at https://arxiv.org/abs/2212.09248 (2022).                                         S. Nowozin for their LLM support; T. Schaul, C. Fernando, A. Barreto and P. Gupta for
70. Ni, A. et al. Lever: learning to verify language-to-code generation with execution. In Proc.    discussions on evolutionary algorithms; M. Figurnov and T. Cemgil for reviewing the paper;
       International Conference on Machine Learning 2610626128 (PMLR, 2023).                       F. Piccinini and S. Kenjeyev for their support on job scheduling; S. Blackwell for technical
71. Zhou, S., Alon, U., Xu, F. F., Jiang, Z. & Neubig, G. Docprompting: generating code by          support; O. Ronneberger, F. Gimeno, B. Huergo, A. Mehrabian and A. Anand for useful advice
       retrieving the docs. In Proc. International Conference on Learning Representations           and G. Holland for program management support.
       (2022).
72. Banzhaf, W., Nordin, P., Keller, R. E. & Francone, F. D. Genetic Programming: An                Author contributions B.R.-P. conceived the project with help from A.F. and P.K. A.F. scoped
       Introduction: On The Automatic Evolution of Computer Programs and its Applications           problems and developed project vision. B.R.-P. and A.N. developed the initial FunSearch
       (Morgan Kaufmann, 1998).                                                                     codebase. A.N., B.R.-P., M. Balog, F.J.R.R., M. Barekatain, E.D. and A.F. implemented and refined
73. Langdon, W. B. & Poli, R. Foundations of Genetic Programming (Springer Science &                the different components of the system. M. Barekatain and A.N. imported and experimented
       Business Media, 2013).                                                                       with LLMs. M. Barekatain, A.N. and M. Balog worked on evaluating, debugging and improving
74. Ma, H., Narayanaswamy, A., Riley, P. & Li, L. Evolving symbolic density functionals. Sci.       the efficiency of experiments. M. Balog, M. Barekatain, B.R.-P., A.N., A.F., O.F. and J.S.E.
       Adv. 8, eabq0279 (2022).                                                                     contributed to the cap set problem. M.P.K., M. Balog and J.S.E. researched and analysed results
75. Schmidt, M. & Lipson, H. Distilling free-form natural laws from experimental data. Science      from the admissible sets problem. E.D., M. Barekatain and P.W. contributed to the online bin
       324, 8185 (2009).                                                                           packing problem. F.J.R.R. and O.F. researched and did experiments on other problems
76. Chen, X. et al. Symbolic discovery of optimization algorithms. Preprint at https://arxiv.       (Shannon capacity and corners problems), P.K. contributed technical advice and ideas.
       org/abs/2302.06675 (2023).                                                                   A.F., B.R.-P., E.D., F.J.R.R., M.P.K., M. Balog, A.N., J.S.E. and M. Barekatain wrote the paper.
77. Koza, J. R. Genetic Programming II: Automatic Discovery of Reusable Programs (MIT, 1994).
78. Salustowicz, R. & Schmidhuber, J. Probabilistic incremental program evolution. Evol.            Competing interests The authors of the paper are planning to file a patent application relating
       Comput. 5, 123141 (1997).                                                                   to subject matter contained in this paper in the name of Google DeepMind.
79. Burke, E. et al. in Handbook of Metaheuristics (eds Glover, F. & Kochenberger, G. A.)
       457474 (Springer, 2003).                                                                    Additional information
80. Ross, P. in Search Methodologies: Introductory Tutorials in Optimization and Decision           Supplementary information The online version contains supplementary material available at
       Support Techniques (eds Burke, E. K. & Kendall, G.) 529556 (Springer, 2005).                https://doi.org/10.1038/s41586-023-06924-6.
81. Burke, E. K. et al. Hyper-heuristics: a survey of the state of the art. J. Oper. Res. Soc. 64,  Correspondence and requests for materials should be addressed to Bernardino
       16951724 (2013).                                                                            Romera-Paredes, Pushmeet Kohli or Alhussein Fawzi.
82. Burke, E. K., Hyde, M. R. & Kendall, G. Evolving bin packing heuristics with genetic            Peer review information Nature thanks Josh Grochow, Andrea Lodi, Jean-Baptiste Mouret,
       programming. In Proc. International Conference on Parallel Problem Solving from Nature       Talia Ringer and Tao Yu for their contribution to the peer review of this work.
       860869 (Springer, 2006).                                                                    Reprints and permissions information is available at http://www.nature.com/reprints.
Extended Data Fig. 1 | Example of best-shot prompting, based on the skeleton from Fig. 2a. The prompt includes k=2 implementations sampled from the
programs database, with higher-scoring implementations being more likely to be included.
Article

Extended Data Fig. 2 | Evolutionary method. The initial programs are              from the islands with the best score are placed in the empty islands. Evolution
separated into islands and each of them is evolved separately. After a number of  then proceeds separately again until the next reset. This process is repeated
iterations, the islands with the worst score are wiped and the best program       until termination.
Extended Data Fig. 3 | Program clusters within islands. Within each island,      programs. The sampled programs are used to prompt the LLM which generates
programs are grouped into clusters based on their signature (i.e., their scores  a new program. If the new program is correct, it is added to the island, either in
on several inputs). We first sample clusters, favoring the ones with higher      an existing cluster or a new one if its signature was not yet present.
score. Within the chosen clusters, we sample a program, favoring shorter
