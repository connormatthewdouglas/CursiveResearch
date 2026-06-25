# Open-Endedness is Essential for Artificial Superhuman Intelligence — Full Text

**Authors:** Edward Hughes; Michael Dennis; Jack Parker-Holder; Feryal Behbahani; Aditi Mavalankar; Yuge Shi; Tom Schaul; Tim Rocktäschel
**arXiv:** 2406.04268v1
**Source:** https://arxiv.org/abs/2406.04268
**PDF:** https://arxiv.org/pdf/2406.04268
**License:** CC BY 4.0 (http://creativecommons.org/licenses/by/4.0/)
**Rights Status:** full-text allowed for corpus storage and redistribution with attribution under CC BY 4.0.
**Retrieved:** 2026-06-25
**Extraction Method:** `pdftotext -layout -enc UTF-8` from the arXiv PDF.

> Corpus note: this is a full text extraction from the rights-cleared arXiv PDF.
> PDF-to-text conversion may distort equations, tables, ligatures, and page headers;
> use `paper.pdf` as the formatting-canonical source and this `paper.md` for
> agent-readable corpus ingestion.

---

Open-Endedness is Essential for Artificial Superhuman Intelligence

                                       Edward Hughes * 1 Michael Dennis * 1 Jack Parker-Holder 1 Feryal Behbahani 1 Aditi Mavalankar 1 Yuge Shi 1
                                                                                           Tom Schaul 1 Tim Rockta¨schel 1

arXiv:2406.04268v1 [cs.LG] 6 Jun 2024                          Abstract                                   explosion of emergent capabilities, behaviors, and artifacts.
                                                                                                          This kind of open-ended invention is the mechanism by
                                             In recent years there has been a tremendous surge            which human individuals and society at large accumulates
                                             in the general capabilities of AI systems, mainly            new knowledge and technology. Therefore, open-endedness
                                             fuelled by training foundation models on internet-           must be a property of an artificial superhuman intelligence
                                             scale data. Nevertheless, the creation of open-              (ASI, Morris et al., 2023) that can, by definition, accomplish
                                             ended, ever self-improving AI remains elusive.               a wide range of tasks at a level which no human can match.
                                             In this position paper, we argue that the in-                By the very nature of superhuman intelligence, open-ended
                                             gredients are now in place to achieve open-                  discovery of innovative solutions is essential to empower hu-
                                             endedness in AI systems with respect to a hu-                manity to manage its risks, just as society evolves norms and
                                             man observer. Furthermore, we claim that                     institutions to govern increasingly capable humans across
                                             such open-endedness is an essential property                 generations (Richerson et al., 2001).
                                             of any artificial superhuman intelligence (ASI).
                                             We begin by providing a concrete formal defini-              Foundation models such as large language models (LLMs)
                                             tion of open-endedness through the lens of novelty           have scaled learning to large, static datasets scraped from
                                             and learnability. We then illustrate a path towards          the internet. Extrapolating, we may soon be running out
                                             ASI via open-ended systems built on top of foun-             of high-quality textual and visual data for training such
                                             dation models, capable of making novel, human-               models (Villalobos et al., 2022). Thus, open-endedness is
                                             relevant discoveries. We conclude by examining               unlikely to arise for free by training on ever-larger datasets.
                                             the safety implications of generally-capable open-           Rather, a system endowed with the open-endedness neces-
                                             ended AI. We expect that open-ended foundation               sary for ASI will eventually have to create, refute and refine
                                             models will prove to be an increasingly fertile and          its own explanatory knowledge, in interaction with a source
                                             safety-critical area of research in the near future.         of evidence (Deutsch, 2011), as well as learning what data to
                                                                                                          learn from (Jiang et al., 2022). Moreover, for ASI to be use-
                                       1. Introduction                                                    ful and safe, it is important that open-endedness be guided
                                                                                                          towards knowledge that is understandable by and beneficial
                                       Recent years have seen impressive progress in AI, mainly           for humanity. Foundation models and open-endedness are
                                       driven by foundation models (Bommasani et al., 2021).              orthogonal dimensions, whose combination is particularly
                                       These models are increasingly used as agents in various            powerful (cf. Lehman et al., 2022; Huang et al., 2022; Chen
                                       applications (e.g., Wang et al., 2023a; Wu et al., 2023;           et al., 2023a; Meyerson et al., 2023; Zhang et al., 2023; Wu
                                       Lifshitz et al., 2023; Wang et al., 2023c; Liu et al., 2023b;      et al., 2023; Wang et al., 2023a). Open-ended algorithms
                                       Zheng et al., 2024; Ahn et al., 2022). This represents signif-     endow foundation models with the ability to uncover new
                                       icant progress towards artificial general intelligence (AGI),      knowledge, while foundation models guide the search space
                                       in the sense of reaching human-level performance on a wide         for open-ended AI towards discovering human-relevant arti-
                                       range of tasks (Legg and Hutter, 2007). However, we are            facts efficiently (Liu et al., 2023a; Ma et al., 2023; Romera-
                                       still missing a formal description of what it would take for       Paredes et al., 2024). A formal definition of open-endedness
                                       an autonomous system to self-improve towards increasingly          can catalyze progress in this direction, offering clarity and
                                       creative and diverse discoveries without end—a Cambrian            focus to galvanize the research community.

                                          *Equal contribution 1Google DeepMind, London, UK. Corre-        We provide a new and precise definition of open-endedness
                                       spondence to: Edward Hughes <edwardhughes@google.com>,             in Section 2, inspired by the open-ended systems in nature
                                       Michael Dennis <dennismi@google.com>.                              that have created life, the human brain, culture, and tech-
                                                                                                          nology, as well as open-ended systems in silico that, for
                                       Proceedings of the 41 st International Conference on Machine       instance, have achieved superhuman level at the game of
                                       Learning, Vienna, Austria. PMLR 235, 2024. Copyright 2024 by       Go (Silver et al., 2016), generated human-level adaptation
                                       the author(s).

                                                                                                       1


--- page break ---

Open-Endedness is Essential for Artificial Superhuman Intelligence

to novel 3D tasks (Bauer et al., 2023), self-improved lan-                   SYSTEM
guage models (Fernando et al., 2023; Yang et al., 2023a),
unlocked the tech tree in Minecraft (Wang et al., 2023a),         ARTIFACTS  …       …  …
and discovered new results in pure mathematics (Romera-
Paredes et al., 2024). Open-endedness has been understood                  OBSERVER
in a wide variety of ways (Earle et al., 2021) ever since
it gained prominence as a term in the study of artificial                      Novelty
life (Bedau, 1992; Bedau et al., 1998) and biological evo-
lution (Holland, 1992; McShea, 1996; Waddington, 2008).                     Learnability
Contrary to Stepney and Hickinbotham (2023), we believe
quantifying open-endedness is both possible and important         Figure 1. Illustration of open-endedness definition. The defini-
going forward, and, akin to Sigaud et al. (2023), we be-          tion of open-endedness hinges on a system’s ability to continuously
lieve it can be achieved via the help of an observer external     generate artifacts that are both novel and learnable to an observer.
to the system. Our definition makes formal the aphorism           Consider a system that designs various aircraft: a mouse (left)
of Lisa B. Soros that, as observers of an open-ended sys-         might find these designs novel but lack the capacity to comprehend
tem, “we’ll be surprised but we’ll be surprised in a way that     the principles behind them; for a human studying aerospace engi-
makes sense in retrospect”. Concretely, open-ended systems        neering (middle), the system offers both novelty and the potential
produce increasingly novel and surprising artifacts that are      for learning, making it open-ended. However, a superintelligent
hard to predict, even for an observer who has learned to          alien (right) with vast aerospace knowledge might not find the
better predict by examining past artifacts. Once a system         design novel, but would still be able to analyze and understand
exhibits these characteristics, i.e. producing learnable but      them. This highlights that open-endedness is observer-dependent
novel artifacts, we call it an open-ended system. This allows     and that novelty or learnability alone is not enough.
us to pinpoint the sense in which open-endedness is essen-
tial for ASI, to provide examples illustrating how existing       et al., 2020). In Section 4, we argue that research into open-
open-ended AI systems lack generality, and to argue that          ended systems will be essential to safely and beneficially
present-day foundation models are not yet open-ended.             deploy any increasingly general and autonomous AI.

Historically, the field of open-endedness has faced numer-        2. Defining Open-Endedness
ous challenges. Principal among these has been the problem
of structuring the search space so as to regularly produce        2.1. Formal Definition
artifacts which are both novel and interesting to humans (Ma
et al., 2023). When humans make discoveries, they do so by        The notion of an open-ended system has received many
“standing on the shoulders of giant human datasets” (Clune,       colloquial definitions (Soros and Stanley, 2014; Stanley
2022); that is to say, utilising prior world, domain and com-     and Lehman, 2015; Stanley et al., 2017; Stanley, 2019).
monsense knowledge, which they have acquired biologically         More formal approaches have often focused on the case
or culturally. Since foundation models have been trained on       of evolutionary systems, quantifying the increasing com-
vast amounts of human data, they capture human notions of         plexity (McShea, 1996; Waddington, 2008) and perpetual
interestingness (Zhang et al., 2023). Furthermore, they are       novelty (Holland, 1992) of biological evolution. Intuitively,
general sequence modellers (Mirchandani et al., 2023) and         an open-ended system endlessly produces novel and interest-
can generate variations from existing examples (Meyerson          ing artifacts. But novelty and interestingness have generally
et al., 2023), thus serving as general mutation operators.        been characterised without sufficient precision, or in an
This is compelling since with more advanced foundation            overly narrow way. We provide a general-purpose, formal
models, practical implementations of open-ended systems           definition of open-endedness, as follows.
become increasingly feasible. Taken together, open-ended
foundation models can both vary (i.e., mutate) data and as-          Definition: From the perspective of an observer, a
sess novelty and interestingness of real and generated data          system is open-ended if and only if the sequence of
to decide what data to further explore (i.e., select) (Jiang         artifacts it produces is both novel and learnable.
et al., 2022).
                                                                  More formally, a system S produces a sequence of artifacts
In Section 3 we provide some concrete research directions         Xt, indexed by time t. An observer O processes a new arti-
for this marriage between open-endedness and foundation           fact XT to determine its predictability given a history X1:t
models, for example leveraging evolutionary algorithms
and reinforcement learning. Generally capable open-ended
systems may be both extremely powerful and increasingly
prevalent, prompting pressing safety considerations (Ecoffet

                                                               2


--- page break ---

Open-Endedness is Essential for Artificial Superhuman Intelligence

of past ones. O possesses a statistical model Xˆt which pre-              for proving whether a system is open-ended. On a practi-
dicts an arbitrary future artifact based on its observations of           cal note, it raises the prospect of searching for open-ended
the artifacts it has seen up to time t. The observer judges the           systems. In this paper, we shall use it to underpin the argu-
quality of their prediction based on a loss metric ℓ(Xˆt, XT ),           ment that open-endedness lies on the critical path towards
or ℓ(t, T ) for short. A natural implementation of Xˆt is as a            ASI, and in particular that the combination of open-ended
learning algorithm.                                                       algorithms and foundation models is ripe to yield significant
                                                                          progress towards that aim. We examine some subtleties of
A system displays novelty if artifacts become increasingly                our definition in Appendix A.2.
unpredictable with respect to the observer’s model at any
fixed time t, namely:                                                     2.2. Related Definitions

      ∀t, ∀T > t, ∃T ′ > T : E [ℓ(t, T ′)] > E [ℓ(t, T )] .               In the interests of space, we review the definitions of open-
                                                                          endedness most closely related to ours, covering more dis-
In other words, there is always a less predictable artifact               tantly related work in Appendix C. Soros and Stanley (2014)
coming further in the future.1                                            provided four necessary conditions for an evolutionary pro-
                                                                          cess to be open-ended, namely (1) that individuals must
The system is learnable whenever conditioning on a longer                 meet a minimal criterion in order to reproduce, (2) that
history makes artifacts more predictable, namely:                         evolution of individuals should create novel opportunities
                                                                          to meet the minimal criterion, (3) that individuals them-
   ∀T, ∀t < T, ∀T > t′ > t : E [ℓ(t′, T )] < E [ℓ(t, T )] .               selves should make decisions about how to interact with the
                                                                          world, and (4) that the potential complexity of the phenotype
Finally, a system is open-ended from the perspective of the               should not be limited by its representation. Our definition
observer O if and only if it generates sequences of artifacts             overlaps with these necessary conditions, but relaxes the
that are both novel and learnable (see Figure 1). The novelty             constraint that the open-ended system is evolutionary. Our
aspect ensures the presence of information gain within the                requirement that learnability is increasing can be seen as
system, while learnability guarantees that this information               a generalisation of the minimal criterion in condition (1).
gain holds meaning and is “interesting” to the observer.                  Our requirement that the observer cannot intervene on the
                                                                          system is analogous to condition (3). Our requirement that
For example, imagine that the system is a noisy TV pro-                   novelty is increasing is analogous to conditions (2) and (4).
ducing uniform random noise (Burda et al., 2018). A noisy                 Indeed, conditions (2) and (4) suggest that an open-ended
TV is learnable, allowing the observer to learn a statistical             system cannot be learned from a fixed data distribution.
model that approximates the uniform distribution increas-
ingly well; however, once the observer’s model converges                  To our knowledge, the most recent paper offering a defini-
to uniform the system loses its novelty: all that is left is              tion of open-endedness is Sigaud et al. (2023). The authors
aleatoric uncertainty, which is collapsed by the expectation.             write: “an observer considers a process as open-ended if, for
Now imagine that the system is a noisy TV switched period-                any time t, there exists a time t′ > t at which the process
ically by a remote control to a random, arbitrary distribution.           generates a token that is new according to this observer’s
Every time the channel is changed, the observer may expe-                 perspective”. This definition has considerable overlap with
rience novelty; however, the system is now not learnable,                 ours. Like us, Sigaud et al. define open-endedness with re-
because the history of artifacts (previous TV channels) are               spect to an observer. They consider the observer examining
not correlated with the distribution of the next channel, so              a sequence of tokens from a process, while we equivalently
the model loss will not decrease in general. We provide an                have the observer consider a sequence of artifacts from a
informal positive example in Appendix A.1.                                system. Our requirement of novelty and learnability is com-
                                                                          patible with their statement that the process should generate
Our definition makes no explicit mention of “interesting-                 a token that is “new according to the observer’s perspec-
ness”. More precisely, interestingness is represented in our              tive”. Our definition differs by being more precise about
definition by the observer’s choice of loss function ℓ. Thus,             what this phrase means. In particular, we specify that what
for us, the interesting parts of artifacts are precisely those            an observer considers “new” should be artifacts that are
features which the observer decides are useful to learn about.            unpredictable according to their current statistical model of
Different observers can, and do, find different artifacts inter-          the system under consideration. Moreover, we specify that
esting, by virtue of the different parts of the feature space             the observer’s “perspective” is generated by learning that
they choose to learn with their statistical model.                        statistical model on the history of artifacts thus far presented
                                                                          by the system. In particular, our definition can rule out
We hope that our definition will serve as a useful grounding              systems that display continual “novelty” but are otherwise
for future work. On the theoretical side, it provides a basis             uninteresting, like white noise on a TV screen, for instance.

    1We take the expectation over any stochasticity in the artefacts;
practically speaking, were the observer to make observations from
identical copies of the system S, the expectation of ℓ would be
approximated by the empirical mean.

                                                                       3


--- page break ---

Open-Endedness is Essential for Artificial Superhuman Intelligence

2.3. Types of Observer                                                   other topics that may crop up later. However, once human
                                                                         memory capacity is saturated, the human observer will start
The choice of observer is a free parameter of great impor-               to forget previous articles. This violates learnability: in
tance for our definition. From the perspective of AI research,           calculus, for instance, once one has forgotten the definition
there is a pre-eminent class of observers, namely humans.                of a derivative, one will find it harder to understand an article
In other words, we wish to generate artifacts that are valu-             about the chain rule. Therefore, conditioning on a history
able to individual humans and to society. This provides a                longer than an observer’s recall doesn’t necessarily make
level of grounding for the open-ended system which nar-                  the current artifact more predictable.
rows the search space considerably, as we shall argue in
Section 3. Nevertheless, our definition deliberately admits              This example brings to light three interesting threads. Firstly,
arbitrary observers, for several reasons. Firstly, it allows our         the open-endedness of human technology, as observed by
definition to encompass open-ended systems which are not                 humans, relies on our ability to compress knowledge into
anthropocentric, such as biological evolution. Secondly, it              a form that can be maintained within our collective mem-
allows us to reason about open-ended systems which might                 ory: indeed, we present an alternative definition of open-
exceed human capabilities, so-called ASI. Thirdly, it allows             endedness in the language of compression in Appendix B.
us to determine whether systems can be open-ended with                   Secondly, an artificial superhuman intelligence may have
respect to any observer, as we did with the noisy TV.2                   less stringent memory constraints than humans, and there-
                                                                         fore may judge itself to be open-ended beyond the point at
Practically speaking, any given observer will have some                  which humans assess it to be so, re-emphasising that human
time horizon τ which bounds their observations of a system,              observers must be considered pre-eminent for the purposes
i.e. t, T < τ . This concept allows us to distinguish between            of safety, as we explore further in Section 4. Thirdly, the
systems which are open-ended on different timescales. We                 open-endedness in this example is a function of the breadth
say that a system is infinitely open-ended with respect to               of the domain. In a narrower domain, elliptic curve cryp-
an observer O if it remains open-ended on any timescale                  tography say, the set of relevant Wikipedia articles would
τ → ∞. We say that a system is finitely open-ended with                  be much smaller, so a human observer would find this open-
time horizon τ with respect to an observer O if it is open-              ended only until they had understood every article, at which
ended for t, T < τ . Consider, for example, an agent trained             point novelty would be violated. Nevertheless, humans can,
in simulation with an automatic curriculum over tasks. In                and frequently do, make new discoveries in narrow domains
principle, a human observer might find observations of the               via experimentation and reasoning; amassing a vast, static
agent behaviour to be infinitely open-ended, for the agent               trove of data is not the be all and end all of open-endedness.
may accrue the ability to solve ever more diverse and sur-
prising tasks. In practice (cf. AdA, Bauer et al., 2023),                2.4. Examples
novelty starts to plateau after about 1 month of training, due
to limitations in the richness of the task space and in the              In this section, we discuss some popular systems that are
size of the agent’s neural network. Thus AdA is finitely                 open-ended but not general, or that are general but not open-
open-ended with time horizon ≈ 1 month.                                  ended, with respect to a human observer. This serves two
                                                                         purposes. Firstly, it demonstrates that our definition is not
Similarly, an observer’s judgement will be influenced by                 so restrictive as to rule out systems that are intuitively open-
the limitations of their cognitive abilities relative to the             ended, and is not so loose as to include systems that intu-
breadth of the domain. For example, a human observer who                 itively lack open-endedness. Secondly, it motivates the ben-
reads a curriculum of ever more complex articles from a                  efits that foundation models can provide in addressing the
current snapshot of Wikipedia may find such a system open-               limitations of current open-ended systems and vice versa.
ended, but only until they reach the limit of their memory.
A suitable ordering of Wikipedia articles will present novel             Our first archetypal open-ended system is AlphaGo (Silver
information, in the sense that every now and then an article             et al., 2016). Consider as artifacts the sequence of policies
will be more unpredictable than we have hitherto seen. We                produced across training by AlphaGo. After sufficient train-
might also expect that this information will be learnable,               ing, AlphaGo produces policies which are novel to human
because human knowledge is interlinked, in the sense that                expert players, in the sense that they play moves which
knowing more about one topic makes it easier to understand               would be low probability for human professionals but which
                                                                         nevertheless are winning against the best humans. Further-
    2There is one constraint on an observer which must be adhered        more, humans can improve their win rate against AlphaGo
to for our definition to make sense. The loss function must treat        by learning from AlphaGo’s behavior (Shin et al., 2023).
artifacts X and predictions Xˆ on an equal footing. In particular it     Yet, AlphaGo keeps discovering new policies that can beat
must be fixed in advance without any knowledge of the system S.          even a human who has learned from previous AlphaGo ar-
Otherwise, an observer O could find a system S to be open-ended          tifacts. Thus, so far as a human is concerned, AlphaGo is
purely by discarding the artifacts from S and constructing its own
artifacts that it finds to be both novel and learnable.

                                                                      4


--- page break ---

Open-Endedness is Essential for Artificial Superhuman Intelligence

both novel and learnable. AlphaGo is just one representative          et al., 2019; 2020). POET trains a population of agents,
from a class of open-ended algorithms that augment rein-              each of which is paired with an environment that is evolving
forcement learning with self-play (Samuel, 1959), achieving           over the course of training. These paired agent-environment
or exceeding human-level play in Go, Chess, Shogi (Silver             artifacts are open-ended with respect to a human observer
et al., 2017), StarCraft II (Vinyals et al., 2019) Stratego (Per-     seeking to model the features of the environments that arise,
olat et al., 2022), DotA (Berner et al., 2019), and Diplomacy         or equivalently the skills the paired agents possess. A Qual-
(Bakhtin et al., 2022).                                               ity Diversity algorithm (QD, Pugh et al., 2016; Mouret and
                                                                      Clune, 2015) is deployed with respect to the environments,
AlphaGo is an example of an open-ended system that                    hunting for challenging problems that lead to diverging per-
achieves narrow superhuman intelligence (Morris et al.,               formance across the population. QD is an example of a
2023). This limits its utility: self-play of this kind can-           wider class of open-ended algorithms, namely evolutionary
not by itself help us to discover new science or technology           algorithms, which we encounter again in Section 3.4.
that requires combining insight from disparate fields, or
taking actions across a range of modalities, timescales and           Crucially, POET periodically transfers agents from one en-
contexts. The constraints of the game rules make the search           vironment to another, which results in an empirical example
for novel and learnable artifacts tractable, and these artifacts      of the stepping stone phenomenon (Stanley and Lehman,
are found to be novel and learnable by human observers                2015): agents can eventually solve incredibly challenging
largely because it was humans who invented the game.                  environments that are not possible to solve with direct opti-
                                                                      mization. As a result of training for billions of environment
Our second archetypal open-ended system is AdA (Bauer                 steps, POET produces a diverse population of highly capa-
et al., 2023; OEL Team et al., 2021). AdA is a large-scale            ble specialist agents, which can solve novel environments
agent that learns to solve tasks in an 3D-environment called          that are created through coevolution with the population
XLand2. In XLand2 there are 25B possible task variants,               (Brant and Stanley, 2017). Novelty arises because of the
corresponding to different world topologies and a variety of          mutation operator in the QD algorithm, which yields new
possible games within each world, that are prioritized for            and unpredictable environments. Learnability arises because
learning potential (Jiang et al., 2021). Checkpoints of the           each mutation is small, so the past lineage of an environ-
AdA agent across training are open-ended with respect to a            ment is a good guide to its current features. Just as for AdA,
human observer who attempts to predict what capabilities              the key limitation on open-endedness is the environment
the agent might show. Across training, the agent gradu-               parameterization itself: eventually POET will plateau once
ally accumulates zero-shot and few-shot capabilities over             the agent can solve all possible terrains.
an ever wider set of held-out environments, requiring ever
more complex skills. Thus the human continually observes              Our final example is contemporary foundation models.
novel capabilities in the agent. Furthermore, the prioritiza-         These are a negative example; they are not open-ended by
tion of task variants provides an interpretable ordering to the       our definition with respect to any observer who can model
accumulation of skills in the agent, rendering this learnable         their training dataset. The justification for this follows im-
by a human. AdA represents a wider class of open-ended al-            mediately from our consideration of the noisy TV in Section
gorithms driven by unsupervised environment design (UED,              2.1. Contemporary foundation models are typically trained
Dennis et al., 2020; Justesen et al., 2018), which establish          on fixed datasets. If the distribution of this data is learnable,
an automatic curriculum (Leibo et al., 2019; Baker et al.,            which it must be, for the foundation model learned it in
2020) of environments in the zone of proximal development             the first place, then it cannot be endlessly novel, because
for agent learning (Vygotsky and Cole, 1978).                         eventually the observer will have modelled the epistemic
                                                                      uncertainty. As we saw in Section 2.3, foundation models
It is natural to ask whether AdA would continue to be judged          may appear open-ended to human observers if the domain of
as open-ended by a human observer should training be con-             enquiry is sufficiently broad, by virtue of the memory limita-
tinued indefinitely. Results in Bauer et al. (2023) suggest           tions of the human brain. However, if the focus is narrowed,
that novelty starts to plateau, implying that with an order           for instance to tasks that require planning (Momennejad
of magnitude more compute AdA would almost certainly                  et al., 2024; Pallagani et al., 2023; Valmeekam et al., 2023),
not be open-ended. Indeed, the authors show that both in-             the limitations of the foundation model in generating novel,
creasing the size of the agent and increasing the number              correct solutions are exposed.
of tasks allow the agent to generalize to a wider range of
environments. Thus, in order for this system to be open-              Since foundation models are periodically retrained on new
ended on longer timescales, one would need an even richer             data, including data generated by their own interactions
environment and an even more capable agent to sustain the             with humans and the real world, one could argue that the
agent-environment co-evolution inherent in UED.                       data distribution is not really fixed. In some quarters, this
                                                                      kind of distributional shift is seen as an annoyance, even
Our third archetypal open-ended system is POET (Wang

                                                                   5


--- page break ---

Open-Endedness is Essential for Artificial Superhuman Intelligence

one which threatens “model collapse” (Shumailov et al.,            on a source of evidence, and codifying the results into new
2023). We flip this argument on its head, and contend              knowledge has yielded unprecedented progress in science
that augmenting foundation models with open-endedness              and technology (Deutsch, 2011). In our view, the fastest
offers a path towards ASI. Similarly, the fact that foundation     path to ASI will take inspiration from the scientific method,
models are typically conditional on context breaks the logic       compiling a dataset online by the explicit combination of
that they cannot be open-ended. In principle, the context of a     foundation models and open-ended algorithms.
foundation model can be recruited to recombine concepts in
an open-ended way by leveraging some external measure of           3.1. Reinforcement Learning
validity. This brings us neatly to some concrete suggestions
for how to build open-ended foundation models.                     The framework of Reinforcement Learning (RL) has been at
                                                                   the forefront of achieving superhuman performance in nar-
3. Open-Ended Foundation Models                                    row domains, such as AlphaGo’s groundbreaking strategies
                                                                   that have enriched the human understanding of the game of
We have defined open-endedness and discussed why the               Go. RL agents act deliberately so as to shape their stream of
current foundation model training paradigm is not open-            experience for both accumulating reward (exploitation) and
ended. We believe that the trend of improving foundation           learning about how to increase expected reward in the future
models trained on passive data by scaling alone will soon          (exploration). A nuanced extension are agents that set their
plateau, and it will not be enough to reach ASI. Our position      own goals to (learn to) pursue; and generating the sequence
is that open-endedness is a property of any ASI, and that          of these goals can itself be an open-ended process, which
foundation models provide the missing ingredient required          drives open-ended experience generation (Colas et al., 2022).
for domain-general open-endedness. Further, we believe             Voyager (Wang et al., 2023a) provides an early example of
that there may be only a few remaining steps required to           how RL-like self-improvement can be built on top of founda-
achieve open-endedness with foundation models. In the              tion models, without the need for explicit parameter updates
following subsections, we sketch four overlapping paths            or established RL algorithms. Instead, Voyager assembles
towards open-ended foundation models that lend credence to         an LLM-powered curriculum, uses iterative prompting as
this belief. The paths are neither intended to be prescriptive     an improvement operator, and assembles verified skills into
nor exhaustive. Indeed, recent publications such as (Wong          a library for hierarchical reuse.
et al., 2023b; Sharma et al., 2023) point to other paths.
                                                                   A key problem in RL is how to shape exploration towards
Before proceeding, we must justify our claim that a future         novel and learnable behaviors in high-dimensional domains,
foundation model trained passively on some large corpus            as discussed in Jiang et al. (2022). Exploration can be
of human data is unlikely to spontaneously acquire open-           guided, for instance, by pseudo-rewards (Bellemare et al.,
endedness. In principle, should we reach ASI, there will           2016; Burda et al., 2018; Du et al., 2023b), modulation
be some sum total of data which the model has consumed             (Schaul et al., 2019) or an automated curriculum that selects
during its training, possibly via several intermediate stages.     relevant tasks (Jiang et al., 2021; Parker-Holder et al., 2022;
Therefore, our claim is not about the impossibility of assem-      Samvelyan et al., 2023). To generalize this, a useful abstrac-
bling such a dataset. Rather, we suggest that it is unlikely       tion may be the notion of a proxy observer, which sits within
that this dataset can be pre-collected offline in an efficient     the system and proactively guides it to generate novel and
way. The reason is that open-endedness is fundamentally an         learnable content for the true external observer. In the past
experiential process: producing novelty and learnability in        this guidance was provided on the basis of simple metrics
the eyes of an observer requires continual online adaptation       such as TD-error, but now we can leverage foundation mod-
on the basis of the artifacts already produced, in the context     els to guide exploration towards artifacts that more closely
of that observer’s evolving prior beliefs.                         align with what a human observer deems to be novel and
                                                                   interesting (Jiang et al., 2022). There is already evidence
What would it take to collect offline a static dataset from        that this approach may be effective, with LLMs providing
which such an experiential skill could be learned? Such            agent rewards from text in an environment (Klissarov et al.,
a dataset must contain a treasure trove of artifacts which         2023) and compiling a curriculum of tasks based on their
themselves crisply show novelty and learnability. Yet the          interestingness (Zhang et al., 2023; Faldor et al., 2024).
process by which culture evolves, ideas develop, inventions
arise and technologies proliferate is seldom recorded neatly       While RL considers the first-person perspective of an agent
and comprehensively. The alternative paradigm, in which            interacting with an environment, a different perspective cen-
experience is “built in” to the open-ended system, is well il-     ters on multi-agent dynamics, and the additional richness
lustrated by the scientific method. Since the Enlightenment,       arising from all the ways that different (possibly heteroge-
the simple process of making hypotheses on the basis of            neous) agents can interact with each other, adapt to each
current knowledge, falsifying them with experiments based          other, or learn from each other. The presence of multiple

                                                                6


--- page break ---

Open-Endedness is Essential for Artificial Superhuman Intelligence

learning agents provides a source of non-stationarity, such         Another possibility is to instead learn world models—
that the optimal strategy for each individual will change over      predictive simulators that can generate future outputs condi-
time, potentially in an open-ended manner. Non-stationary           tioned on text or actions. A promising approach is to con-
dynamics been used to achieve or exceed human-level per-            sider a foundation model to be a world model itself, since
formance in games like StarCraft, DotA and Stratego. There          it is capable of predicting the future (Wong et al., 2023a;
is early evidence that multi-agent systems may help to im-          Gurnee and Tegmark, 2023; Park et al., 2023). Learned
prove factuality and reasoning in LLMs via debate (Du et al.,       world models like Genie (Bruce et al., 2024), and text-to-
2023c; Tang et al., 2023), although there is much more re-          video generation models like Sora (Brooks et al., 2024)
search needed before superhuman capability is reached.              demonstrate that foundation video models can be used as
                                                                    learned simulators, including in real-world settings like
3.2. Self-Improvement                                               robotics (Yang et al., 2023b) and autonomous driving (Hu
                                                                    et al., 2023). If these works combine with learned multi-
To achieve open-endedness, a model must not only con-               modal reward models (Chan et al., 2023; Du et al., 2023a),
sume knowledge from pre-collected feedback as in, for               they could be used to generate an open-ended curriculum of
example, RLHF (Ziegler et al., 2019), but also generate             tasks, scaling to task spaces far larger and more photorealis-
new knowledge, in form of hypotheses, insights or creative          tic than can currently be achieved. At sufficient scale, this
outputs beyond the human curated training data. A self-             may provide a path to generating AI agents with superhu-
improvement loop should allow the agent to actively engage          man adaptability across a wide range of previously unseen
in tasks that push the boundary of its knowledge and ca-            tasks, which can be deployed in the real world across the
pabilities, for example via leveraging tools such as search         rapidly closing Sim-to-Real gap (Huang et al., 2023).
engines, simulated environments, calculators or interpreters
and interacting with other agents (Jiang et al., 2022; Schick       3.4. Evolutionary Algorithms
et al., 2024). This requires the model to have a scalable
mechanism to evaluate its own performance, identify areas           Evolutionary methods offer a promising path to generate
for improvement, and adapt its learning process accordingly.        open-ended systems with foundation models (Wu et al.,
                                                                    2024). LLMs are well-placed to act as selection and muta-
There is growing evidence that foundation models can be             tion operators, as they have been trained on vast datasets of
leveraged for feedback in place of humans, and can signifi-         human knowledge, culture and preferences. For example,
cantly amplify data generated by humans. Examples include           LLMs offer a mechanism through which to make semanti-
self-critique and revision for training harmless assistants         cally meaningful mutations via text (Lehman et al., 2022;
(Bai et al., 2022) and guiding human evaluators (Saunders           Meyerson et al., 2023; Chen et al., 2023a). The simplest
et al., 2022), self-correction for tool-use (Gou et al., 2023),     such approach may be via prompts, which already allow
self-instruction for instruction following (Wang et al., 2022),     foundation models to further improve their performance.
self-debugging for code generation (Chen et al., 2023b), self-      Recent works have shown it is possible to far surpass human
rewarding for instruction following (Yuan et al., 2024), and        designed prompts, leading to stronger models (Fernando
leveraging VLMs as reward functions for control (Baumli             et al., 2023; Yang et al., 2023a; Guo et al., 2023). More
et al., 2023). These works hint at the possibility of founda-       recently, Bradley et al. (2023) and Samvelyan et al. (2024)
tion models generating their own samples and refining them          went further, using an evolutionary algorithm and LLMs to
in an open-ended way.                                               both generate variation and evaluate the quality and diversity
                                                                    of candidate text, making it possible to guide the search for
3.3. Task Generation                                                creative and novel outputs. In the future it may be possible
                                                                    to further refine a model on these outputs, or use them for
Closely related to both RL and self-improvement is the prob-        planning (Gandhi et al., 2023), to achieve self-improvement.
lem of task generation, also known as the “problem problem”
(Leibo et al., 2019). One great candidate approach for open-        Another angle of attack for evolutionary methods is in the
endedness is to keep adapting the difficulty of tasks to an         space of code (also known as genetic programming). Foun-
agent’s capability so that they remain forever challenging          dation models have proven to be competent at producing
yet learnable. Past examples of this type of system include         diverse and novel programs, providing a means of iterat-
setter-solvers (Schmidhuber, 1991b) and unsupervised envi-          ing upon an archive of candidate solutions. For example,
ronment design (Dennis et al., 2020; Justesen et al., 2018;         Eureka (Ma et al., 2023) evolves code-based reward func-
Wang et al., 2019). With the advent of foundation models,           tions to learn complex control behaviors. Similarly, Fun-
it has become feasible to use the Internet itself as an envi-       Search (Romera-Paredes et al., 2024) evolves programs that
ronment (Jiang et al., 2022; Gur et al., 2021) via web-based        represent new mathematical knowledge. These examples
APIs, affording agents with an incredibly rich, ever-growing        are focused on specific domains, and it remains an open
and human-relevant task domain (Zhou et al., 2023).                 problem to scale code evolution to a more general setting.

                                                                 7


--- page break ---

Open-Endedness is Essential for Artificial Superhuman Intelligence

4. Achieving ASI Responsibly

Now that we have foundation models, designing a truly gen-          Figure 2. Knowledge accumulation and transfer in a human-AI
eral open-ended learning system may be within our grasp.            open-ended system. We depict AI building on AI knowledge,
However, the power of open-endedness comes with a swathe            humans understanding AI knowledge, AI understanding human
of notable safety risks—beyond existing safety considera-           knowledge, humans building on human knowledge, and emergent
tions facing foundation models (Ecoffet et al., 2020). Find-        knowledge created by the process as a whole. Every process in
ing solutions to these challenges are interesting and impor-        this diagram offers an opportunity to embed safety methods that
tant core problems in open-endedness research. Because              guide the system towards achieving ASI responsibly.
the solutions to these problems may well depend on the
design of the open-ended system, it is critical that safety         4.2. Humans Understanding AI Creations
and open-endedness are pursued in tandem. We cover them
here not to hold them separate from other directions in             In order to provide informed oversight and direction when
open-endedness—in fact many of these problems are cur-              guiding an open-ended system, human observers need to
rent practical limitations of artificial open-ended systems.        at least partially understand the significance of the new
Rather, this section is intended to draw specific attention         artifacts that the system produces. This becomes increas-
to these problems as some of the most fundamental and               ingly challenging as the complexity of these artifacts grows,
exciting directions for research in the field. Of course, this      leading to the inability to give informed oversight and guid-
short section cannot do justice to the breadth of concerns.         ance. Such a system may not only be unsafe, but would no
Hence, where possible, we provide references to the wealth          longer be open-ended for human observers, since it would
of knowledge in the ASI safety community.                           no longer be learnable. As such, any open-ended system
                                                                    we want to build should have the ability to bring human ob-
We organize our understanding of these risks similar to             servers along with it—understanding and interpreting these
(Critch and Krueger, 2020) by focusing on the ways knowl-           systems is not only a core problem to make them safe, it is
edge is created and transmitted through the joint human-AI          also a core problem to make them useful.
open-ended process in Figure 2. A powerful open-ended
system which has the problems listed in this section is not a       One approach would be to try to understand the policy gen-
beneficial open-ended system, and we believe it is not one          erated by open-ended systems through interpretability. With
we should be striving to build. Solving these problems is           current approaches this would require a formidable inter-
not just making open-ended systems safer, but also making           pretability effort for each domain of interest. However,
them usable by humans. As such, addressing these prob-              with the advent of automated interpretability (Bills et al.,
lems should be thought of as minimum specifications of an           2023), one may hope to build increasingly good explana-
open-ended system that we would want to build.                      tions of the systems’ behaviors which match the increasing
                                                                    complexity of the open-ended system. This presents an
4.1. AI Creation and Agency                                         sizeable challenge, as such a system would be a universal
                                                                    explainer (Deutsch, 2011), by definition.
AI systems powering the open-ended creation of new knowl-
edge could lead to powerful new affordances. Without di-            An alternative approach is to prefer designs for open-ended
rection, these creations could be the source of dual-use            systems which promote interpretability and explainability,
dangers (Urbina et al., 2022). The danger is magnified when         or whose goal is to teach human observers. Already, there
the open-ended systems take immediate action in an envi-            are efforts to train systems which directly inform the user of
ronment. Current state-of-the-art systems operate in narrow,        implicit knowledge (Christiano et al., 2021). One might aim
simulated environments (Wang et al., 2023a; OEL Team                to design systems that at least maintain informed oversight
et al., 2021; Bauer et al., 2023). However, as AI is trained in     (Amodei et al., 2016; Bowman et al., 2022). This approach
broader, more diverse simulations or is even deployed (and
continues to learn) in the real world, it becomes critical to
understand the dangers. The agency of open-ended AI poses
several safety risks, such as goal misgeneralization (di Lan-
gosco et al., 2022; Shah et al., 2022) and specification gam-
ing (Clark and Amodei, 2016). Open-ended search can be
seen as an ambitiously aggressive form of exploration; thus
one could hope to use similar approaches to mitigate the dan-
gers of exploration as in RL, like safe exploration (Garcıa
and Ferna´ndez, 2015) and impact regularization (Krakovna
et al., 2018; Turner et al., 2020).

                                                                 8


--- page break ---

Open-Endedness is Essential for Artificial Superhuman Intelligence

may be especially effective if the design of the open-ended            governance rapidly and retrospectively in response to open-
system automatically facilitates understanding and control             ended artifacts, finding a good balance between collecting
by human users (Irving et al., 2018).                                  information and avoiding entrenchment of undesirable arti-
                                                                       facts (Collingridge, 1980).
4.3. Humans Guiding AI Creation
                                                                       4.5. Emergent Risks of Open-Ended Systems
Even if we assume that human observers can understand
enough of the behavior of an open-ended system to be in a              Even if each subcomponent of Figure 2 can be made safe,
position to give informed feedback, we arrive at the question          it may still be the case that the aggregate joint human-AI
of how a human designer could meaningfully guide an open-              open-ended system leads to unforeseen problems. For in-
ended system. This challenge goes beyond the difficulties of           stance, two systems that are open-ended in isolation could
directing individual RL agents, as not only do open-ended              negatively interact to cause neither to be open-ended. This
systems often lack well-defined objectives that could be               would mean a cessation of progress and an inability to col-
modified, but they are increasingly unpredictable by design.           lectively respond to new challenges. While such emergent
One possibility would be to use humans in the loop to drive            effects have been studied in multi-agent systems (Johanson
open-endedness (Secretan et al., 2008), a kind of open-                et al., 2022) and ASI safety (Critch and Krueger, 2020) solu-
endedness from human feedback (Zhang et al., 2023). A                  tions are still elusive, and an understanding of these effects
complete solution to this problem not only needs to be                 is critical to the safe deployment of open-ended systems.
directable, but must actively raise unexpected and possibly
important artifacts to the user’s attention.                           If such problems are inevitable and unpredictable, we would
                                                                       need our human-AI open-ended systems to adapt to solve
If open-ended systems could be made as directable as in-               novel ASI safety failures as they arise. Due to the in-
dividual RL agents, then work defining objectives which                herent unpredictability of knowledge creation, these prob-
preserve controllability (Hadfield-Menell et al., 2016; 2017;          lems may be both unavoidable and solvable once as they
Carey and Everitt, 2023) might be a promising path towards             arise (Deutsch, 2011). We should be building an open-ended
more controllable open-ended systems. However, direct-                 system whose safety is anti-fragile (Taleb, 2014), adapting
ing an open-ended system towards any objective effectively             to emerging safety risks and getting stronger for it. This
while maintaining the open-endedness is an open problem.               entails designing techniques for understanding, monitoring,
This problem is not only important for safety, but is impor-           and rapidly coordinating responses to emerging risks.
tant for open-ended systems to be useful. In sufficiently
broad domains—such as all of mathematics, all proteins, or             5. Conclusion and Outlook
all behaviors on a computer—an open-ended system may
rabbit-hole into the obscure theorems, useless proteins, or            Foundation models have led to a rapid increase in the gen-
only certain computer applications. Thus, building mech-               erality of current AI systems. However, current foundation
anisms that allow us to direct open-ended systems to not               models are limited in their capability to discover new knowl-
just the safe artifacts, but the interesting and useful artifacts,     edge. In this paper, our position is that to further advance
is a fruitful avenue for collaboration between safety and              in levels of AGI towards ASI, we require systems that are
open-endedness researchers.                                            open-ended—endowed with the ability to generate novel
                                                                       and learnable artifacts for a human observer. There has
4.4. Human Society Adapting                                            never been a more exciting time to build such systems, with
                                                                       foundation models already exhibiting general human-like
There are significant non-technical concerns in ensuring that          knowledge that both accelerates further learning and guides
society can understand, prepare for, and appropriately react           this learning towards human-relevant artifacts.
to new technological capabilities emerging from open-ended
foundation models. Indeed, the impact of AI systems is not             As we develop and deploy more generally-capable open-
just felt at the individual level, but also at the level of the        ended systems, novel safety concerns arise that will be criti-
collectives that structure our society—communities, organ-             cal to address. In order to realise the benefits of such sys-
isations, markets and nation states, to name a few. Since              tems, it is important that the human observer remains able
the artifacts arising from open-ended foundation models                to learn from the novel artifacts, bringing fields such as ex-
will by definition appear novel, we must devote prospective            plainability to the forefront of open-endedness research. If
attention to the ways in which these could harm or benefit             these endeavors are successful, then we believe open-ended
the cooperative infrastructure of society (Dafoe et al., 2020).        foundation models could lead to advances that drastically
Likewise, we must develop mechanisms to avoid tipping                  enhance modern society.
points driven by feedback loops, like flash crashes (Aldrich
et al., 2017). Decision-makers should be prepared to adapt

                                                                    9


--- page break ---

Open-Endedness is Essential for Artificial Superhuman Intelligence

Impact Statement                                                        man, and D. Mane´. Concrete problems in ai safety.
                                                                       ArXiv preprint, abs/1606.06565, 2016. URL https:
Our work provides a formal definition of open-endedness,               //arxiv.org/abs/1606.06565.
and provides a discussion on its significance for the pursuit
of ASI. We explore current research directions in the field,         Y. Bai, S. Kadavath, S. Kundu, A. Askell, J. Kernion,
emphasising the potential of combining open-endedness                  A. Jones, A. Chen, A. Goldie, A. Mirhoseini, C. McK-
with foundation models as a pre-eminent path towards                    innon, C. Chen, C. Olsson, C. Olah, D. Hernan-
achieving ASI. Developed responsibly, we believe that such              dez, D. Drain, D. Ganguli, D. Li, E. Tran-Johnson,
open-ended foundation models can have tremendous posi-                  E. Perez, J. Kerr, J. Mueller, J. Ladish, J. Landau,
tive impact on the society, accelerating scientific and techno-         K. Ndousse, K. Lukosuite, L. Lovitt, M. Sellitto, N. El-
logical breakthroughs, enhancing human creativity through               hage, N. Schiefer, N. Mercado, N. DasSarma, R. Lasenby,
a collaborative feedback loop, and acting as an engine for              R. Larson, S. Ringer, S. Johnston, S. Kravec, S. E.
general knowledge expansion across many fields. Recognis-               Showk, S. Fort, T. Lanham, T. Telleen-Lawton, T. Con-
ing the profound implications of this concept, we dedicate              erly, T. Henighan, T. Hume, S. R. Bowman, Z. Hatfield-
the entirety of Section 4 to an initial analysis of potential           Dodds, B. Mann, D. Amodei, N. Joseph, S. McCandlish,
risks and societal impacts, offering frameworks for the re-            T. Brown, and J. Kaplan. Constitutional AI: Harmlessness
sponsible and ethical development of ASI. We hope that                  from AI Feedback, Dec. 2022.
highlighting these issues early will help to promote safety,
responsibility and accountability as the field grows.                B. Baker, I. Kanitscheider, T. M. Markov, Y. Wu, G. Powell,
                                                                        B. McGrew, and I. Mordatch. Emergent tool use from
Acknowledgements                                                        multi-agent autocurricula. In 8th International Confer-
                                                                        ence on Learning Representations, ICLR 2020, Addis
We gratefully acknowledge Dave Abel for providing valu-                Ababa, Ethiopia, April 26-30, 2020. OpenReview.net,
able feedback on an early draft of this paper. We are thankful          2020. URL https://openreview.net/forum?
to the designers at the Noun Project, from which we sourced             id=SkxpxJBKwS.
graphics under the CC BY 3.0 licence as follows: “tick”
icon by kareemovic, “Delete” icon by kareemovic, “alien”             A. Bakhtin, N. Brown, E. Dinan, G. Farina, C. Flaherty,
icon by Artem Yurov, “girl” icon by Teewara soontorn, “year             D. Fried, A. Goff, J. Gray, H. Hu, et al. Human-level play
of rat” icon by DailyPM, “aircraft” icon by mikicon, “con-              in the game of diplomacy by combining language models
corde” icon by mikicon, “Plane” icon by CAMB, “humans”                 with strategic reasoning. Science, 378(6624):1067–1074,
icon by Ifanicon, and “Robot” icon by Deemak Daksina.                   2022.

References                                                           J. Bauer, K. Baumli, F. Behbahani, A. Bhoopchand,
                                                                        N. Bradley-Schmieg, M. Chang, N. Clay, A. Collister,
D. Abel, A. Barreto, B. Van Roy, D. Precup, H. van Hasselt,            V. Dasagi, L. Gonzalez, K. Gregor, E. Hughes, S. Kashem,
   and S. Singh. A definition of continual reinforcement                M. Loks-Thompson, H. Openshaw, J. Parker-Holder,
   learning. ArXiv preprint, abs/2307.11046, 2023. URL                  S. Pathak, N. Perez-Nieves, N. Rakicevic, T. Rockta¨schel,
   https://arxiv.org/abs/2307.11046.                                   Y. Schroecker, S. Singh, J. Sygnowski, K. Tuyls, S. York,
                                                                       A. Zacherl, and L. M. Zhang. Human-timescale adapta-
M. Ahn, A. Brohan, N. Brown, Y. Chebotar, O. Cortes,                    tion in an open-ended task space. In A. Krause, E. Brun-
   B. David, C. Finn, C. Fu, K. Gopalakrishnan, K. Haus-                skill, K. Cho, B. Engelhardt, S. Sabato, and J. Scarlett,
   man, A. Herzog, D. Ho, J. Hsu, J. Ibarz, B. Ichter,                  editors, Proceedings of the 40th International Conference
   A. Irpan, E. Jang, R. J. Ruano, K. Jeffrey, S. Jesmonth,             on Machine Learning, volume 202 of Proceedings of
   N. J. Joshi, R. Julian, D. Kalashnikov, Y. Kuang, K.-               Machine Learning Research, pages 1887–1935. PMLR,
   H. Lee, S. Levine, Y. Lu, L. Luu, C. Parada, P. Pastor,              2023.
   J. Quiambao, K. Rao, J. Rettinghouse, D. Reyes, P. Ser-
   manet, N. Sievers, C. Tan, A. Toshev, V. Vanhoucke,               K. Baumli, S. Baveja, F. Behbahani, H. Chan, G. Comanici,
   F. Xia, T. Xiao, P. Xu, S. Xu, M. Yan, and A. Zeng. Do               S. Flennerhag, M. Gazeau, K. Holsheimer, D. Horgan,
   As I Can, Not As I Say: Grounding Language in Robotic                M. Laskin, et al. Vision-language models as a source of
   Affordances, Aug. 2022.                                              rewards. ArXiv preprint, abs/2312.09187, 2023. URL
                                                                        https://arxiv.org/abs/2312.09187.
E. M. Aldrich, J. Grundfest, and G. Laughlin. The flash
   crash: A new deconstruction. Available at SSRN 2721922,           M. Bedau. Measurement of evolutionary activity, teleology,
   2017.                                                                and life. 1992.

D. Amodei, C. Olah, J. Steinhardt, P. Christiano, J. Schul-          M. A. Bedau, E. Snyder, C. T. Brown, N. H. Packard, et al. A
                                                                        comparison of evolutionary activity in artificial evolving

                                                                 10


--- page break ---

                    Open-Endedness is Essential for Artificial Superhuman Intelligence

   systems and in the biosphere. In Proceedings of the fourth          N. Heess, L. Gonzalez, S. Osindero, S. Ozair, S. Reed,
  European conference on artificial life, pages 125–134.              J. Zhang, K. Zolna, J. Clune, N. de Freitas, S. Singh, and
   MIt Press Cambridge, 1997.                                         T. Rockta¨schel. Genie: Generative Interactive Environ-
                                                                       ments, Feb. 2024.
M. A. Bedau, E. Snyder, and N. H. Packard. A classification
   of long-term evolutionary dynamics. Artificial Life: The         Y. Burda, H. Edwards, A. Storkey, and O. Klimov. Explo-
  Proceedings..., page 228, 1998.                                      ration by Random Network Distillation, Oct. 2018.

M. Bellemare, S. Srinivasan, G. Ostrovski, T. Schaul,               M. C. Campi and S. Garatti. Compression, generalization
   D. Saxton, and R. Munos. Unifying count-based ex-                   and learning. ArXiv preprint, abs/2301.12767, 2023. URL
   ploration and intrinsic motivation. Advances in neural              https://arxiv.org/abs/2301.12767.
   information processing systems, 29, 2016.
                                                                    R. Carey and T. Everitt. Human control: Definitions and
C. Berner, G. Brockman, B. Chan, V. Cheung, P. Debiak,                 algorithms. ArXiv preprint, abs/2305.19861, 2023. URL
   C. Dennison, D. Farhi, Q. Fischer, S. Hashme, C. Hesse,             https://arxiv.org/abs/2305.19861.
   et al. Dota 2 with large scale deep reinforcement learning.
  ArXiv preprint, abs/1912.06680, 2019. URL https:                  H. Chan, V. Mnih, F. Behbahani, M. Laskin, L. Wang,
  //arxiv.org/abs/1912.06680.                                          F. Pardo, M. Gazeau, H. Sahni, D. Horgan, K. Baumli,
                                                                      Y. Schroecker, S. Spencer, R. Steigerwald, J. Quan, G. Co-
S. Bills, N. Cammarata, D. Mossing, H. Tillman, L. Gao,                manici, S. Flennerhag, A. Neitz, L. M. Zhang, T. Schaul,
   G. Goh, I. Sutskever, J. Leike, J. Wu, and W. Saun-                 S. Singh, C. Lyle, T. Rockta¨schel, J. Parker-Holder, and
   ders. Language models can explain neurons in language               K. Holsheimer. Vision-language models as a source of
   models. URL https://openaipublic. blob. core. windows.              rewards. In Second Agent Learning in Open-Endedness
   net/neuron-explainer/paper/index. html.(Date accessed:             Workshop, 2023.
  14.05. 2023), 2023.
                                                                    A. Chen, D. M. Dohan, and D. R. So. EvoPrompting:
R. Bommasani, D. A. Hudson, E. Adeli, R. Altman,                       Language Models for Code-Level Neural Architecture
   S. Arora, S. von Arx, M. S. Bernstein, J. Bohg, A. Bosse-           Search, Feb. 2023a.
   lut, E. Brunskill, et al. On the opportunities and risks
   of foundation models. arXiv preprint arXiv:2108.07258,           X. Chen, M. Lin, N. Scha¨rli, and D. Zhou. Teaching Large
   2021.                                                               Language Models to Self-Debug, Apr. 2023b.

S. R. Bowman, J. Hyun, E. Perez, E. Chen, C. Pettit,                P. Christiano, A. Cotra, and M. Xu. Eliciting latent knowl-
   S. Heiner, K. Lukosˇiu¯te˙, A. Askell, A. Jones, A. Chen,           edge: How to tell if your eyes deceive you, 2021.
   et al. Measuring progress on scalable oversight for large
   language models. ArXiv preprint, abs/2211.03540, 2022.           J. Clark and D. Amodei. Faulty reward functions in the
   URL https://arxiv.org/abs/2211.03540.                              wild. Internet: https://blog. openai. com/faulty-reward-
                                                                       functions, 2016.

H. Bradley, A. Dai, H. Teufel, J. Zhang, K. Oostermei-              J. Clune. AI-GAs: AI-generating algorithms, an alternate
   jer, M. Bellagente, J. Clune, K. Stanley, G. Schott, and            paradigm for producing general artificial intelligence, Jan.
  J. Lehman. Quality-Diversity through AI Feedback, Oct.               2020.

2023.                                                               J. Clune. Ai will go farterh if it stands on the shoulders of

J. C. Brant and K. O. Stanley. Minimal criterion coevolution:       giant human data sets. Dec. 2022.

a new approach to open-ended search. In Proceedings of C. Colas, T. Karch, O. Sigaud, and P.-Y. Oudeyer. Autotelic

the Genetic and Evolutionary Computation Conference,                agents with intrinsically motivated goal-conditioned rein-

pages 67–74, 2017.                                                  forcement learning: a short survey. Journal of Artificial

T. Brooks, B. Peebles, C. Holmes, W. DePue, Y. Guo,                 Intelligence Research, 74:1159–1199, 2022.

L. Jing, D. Schnurr, J. Taylor, T. Luhman, E. Luh- D. Collingridge. The Social Control of Technology.

man, C. Ng, R. Wang, and A. Ramesh. Video                           St. Martin’s Press, 1980. ISBN 9780312731687.

generation models as world simulators. 2024.                        URL https://books.google.co.uk/books?

URL    https://openai.com/research/                                 id=hCSdAQAACAAJ.

video-generation-models-as-world-simulators.
                                                                         A. Critch and D. Krueger. Ai research considerations

J. Bruce, M. Dennis, A. Edwards, J. Parker-Holder, Y. Shi,          for human existential safety (arches). ArXiv preprint,

E. Hughes, M. Lai, A. Mavalankar, R. Steigerwald,                   abs/2006.04948, 2020. URL https://arxiv.org/

C. Apps, Y. Aytar, S. Bechtle, F. Behbahani, S. Chan,               abs/2006.04948.

                                                                11


--- page break ---

Open-Endedness is Essential for Artificial Superhuman Intelligence

A. Dafoe, E. Hughes, Y. Bachrach, T. Collins, K. R. McKee,        Y. Du, S. Li, A. Torralba, J. B. Tenenbaum, and I. Mor-
  J. Z. Leibo, K. Larson, and T. Graepel. Open Problems              datch. Improving factuality and reasoning in language
   in Cooperative AI, Dec. 2020.                                     models through multiagent debate. arXiv preprint
                                                                     arXiv:2305.14325, 2023c.
O. David, S. Moran, and A. Yehudayoff. On statistical
   learning via the lens of compression. ArXiv preprint,          S. Earle, J. Togelius, and L. B. Soros. Video games as
   abs/1610.03592, 2016. URL https://arxiv.org/                      a testbed for open-ended phenomena. In 2021 IEEE
   abs/1610.03592.                                                  Conference on Games (CoG), pages 1–9. IEEE, 2021.

G. Dele´tang, A. Ruoss, P.-A. Duquenne, E. Catt, T. Ge-           A. Ecoffet, J. Clune, and J. Lehman. Open Questions in
   newein, C. Mattern, J. Grau-Moya, L. K. Wenliang,                 Creating Safe Open-ended AI: Tensions Between Control
   M. Aitchison, L. Orseau, M. Hutter, and J. Veness. Lan-           and Creativity, June 2020.
   guage Modeling Is Compression, Sept. 2023.
                                                                  M. Faldor, J. Zhang, A. Cully, and J. Clune. Omni-epic:
M. Dennis, N. Jaques, E. Vinitsky, A. M. Bayen, S. Rus-              Open-endedness via models of human notions of interest-
   sell, A. Critch, and S. Levine. Emergent complexity and           ingness with environments programmed in code. arXiv
   zero-shot transfer via unsupervised environment design.           preprint arXiv:2405.15568, 2024.
   In H. Larochelle, M. Ranzato, R. Hadsell, M. Balcan, and
   H. Lin, editors, Advances in Neural Information Process-       C. Fernando, D. Banarse, H. Michalewski, S. Osindero, and
   ing Systems 33: Annual Conference on Neural Informa-             T. Rockta¨schel. Promptbreeder: Self-Referential Self-
   tion Processing Systems 2020, NeurIPS 2020, December              Improvement Via Prompt Evolution, Sept. 2023.
   6-12, 2020, virtual, 2020.
                                                                  K. Gandhi, D. Sadigh, and N. D. Goodman. Strategic Rea-
J. Derbyshire. Potential surprise theory as a theoretical foun-      soning with Language Models, May 2023.
   dation for scenario planning. Technological Forecasting
   and Social Change, 124:77–87, 2017.                            J. Garcıa and F. Ferna´ndez. A comprehensive survey on safe
                                                                     reinforcement learning. Journal of Machine Learning
D. Deutsch. The beginning of infinity: Explanations that            Research, 16(1):1437–1480, 2015.
   transform the world. Penguin UK, 2011.
                                                                  Z. Gou, Z. Shao, Y. Gong, Y. Shen, Y. Yang, N. Duan,
L. L. di Langosco, J. Koch, L. D. Sharkey, J. Pfau, and              and W. Chen. Critic: Large language models can self-
   D. Krueger. Goal misgeneralization in deep reinforce-             correct with tool-interactive critiquing. ArXiv preprint,
   ment learning. In K. Chaudhuri, S. Jegelka, L. Song,              abs/2305.11738, 2023. URL https://arxiv.org/
   C. Szepesva´ri, G. Niu, and S. Sabato, editors, Interna-          abs/2305.11738.
   tional Conference on Machine Learning, ICML 2022, 17-
  23 July 2022, Baltimore, Maryland, USA, volume 162 of           Q. Guo, R. Wang, J. Guo, B. Li, K. Song, X. Tan, G. Liu,
  Proceedings of Machine Learning Research, pages 12004–            J. Bian, and Y. Yang. Connecting Large Language Models
  12019. PMLR, 2022. URL https://proceedings.                       with Evolutionary Algorithms Yields Powerful Prompt
   mlr.press/v162/langosco22a.html.                                  Optimizers, Sept. 2023.

E. L. Dolson, A. E. Vostinar, M. J. Wiser, and C. Ofria. The      I. Gur, N. Jaques, Y. Miao, J. Choi, M. Tiwari, H. Lee, and
   modes toolbox: Measurements of open-ended dynamics               A. Faust. Environment generation for zero-shot com-
   in evolving systems. Artificial life, 25(1):50–73, 2019.          positional reinforcement learning. Advances in Neural
                                                                    Information Processing Systems, 34:4157–4169, 2021.
Y. Du, K. Konyushkova, M. Denil, A. Raju, J. Landon,
   F. Hill, N. de Freitas, and S. Cabi. Vision-language mod-      W. Gurnee and M. Tegmark. Language Models Represent
   els as success detectors. In Proceedings of The 2nd Con-          Space and Time, Oct. 2023.
   ference on Lifelong Learning Agents, pages 120–136,
   2023a.                                                         D. Hadfield-Menell, S. J. Russell, P. Abbeel, and A. D.
                                                                     Dragan. Cooperative inverse reinforcement learning. In
Y. Du, E. Kosoy, A. Dayan, M. Rufova, P. Abbeel, and                 D. D. Lee, M. Sugiyama, U. von Luxburg, I. Guyon,
  A. Gopnik. What can ai learn from human exploration?               and R. Garnett, editors, Advances in Neural Information
   intrinsically-motivated humans and agents in open-world          Processing Systems 29: Annual Conference on Neural
   exploration. In NeurIPS 2023 workshop: Information-              Information Processing Systems 2016, December 5-10,
  Theoretic Principles in Cognitive Systems, 2023b.                 2016, Barcelona, Spain, pages 3909–3917, 2016.

                                                              12


--- page break ---

Open-Endedness is Essential for Artificial Superhuman Intelligence

D. Hadfield-Menell, A. D. Dragan, P. Abbeel, and S. J.              M. Klissarov, P. D’Oro, S. Sodhani, R. Raileanu, P.-L. Ba-
   Russell. The off-switch game. In C. Sierra, editor, Pro-            con, P. Vincent, A. Zhang, and M. Henaff. Motif: Intrinsic
   ceedings of the Twenty-Sixth International Joint Confer-            Motivation from Artificial Intelligence Feedback, Sept.
   ence on Artificial Intelligence, IJCAI 2017, Melbourne,             2023.
  Australia, August 19-25, 2017, pages 220–227. ijcai.org,
   2017. doi: 10.24963/ijcai.2017/32. URL https:                    F. H. Knight. Risk, uncertainty and profit, volume 31.
  //doi.org/10.24963/ijcai.2017/32.                                    Houghton Mifflin, 1921.

E. Hazan and S. Kale. Extracting certainty from uncertainty:        V. Krakovna, L. Orseau, R. Kumar, M. Martic, and S. Legg.
   Regret bounded by variation in costs. Machine learning,             Penalizing side effects using stepwise relative reachability.
   80:165–188, 2010.                                                  ArXiv preprint, abs/1806.01186, 2018. URL https:
                                                                      //arxiv.org/abs/1806.01186.
M. Henaff, R. Raileanu, M. Jiang, and T. Rockta¨schel. Ex-
   ploration via Elliptical Episodic Bonuses, Jan. 2023.            S. Legg and M. Hutter. Universal Intelligence: A Definition
                                                                       of Machine Intelligence, Dec. 2007.
J. H. Holland. Adaptation in natural and artificial systems:
   an introductory analysis with applications to biology,           J. Lehman and K. O. Stanley. Abandoning Objectives: Evo-
   control, and artificial intelligence. MIT press, 1992.              lution Through the Search for Novelty Alone. Evolu-
                                                                       tionary Computation, 19(2):189–223, June 2011. ISSN
A. Hu, L. Russell, H. Yeo, Z. Murez, G. Fedoseev,                     1063-6560. doi: 10.1162/EVCO a 00025.
  A. Kendall, J. Shotton, and G. Corrado. GAIA-1: A
   Generative World Model for Autonomous Driving, Sept.             J. Lehman, J. Gordon, S. Jain, K. Ndousse, C. Yeh, and
   2023.                                                               K. O. Stanley. Evolution through Large Models, June
                                                                       2022.
J. Huang, S. S. Gu, L. Hou, Y. Wu, X. Wang, H. Yu, and
  J. Han. Large Language Models Can Self-Improve, Oct.              J. Z. Leibo, E. Hughes, M. Lanctot, and T. Graepel. Au-
   2022.                                                               tocurricula and the Emergence of Innovation from Social
                                                                       Interaction: A Manifesto for Multi-Agent Intelligence
P. Huang, X. Zhang, Z. Cao, S. Liu, M. Xu, W. Ding, J. Fran-           Research, Mar. 2019.
   cis, B. Chen, and D. Zhao. What went wrong? closing
   the sim-to-real gap via differentiable causal discovery. In      S. Lifshitz, K. Paster, H. Chan, J. Ba, and S. McIlraith.
  Conference on Robot Learning, pages 734–760. PMLR,                   STEVE-1: A Generative Model for Text-to-Behavior in
   2023.                                                               Minecraft, June 2023.

M. Hutter. Universal artificial intelligence: Sequential            S. Liu, C. Chen, X. Qu, K. Tang, and Y.-S. Ong. Large lan-
   decisions based on algorithmic probability. Springer                guage models as evolutionary optimizers. arXiv preprint
   Science & Business Media, 2004.                                     arXiv:2310.19046, 2023a.

G. Irving, P. Christiano, and D. Amodei. AI safety via              X. Liu, H. Yu, H. Zhang, Y. Xu, X. Lei, H. Lai, Y. Gu,
   debate, Oct. 2018.                                                  H. Ding, K. Men, K. Yang, S. Zhang, X. Deng, A. Zeng,
                                                                       Z. Du, C. Zhang, S. Shen, T. Zhang, Y. Su, H. Sun,
M. Jiang, E. Grefenstette, and T. Rockta¨schel. Prioritized            M. Huang, Y. Dong, and J. Tang. AgentBench: Eval-
   Level Replay, June 2021.                                            uating LLMs as Agents, Aug. 2023b.

M. Jiang, T. Rockta¨schel, and E. Grefenstette. General             Y. J. Ma, W. Liang, G. Wang, D.-A. Huang, O. Bastani,
   Intelligence Requires Rethinking Exploration, Nov. 2022.            D. Jayaraman, Y. Zhu, L. Fan, and A. Anandkumar. Eu-
                                                                       reka: Human-Level Reward Design via Coding Large
M. B. Johanson, E. Hughes, F. Timbers, and J. Z. Leibo.                Language Models, Oct. 2023.
   Emergent bartering behaviour in multi-agent reinforce-
   ment learning. ArXiv preprint, abs/2205.06760, 2022.             A. N. Mavor-Parker, K. A. Young, C. Barry, and L. D.
   URL https://arxiv.org/abs/2205.06760.                               Griffin. How to stay curious while avoiding noisy tvs
                                                                       using aleatoric uncertainty estimation. In K. Chaud-
N. Justesen, R. R. Torrado, P. Bontrager, A. Khalifa, J. To-           huri, S. Jegelka, L. Song, C. Szepesva´ri, G. Niu, and
   gelius, and S. Risi. Illuminating generalization in deep            S. Sabato, editors, International Conference on Ma-
   reinforcement learning through procedural level genera-             chine Learning, ICML 2022, 17-23 July 2022, Balti-
   tion. arXiv preprint arXiv:1806.10729, 2018.                        more, Maryland, USA, volume 162 of Proceedings of
                                                                      Machine Learning Research, pages 15220–15240. PMLR,
                                                                       2022. URL https://proceedings.mlr.press/
                                                                      v162/mavor-parker22a.html.

                                                                13


--- page break ---

Open-Endedness is Essential for Artificial Superhuman Intelligence

D. W. McShea. Perspective metazoan complexity and evo-                 and S. Sabato, editors, International Conference on Ma-
   lution: is there a trend? Evolution, 50(2):477–492, 1996.           chine Learning, ICML 2022, 17-23 July 2022, Balti-
                                                                       more, Maryland, USA, volume 162 of Proceedings of
E. Meyerson, M. J. Nelson, H. Bradley, A. Moradi, A. K.               Machine Learning Research, pages 17473–17498. PMLR,
   Hoover, and J. Lehman. Language Model Crossover:                    2022. URL https://proceedings.mlr.press/
  Variation through Few-Shot Prompting, Feb. 2023.                    v162/parker-holder22a.html.

S. Mirchandani, F. Xia, P. Florence, B. Ichter, D. Driess,          D. Pathak, P. Agrawal, A. A. Efros, and T. Darrell.
   M. G. Arenas, K. Rao, D. Sadigh, and A. Zeng. Large                 Curiosity-driven exploration by self-supervised predic-
   Language Models as General Pattern Machines, July                   tion. In D. Precup and Y. W. Teh, editors, Pro-
   2023.                                                               ceedings of the 34th International Conference on Ma-
                                                                       chine Learning, ICML 2017, Sydney, NSW, Australia,
I. Momennejad, H. Hasanbeig, F. Vieira Frujeri, H. Sharma,             6-11 August 2017, volume 70 of Proceedings of Ma-
   N. Jojic, H. Palangi, R. Ness, and J. Larson. Evaluating            chine Learning Research, pages 2778–2787. PMLR,
   cognitive maps and planning in large language models                2017. URL http://proceedings.mlr.press/
  with cogeval. Advances in Neural Information Processing             v70/pathak17a.html.
  Systems, 36, 2024.
                                                                    J. Perolat, B. De Vylder, D. Hennes, E. Tarassov, F. Strub,
M. R. Morris, J. Sohl-dickstein, N. Fiedel, T. Warkentin,             V. de Boer, P. Muller, J. T. Connor, N. Burch, T. Anthony,
  A. Dafoe, A. Faust, C. Farabet, and S. Legg. Levels of               et al. Mastering the game of stratego with model-free
  AGI: Operationalizing Progress on the Path to AGI, Nov.              multiagent reinforcement learning. Science, 378(6623):
   2023.                                                               990–996, 2022.

J.-B. Mouret and J. Clune. Illuminating search spaces by            J. K. Pugh, L. B. Soros, and K. O. Stanley. Quality diversity:
   mapping elites. ArXiv preprint, abs/1504.04909, 2015.              A new frontier for evolutionary computation. Frontiers
   URL https://arxiv.org/abs/1504.04909.                               in Robotics and AI, 3:40, 2016. ISSN 2296-9144. doi:
                                                                      10.3389/frobt.2016.00040.
OEL Team, A. Stooke, A. Mahajan, C. Barros, C. Deck,
  J. Bauer, J. Sygnowski, M. Trebacz, M. Jader-                     R. Raileanu and T. Rockta¨schel. RIDE: Rewarding Impact-
   berg, M. Mathieu, N. McAleese, N. Bradley-Schmieg,                  Driven Exploration for Procedurally-Generated Environ-
   N. Wong, N. Porcel, R. Raileanu, S. Hughes-Fitt, V. Dal-            ments, Feb. 2020.
   ibard, and W. M. Czarnecki. Open-ended learning
   leads to generally capable agents. ArXiv preprint,               P. J. Richerson, R. Boyd, et al. Institutional evolution in the
   abs/2107.12808, 2021. URL https://arxiv.org/                        holocene: the rise of complex societies. In Proceedings-
   abs/2107.12808.                                                    British Academy, volume 110, pages 197–234. Oxford
                                                                       University Press Inc., 2001.
L. Ouyang, J. Wu, X. Jiang, D. Almeida, C. L. Wain-
  wright, P. Mishkin, C. Zhang, S. Agarwal, K. Slama,               B. Romera-Paredes, M. Barekatain, A. Novikov, M. Balog,
  A. Ray, J. Schulman, J. Hilton, F. Kelton, L. Miller,                M. P. Kumar, E. Dupont, F. J. R. Ruiz, J. S. Ellenberg,
   M. Simens, A. Askell, P. Welinder, P. Christiano, J. Leike,         P. Wang, O. Fawzi, P. Kohli, and A. Fawzi. Mathematical
   and R. Lowe. Training language models to follow instruc-            discoveries from program search with large language
   tions with human feedback, Mar. 2022.                               models. Nature, 625(7995):468–475, Jan. 2024. ISSN
                                                                      1476-4687. doi: 10.1038/s41586-023-06924-6.
V. Pallagani, B. Muppasani, K. Murugesan, F. Rossi, B. Sri-
  vastava, L. Horesh, F. Fabiano, and A. Loreggia. Un-              A. L. Samuel. Some studies in machine learning using
   derstanding the capabilities of large language models for           the game of checkers. IBM Journal of research and
   automated planning. arXiv preprint arXiv:2305.16151,                development, 3(3):210–229, 1959.
   2023.
                                                                    M. Samvelyan, A. Khan, M. Dennis, M. Jiang, J. Parker-
J. S. Park, J. C. O’Brien, C. J. Cai, M. R. Morris, P. Liang,          Holder, J. Foerster, R. Raileanu, and T. Rockta¨schel.
   and M. S. Bernstein. Generative Agents: Interactive                 MAESTRO: Open-Ended Environment Design for Multi-
   Simulacra of Human Behavior, Apr. 2023.                            Agent Reinforcement Learning, Mar. 2023.

J. Parker-Holder, M. Jiang, M. Dennis, M. Samvelyan, J. N.          M. Samvelyan, S. C. Raparthy, A. Lupu, E. Hambro, A. H.
   Foerster, E. Grefenstette, and T. Rockta¨schel. Evolv-              Markosyan, M. Bhatt, Y. Mao, M. Jiang, J. Parker-Holder,
   ing curricula with regret-based environment design. In             J. Foerster, T. Rockta¨schel, and R. Raileanu. Rainbow
   K. Chaudhuri, S. Jegelka, L. Song, C. Szepesva´ri, G. Niu,          teaming: Open-ended generation of diverse adversarial
                                                                       prompts, 2024.

                                                                14


--- page break ---

Open-Endedness is Essential for Artificial Superhuman Intelligence

W. Saunders, C. Yeh, J. Wu, S. Bills, L. Ouyang, J. Ward,          I. Shumailov, Z. Shumaylov, Y. Zhao, Y. Gal, N. Papernot,
   and J. Leike. Self-critiquing models for assisting human           and R. Anderson. Model dementia: Generated data makes
   evaluators. ArXiv preprint, abs/2206.05802, 2022. URL              models forget. arXiv e-prints, pages arXiv–2305, 2023.
   https://arxiv.org/abs/2206.05802.
                                                                   P. Shyam, W. Jaskowski, and F. Gomez. Model-based active
T. Schaul, D. Borsa, D. Ding, D. Szepesvari, G. Ostro-                exploration. In K. Chaudhuri and R. Salakhutdinov, ed-
  vski, W. Dabney, and S. Osindero. Adapting behaviour                itors, Proceedings of the 36th International Conference
   for learning progress. arXiv preprint arXiv:1912.06910,            on Machine Learning, ICML 2019, 9-15 June 2019, Long
   2019.                                                             Beach, California, USA, volume 97 of Proceedings of
                                                                     Machine Learning Research, pages 5779–5788. PMLR,
T. Schick, J. Dwivedi-Yu, R. Dess`ı, R. Raileanu, M. Lomeli,          2019. URL http://proceedings.mlr.press/
   E. Hambro, L. Zettlemoyer, N. Cancedda, and T. Scialom.           v97/shyam19a.html.
  Toolformer: Language models can teach themselves to
   use tools. Advances in Neural Information Processing            O. Sigaud, G. Baldassarre, C. Colas, S. Doncieux, R. Duro,
  Systems, 36, 2024.                                                  N. Perrin-Gilbert, and V.-G. Santucci. A definition
                                                                      of open-ended learning problems for goal-conditioned
J. Schmidhuber. Adaptive confidence and adaptive curiosity.           agents. ArXiv preprint, abs/2311.00344, 2023. URL
   Inst. fu¨r Informatik, 1991a.                                      https://arxiv.org/abs/2311.00344.

J. Schmidhuber. A possibility for implementing curiosity           D. Silver, A. Huang, C. J. Maddison, A. Guez, L. Sifre,
   and boredom in model-building neural controllers. In               G. van den Driessche, J. Schrittwieser, I. Antonoglou,
  Proc. of the international conference on simulation of             V. Panneershelvam, M. Lanctot, S. Dieleman, D. Grewe,
   adaptive behavior: From animals to animats, pages 222–            J. Nham, N. Kalchbrenner, I. Sutskever, T. Lillicrap,
   227, 1991b.                                                        M. Leach, K. Kavukcuoglu, T. Graepel, and D. Hassabis.
                                                                      Mastering the game of Go with deep neural networks and
J. Secretan, N. Beato, D. B. D Ambrosio, A. Rodriguez,                tree search. Nature, 529(7587):484–489, Jan. 2016. ISSN
  A. Campbell, and K. O. Stanley. Picbreeder: Evolv-                 1476-4687. doi: 10.1038/nature16961.
   ing pictures collaboratively online. In Proceedings of the
  SIGCHI Conference on Human Factors in Computing Sys-             D. Silver, T. Hubert, J. Schrittwieser, I. Antonoglou, M. Lai,
   tems, CHI ’08, pages 1759–1768, New York, NY, USA,                A. Guez, M. Lanctot, L. Sifre, D. Kumaran, T. Graepel,
  Apr. 2008. Association for Computing Machinery. ISBN               T. Lillicrap, K. Simonyan, and D. Hassabis. Mastering
   978-1-60558-011-1. doi: 10.1145/1357054.1357328.                   Chess and Shogi by Self-Play with a General Reinforce-
                                                                      ment Learning Algorithm, Dec. 2017.
G. Shackle. Expectation in Economics. Cambridge
   University Press, 1949. ISBN 9781107629141.                     R. J. Solomonoff. A preliminary report on a general theory
   URL https://books.google.co.uk/books?                              of inductive inference. Citeseer, 1960.
   id=zEb47udAsOcC.
                                                                   L. Soros and K. Stanley. Identifying necessary condi-
R. Shah, V. Varma, R. Kumar, M. Phuong, V. Krakovna,                  tions for open-ended evolution through the artificial
  J. Uesato, and Z. Kenton. Goal misgeneralization: Why               life world of chromaria. In ALIFE 14: The Four-
   correct specifications aren’t enough for correct goals.            teenth International Conference on the Synthesis and
  ArXiv preprint, abs/2210.01790, 2022. URL https:                   Simulation of Living Systems, ALIFE 2023: Ghost
  //arxiv.org/abs/2210.01790.                                         in the Machine: Proceedings of the 2023 Artificial
                                                                      Life Conference, pages 793–800, 2014. doi: 10.
A. Sharma, D. Cze´gel, M. Lachmann, C. P. Kempes, S. I.              1162/978-0-262-32621-6-ch128. URL https://doi.
  Walker, and L. Cronin. Assembly theory explains and                 org/10.1162/978-0-262-32621-6-ch128.
   quantifies selection and evolution. Nature, 622(7982):
   321–328, Oct. 2023. ISSN 1476-4687. doi: 10.1038/               K. Stanley and J. Lehman. Why Greatness Cannot Be
   s41586-023-06600-9.                                               Planned: The Myth of the Objective. Springer In-
                                                                      ternational Publishing, 2015. ISBN 9783319155241.
M. Shin, J. Kim, B. van Opheusden, and T. L. Griffiths.               URL https://books.google.co.uk/books?
   Superhuman Artificial Intelligence Can Improve Human               id=Llb1CAAAQBAJ.
   Decision Making by Increasing Novelty. Proceedings of
   the National Academy of Sciences, 120(12):e2214840120,          K. O. Stanley. Why open-endedness matters. Artificial Life,
   Mar. 2023. ISSN 0027-8424, 1091-6490. doi: 10.1073/                25(3):232–235, 2019. ISSN 1064-5462. doi: 10.1162/
   pnas.2214840120.                                                   artl a 00294. URL https://doi.org/10.1162/
                                                                      artl_a_00294.

                                                               15


--- page break ---

Open-Endedness is Essential for Artificial Superhuman Intelligence

K. O. Stanley and L. Soros. The role of subjectivity in              T. Lillicrap, K. Kavukcuoglu, D. Hassabis, C. Apps,
   the evaluation of open-endedness. In Presentation deliv-           and D. Silver. Grandmaster level in StarCraft II us-
   ered in OEE2: The Second Workshop on Open-Ended                    ing multi-agent reinforcement learning. Nature, 575
  Evolution, at ALIFE 2016, 2016.                                    (7782):350–354, Nov. 2019. ISSN 1476-4687. doi:
                                                                     10.1038/s41586-019-1724-z.
K. O. Stanley, J. Lehman, and L. Soros. Open-endedness:
  The last grand challenge you’ve never heard of. While            L. S. Vygotsky and M. Cole. Mind in society: Development
   open-endedness could be a force for discovering intelli-           of higher psychological processes. Harvard university
   gence, it could also be a component of AI itself, 2017.            press, 1978.

S. Stepney and S. Hickinbotham. On the open-endedness              C. H. Waddington. Paradigm for an evolutionary process.
   of detecting open-endedness. Artificial Life, pages 1–26,         Biological Theory, 3:258–266, 2008.
   2023.
                                                                   G. Wang, Y. Xie, Y. Jiang, A. Mandlekar, C. Xiao, Y. Zhu,
R. J. Sternberg and J. E. Davidson. The nature of insight.            L. Fan, and A. Anandkumar. Voyager: An Open-Ended
  The MIT Press, 1995.                                                Embodied Agent with Large Language Models, May
                                                                      2023a.
N. N. Taleb. Antifragile: Things that gain from disorder,
  volume 3. Random House Trade Paperbacks, 2014.                   R. Wang, J. Lehman, J. Clune, and K. O. Stanley. Paired
                                                                      open-ended trailblazer (POET): endlessly generating in-
X. Tang, A. Zou, Z. Zhang, Y. Zhao, X. Zhang, A. Cohan,               creasingly complex and diverse learning environments
   and M. Gerstein. Medagents: Large language models                  and their solutions. ArXiv preprint, abs/1901.01753, 2019.
   as collaborators for zero-shot medical reasoning. arXiv            URL https://arxiv.org/abs/1901.01753.
   preprint arXiv:2311.10537, 2023.
                                                                   R. Wang, J. Lehman, A. Rawal, J. Zhi, Y. Li, J. Clune, and
T. Taylor. Requirements for open-ended evolution in natural           K. O. Stanley. Enhanced POET: open-ended reinforce-
   and artificial systems. arXiv preprint arXiv:1507.07403,           ment learning through unbounded invention of learning
   2015.                                                              challenges and their solutions. In Proceedings of the 37th
                                                                     International Conference on Machine Learning, ICML
T. Taylor. Routes to open-endedness in evolutionary systems.         2020, 13-18 July 2020, Virtual Event, volume 119 of
   arXiv preprint arXiv:1806.01883, 2018.                            Proceedings of Machine Learning Research, pages 9940–
                                                                      9951. PMLR, 2020. URL http://proceedings.
A. M. Turner, D. Hadfield-Menell, and P. Tadepalli. Con-              mlr.press/v119/wang20l.html.
   servative agency via attainable utility preservation. In
  Proceedings of the AAAI/ACM Conference on AI, Ethics,            T. T. Wang, A. Gleave, T. Tseng, K. Pelrine, N. Bel-
   and Society, pages 385–391, 2020.                                  rose, J. Miller, M. D. Dennis, Y. Duan, V. Pogrebniak,
                                                                      S. Levine, et al. Adversarial policies beat superhuman go
F. Urbina, F. Lentzos, C. Invernizzi, and S. Ekins. Dual use          ais. In International Conference on Machine Learning,
   of artificial-intelligence-powered drug discovery. Nature          pages 35655–35739. PMLR, 2023b.
  Machine Intelligence, 4(3):189–191, 2022.
                                                                   Y. Wang, Y. Kordi, S. Mishra, A. Liu, N. A. Smith,
K. Valmeekam, M. Marquez, S. Sreedharan, and S. Kamb-                 D. Khashabi, and H. Hajishirzi. Self-instruct: Align-
   hampati. On the planning abilities of large language               ing language model with self generated instructions.
   models-a critical investigation. Advances in Neural Infor-        ArXiv preprint, abs/2212.10560, 2022. URL https:
   mation Processing Systems, 36:75993–76005, 2023.                  //arxiv.org/abs/2212.10560.

P. Villalobos, J. Sevilla, L. Heim, T. Besiroglu, M. Hobb-         Z. Wang, S. Cai, A. Liu, Y. Jin, J. Hou, B. Zhang,
   hahn, and A. Ho. Will we run out of data? An analysis of           H. Lin, Z. He, Z. Zheng, Y. Yang, X. Ma, and Y. Liang.
   the limits of scaling datasets in Machine Learning, Oct.          JARVIS-1: Open-World Multi-task Agents with Memory-
   2022.                                                             Augmented Multimodal Language Models, Nov. 2023c.

O. Vinyals, I. Babuschkin, W. M. Czarnecki, M. Mathieu,            L. Wong, G. Grand, A. K. Lew, N. D. Goodman, V. K.
  A. Dudzik, J. Chung, D. H. Choi, R. Powell, T. Ewalds,              Mansinghka, J. Andreas, and J. B. Tenenbaum. From
   P. Georgiev, J. Oh, D. Horgan, M. Kroiss, I. Danihelka,           Word Models to World Models: Translating from Natural
  A. Huang, L. Sifre, T. Cai, J. P. Agapiou, M. Jader-                Language to the Probabilistic Language of Thought, June
   berg, A. S. Vezhnevets, R. Leblond, T. Pohlen, V. Dal-             2023a.
   ibard, D. Budden, Y. Sulsky, J. Molloy, T. L. Paine,
   C. Gulcehre, Z. Wang, T. Pfaff, Y. Wu, R. Ring, D. Yo-
   gatama, D. Wu¨nsch, K. McKinney, O. Smith, T. Schaul,

                                                               16


--- page break ---

Open-Endedness is Essential for Artificial Superhuman Intelligence

M. L. Wong, C. E. Cleland, D. Arend Jr, S. Bartlett, H. J.       A. Illustrating Open-Endedness
   Cleaves, H. Demarest, A. Prabhu, J. I. Lunine, and R. M.
   Hazen. On the roles of function and selection in evolv-       A.1. An Informal Example
   ing systems. Proceedings of the National Academy of
  Sciences, 120(43):e2310223120, 2023b.                          To illustrate our definition informally, we provide a relatable
                                                                 real-world example. Let S be a research lab and the xt be
X. Wu, S.-h. Wu, J. Wu, L. Feng, and K. C. Tan. Evolu-           academic papers published by the lab. A natural choice of
   tionary computation in the era of large language model:       observer O is a research student in the field at a different
   Survey and roadmap. arXiv preprint arXiv:2401.10034,          lab. Roughly speaking, a research student sees novelty in a
   2024.                                                         line of work if, based on their knowledge of the literature up
                                                                 to time t, given any subsequent paper xT they can always
Y. Wu, S. Prabhumoye, S. Y. Min, Y. Bisk, R. Salakhutdi-         find a later paper xT ′ that is more surprising than xT . This
   nov, A. Azaria, T. Mitchell, and Y. Li. SPRING: GPT-4         is intuitively sensible, a putative student with knowledge of
   Out-performs RL Algorithms by Studying Papers and             Newtonian mechanics will find Maxwell’s equations hard
   Reasoning, May 2023.                                          to predict, quantum mechanics even more surprising, and
                                                                 contemporary particle physics very far outside their current
C. Yang, X. Wang, Y. Lu, H. Liu, Q. V. Le, D. Zhou, and          level of comprehension. A research student sees learnability
  X. Chen. Large Language Models as Optimizers, Sept.            in a line of work if they find that reading the previous papers
   2023a.                                                        helps them better to predict the contents of the current paper.
                                                                 Again, this appeals to our intuition: part of the purpose of
M. Yang, Y. Du, K. Ghasemipour, J. Tompson, D. Schuur-           citations, for instance, is to point new researchers at previous
   mans, and P. Abbeel. Learning Interactive Real-World          works that will help to deepen their understanding of the
   Simulators, Oct. 2023b.                                       current work.

W. Yuan, R. Y. Pang, K. Cho, S. Sukhbaatar, J. Xu, and           Our interpretation of “interestingness” as learnability also
  J. Weston. Self-rewarding language models. arXiv               makes sense from the perspective of a research student. A
   preprint arXiv:2401.10020, 2024.                              research student may choose to ignore a paper’s choice of
                                                                 font, but will likely pay close attention to the details of a
J. Zhang, J. Lehman, K. Stanley, and J. Clune. OMNI:             novel method that yields state-of-the-art results. Thus the
   Open-endedness via Models of human Notions of Inter-          student finds interesting the parts of the paper from which
   estingness, June 2023.                                        they can learn the most. Similarly, the requirement that
                                                                 the loss metric ℓ be chosen without knowledge of S finds a
B. Zheng, B. Gou, J. Kil, H. Sun, and Y. Su. GPT-4V(ision)       natural interpretation here. A research student cannot judge
   is a Generalist Web Agent, if Grounded, Jan. 2024.            the open-endedness of a stack of papers by choosing to
                                                                 never read the papers and instead inventing their own line
S. Zhou, F. F. Xu, H. Zhu, X. Zhou, R. Lo, A. Srid-              of research with no reference to previous works.
   har, X. Cheng, T. Ou, Y. Bisk, D. Fried, U. Alon, and
   G. Neubig. Webarena: A realistic web environment for          A.2. Definitional Subtleties
   building autonomous agents. In Second Agent Learn-
   ing in Open-Endedness Workshop, 2023. URL https:              Self-play illustrates some subtleties in our definition. The
  //openreview.net/forum?id=rmiwIL98uQ.                          first subtlety is the dependence of open-endedness on the
                                                                 choice of observer. Suppose that O is an oracle who knows
D. M. Ziegler, N. Stiennon, J. Wu, T. B. Brown, A. Radford,      the Nash strategy to play in Go. Assuming that the oracle
   D. Amodei, P. Christiano, and G. Irving. Fine-tuning          is modelling the win-rate of AlphaZero’s artifacts against
   language models from human preferences. ArXiv preprint,       its own policy, it will never find any AlphaZero policy to
   abs/1909.08593, 2019. URL https://arxiv.org/                  be novel. Therefore the oracle does not find AlphaZero to
   abs/1909.08593.                                               be open-ended. The second subtlety is the dependence of
                                                                 open-endedness on the learning limitations of the observer.
                                                                 To an average human Go player, as opposed to an expert,
                                                                 AlphaZero becomes novel earlier in training, and at some
                                                                 point ceases to be learnable, because the average player
                                                                 cannot figure out how to improve their own play with ref-
                                                                 erence to very unusual style of a superhuman policy. Thus,
                                                                 open-ended systems only remain open-ended while they
                                                                 can “educate” their observers. We posit that superhuman
                                                                 intelligence will be interesting to humans only as far as

                                                             17


--- page break ---

Open-Endedness is Essential for Artificial Superhuman Intelligence

humans can learn to understand it. The third subtlety is             ciple, there is nothing in our definition that rules out self-
that open-ended systems need not explore a problem space             observing open-ended systems. For example, an individual
fully to qualify as open-ended. Recently, adversarial search         self-improving agent could generate a series of artifacts,
was shown to yield policies that beat reimplementations              each one of which is novel (surprising compared to the pre-
of AlphaZero and which are so simple that even amateur               vious artifacts) and learnable (increasingly predictable given
humans can learn them (Wang et al., 2023b). Novelty and              the more history of the past artifacts). When the feedback
learnability give no guarantee of coverage.                          from self-observation is used to improve the system itself,
                                                                     we call the observer a proxy observer for it no longer sits
Because our definition is based on the perspective of an             outside the system.
external observer, one could worry that this makes it impos-
sible to make any sort of objective claims about the open-           For example, AlphaGo can be seen as an example of a self-
endedness of any particular system, in harmony with the              observing system, in that the agent trains in self-play i.e. it
arguments of Stanley and Soros (2016); Stepney and Hick-             observes its own policy as an opponent, is challenged by
inbotham (2023). There are two factors which mitigate this           the novel discoveries of search, and learns from them to im-
concern. Firstly, the definition of open-endedness becomes           prove the policy. Likewise, humans can experience “Eureka
objective given any fixed observer, and so it becomes a mea-         moments”, when an individual suddenly reconceptualizes
surable claim, in the sense that theorems can be written and         a problem in a ways that yields a solution (Sternberg and
experiments conducted. For instance, if we care about open-          Davidson, 1995). A series of Eureka moments, each build-
endedness with respect to humans, open-endedness can be              ing on the last, is a self-observing open-ended system: the
measured experimentally by how well humans can predict               human generates discoveries which are novel to themselves,
the system. By having observer-dependence explicit in our            but which are also predictive of the next discovery.
definition, we make precise the intuition that different ob-
servers, with different prior knowledge, different cognitive         Our notions of learnability is rather strict, in that it requires
capabilities and different timescales, are likely to judge the       that the loss be decreasing for all t′ > t. A weaker and more
same system in different ways. Thus our definition grace-            practical notion of learnability might state that it should
fully encompasses the diversity in perspectives of human             be probabilistically unlikely that the loss will increase as a
individuals and groups (such as companies or governments),           function of t:
as well as the possibility that AI systems themselves could
be observers.                                                          ∀T, ∀t < T, ∀T > t′ > t : P (ℓ(t′, T ) ≥ ℓ(t, T )) < δ .

Secondly, while our definition of open-endedness depends             It would be interesting to compare the consequences of
on an external observer, it is an open question as to whether        δ being a constant with the situation in which δ has some
all “reasonable” observers would judge the same systems to           appropriate dependence on the variables (t, t′, T ). Similarly,
be open-ended. Since our definition rests on a notion of pre-        one could weaken the notion of novelty to state that it should
dictability with respect to the observer, our definition will        be probabilistically unlikely that the loss will decrease as a
be as subjective as the underlying notion of predictability.         function of T . We believe that there may be several related
One may believe that predictability can be accurately and            and differently useful variants on our definition that would
objectively modeled as Solomonoff induction (Solomonoff,             be interesting to independently study, in a similar way that
1960). Thus if reasonable observers are taken to be those            there are many notions of convergence which are interesting,
whose predictions eventually follow something approximat-            related, and differently useful.
ing Solomonoff induction, then any observer in this class
would eventually agree on which systems are open-ended.              B. Alternative Definition

Practically speaking, there are various existing methods in          In Section 2.1 we provided a formal definition of open-
the literature which can immediately be adapted to assess            endedness in the language of statistical learning. Here we
the open-endedness of a system. First, one might elicit direct       give an alternative definition which we conjecture is equiva-
human feedback on learnability and novelty of artifacts, in          lent under appropriate conditions. The alternative definition
the same spirit as RLHF (Ouyang et al., 2022) or PicBreeder          is phrased in the language of compression, a topic with
(Secretan et al., 2008). Second, one can use large language          known formal connections to statistical learning (Hutter,
models themselves as judges of novelty and learnability, as          2004; David et al., 2016; Campi and Garatti, 2023; Dele´tang
argued for in OMNI (Zhang et al., 2023). Finally, one could          et al., 2023).
explicitly learn a model of the artifacts with an online learn-
ing method like Follow-the-Regularized-Leader (Hazan and             A system S produces a sequence of artifacts Xt ∈ X ,
Kale, 2010).                                                         indexed by time t. An observer O processes a new artifact
                                                                     XT to determine its information content given a history
Can an open-ended system be its own observer? In prin-               ht = X1:t of past ones. O possesses a history-dependent

                                                                 18


--- page break ---

Open-Endedness is Essential for Artificial Superhuman Intelligence

compression map Cht : X → {0, 1}∗ which encodes XT                    Figure 3. Open-endedness through the lens of rate-distortion
into a binary string of length |Cht (XT )|.                           curves. We depict part of the upper triangular matrix of rate-
                                                                      distortion curves GtT induced an observer after seeing the first t
The system displays novelty if the information content in-            artifacts aiming to lossily compress future artifact T . Here t =
creases, namely:                                                      2, 3, 4 and T = 5, 6, 7. Broad novelty is the property that, as you
                                                                      move from left to right in any fixed row, the rate-distortion curves
     ∀t, ∀T > t, ∃T ′ > T : |Cht (XT ′ )| > |Cht (XT )|.              become fatter. Broad learnability is the property that, as you move
                                                                      from top to bottom in any fixed column, the curves become flatter.
In other words, the complexity of the artifacts grows, ac-            For the system to be broadly open-ended, both properties must
cording to the observer.                                              hold.

The system is learnable if conditioning on a longer history           C. Further Related Work
increases compressibility, namely:
                                                                      Open-endedeness as a term emerged from the AI Life com-
   ∀T, ∀t < T, ∀T > t′ > t : |Cht′ (XT )| < |Cht (XT )|.              munity when trying to quantify and replicate the increasing
                                                                      complexity and perpetual novelty of biological evolution.
In other words, as its history grows, the observer must be            This is a rich field with a significant degree of disagreement
able to keep extracting additional patterns that help it com-         (Earle et al., 2021). As such there are a wide range of met-
press future artifacts.                                               rics proposed within the context of evolutionary systems
                                                                      which aim to quantify it’s behavior. For instance persistence
Finally, a system is open-ended from the perspective of O             filtering, which measures how many generations an organ-
if and only if it generates sequences of artifacts that are both      ism has persisted for (Dolson et al., 2019), and evolutionary
novel and learnable.                                                  activity statistics (Bedau et al., 1997; 1998). The closely
                                                                      related question around the necessary conditions to produce
We allow for the compression map Cht to be lossy. Hence,              open-ended evolution has also been deeply studied (Taylor,
O also possesses a decompression map Dht : {0, 1}∗ → X ,              2018; 2015). As these definitions are largely specific to bio-
a symmetric loss function ℓ : X × X → R+, and a threshold             logical evolution, we focus the remainder of our discussion
ϵ ∈ R+ that upper-bounds the error made by by Cht :                   on the more recent definitions which aim to define open-
                                                                      ended systems in a way that applies to current ML systems
          ∀T, ∀t < T : ℓ(Dht (Cht (XT )), XT ) < ϵ.                   and systems more broadly.

We can strengthen the definition to be independent of ϵ by            Our definition of open-endedness is closely related to the
appealing to rate-distortion theory. A rate-distortion curve          concept of potential surprise in economics (Shackle, 1949).
plots the the minimum information content |Ch(X)| such                To measure potential surprise, an individual should ask:
that ℓ(Dh(Ch(X)), X) < ϵ against ϵ, where the minimum                 “how surprised would I be if this outcome actually occurred,
is over the maps Ch and Dh. The information content is                if, at the time it occurred, I were still looking at the world in
referred to as the rate and ϵ is referred to as the distortion.       the way I look at it right now?” (Derbyshire, 2017). Inter-
Picture a grid of rate-distortion curves GtT indexed by (dis-         preting surprise as unpredictability under a statistical model,
cretized) t and T , as in Figure 3. Remember that T > t,              an open-ended system S is precisely one which produces
so GtT is strictly upper triangular, with other entries be-           ever increasing “Shackle surprise” in an observer which is
ing undefined. Then broad novelty is the requirement that             learning. The concept of potential surprise is itself based
the curves get “fatter” as you move across the columns T              on the century-old idea of Knightian uncertainty (Knight,
on the grid, for every row t. Similarly, broad learnabil-
ity is the requirement that the curves get “flatter” as you
move down the rows t on the grid, for every column T .
Broad open-endedness is the requirement that both broad
novelty and broad learnability hold. This notion of broad
open-endedness is vague in the same way the notion of
“convergence” is vague in that it can be made precise in
many subtly different but connected ways. For instance,
one could say a system is “uniformly” open-ended if dis-
tortion increases across the rows and decreases down the
columns for every rate ϵ. Alternatively, one could define
“average” open-endedness by requiring that the integral of
the rate-distortion curve get larger as you move across the
columns and smaller as you move down the rows. We hope
that future work will elucidate these subtleties in defining
broad open-endedness and determine which variants have
theoretical or practical merit.

                                                                  19


--- page break ---

Open-Endedness is Essential for Artificial Superhuman Intelligence

1921). Knightian uncertainty is a lack of any quantifiable            and ASI. A construction of a particular open-ended learn-
knowledge about some possible occurrence, as opposed                  ing system is provided in (Jiang et al., 2022), which may
to the presence of quantifiable risk. Thus, somewhat im-              or may not fit our proposed definition of an open-ended
precisely, an open-ended system S is one which induces                system depending on how it is instantiated. The system
Knightian uncertainty in an observer who is learning.                 generates Turing machine descriptions of MDPs, explicitly
                                                                      optimizing for an objective containing terms for learning
In Stanley and Lehman (2015), the authors argue that local            potential, diversity, and grounding. These terms have some
search for novel and interesting artifacts can be advanta-            high-level relation to our notions of learnability and novelty,
geous over optimization for a global objective. This is be-           but they are quite distinct in the details. For instance, learn-
cause stepping stones towards a solution that optimizes the           ing potential is divided into three sub-critia, improbability,
global objective may well not resemble the solution itself.           learnability, and consistency, which are not made entirely
Hence it is hard to translate the global objective into a local       formal. More crucially, the learnability discussed by (Jiang
improvement operator that reliably accumulates improve-               et al., 2022) is a property of a single MDP, whereas the
ments without getting stuck in local optima. To address this          learnability we define is a property of a sequence of artifacts.
deceptiveness, they suggest that novelty search (Lehman               Similarly, in (Jiang et al., 2022) diversity is defined as a
and Stanley, 2011), guided by a notion of interestingness,            distance measure between MDPs, whereas novelty, as we
can uncover stepping stones that advance knowledge and                define it, is a property of the learning of the observer with no
capability. We take inspiration from this blueprint and turn          necessary relationship to distances in the space of artifacts.
it into a definition. In order to clarify the notions of nov-         It would be an interesting direction for future research to
elty and interestingness, we formalize them with respect              understand under what conditions the system described in
to an external observer. Novelty becomes unpredictability             (Jiang et al., 2022) would be open-ended by our definition,
according to the observer’s history-conditional model, and            and, more generally, whether one can directly optimize for
interestingness becomes learnability of that model across             open-endedness in some circumstances.
the history of observations.
                                                                      Open-endedness is related to, but separate from, the no-
Our definition naturally relates to the notion of curiosity. Cu-      tion of an AI-generating algorithm (AIGA, Clune, 2020).
riosity, implemented as prediction error of a world model,            An AIGA automatically learns how to build a general AI,
has long been mooted as an intrinsic motivation that can lead         based on meta-learning model architectures, meta-learning
to open-ended discovery in RL agents given a sufficiently             learning algorithms, and automatically generating data from
rich environment space (Schmidhuber, 1991b; Pathak et al.,            which to learn. Adapting the logic of Clune (2020), an
2017; Raileanu and Rockta¨schel, 2020; Henaff et al., 2023).          AIGA need not be open-ended by our definition; if an
Our definition of novelty is effectively a generalisation of          AIGA had the objective of passing a Turing test, it need
curiosity, without requiring an overarching RL framework.             not produce any further novelty once this objective had
Our requirement of learnability ensures that the observer             been achieved. Likewise, an open-ended system need not
attempts to capture all the epistemic uncertainty about the ar-       be an AIGA; as we shall see in Section 2.4, there exist
tifacts produced by a system. One challenge is that curiosity         open-ended systems with narrow scope that match or ex-
based on novelty alone leads to “stochastic traps”, whereby           ceed human ability without full domain-generality. Our idea
an agent will seek out sources of random noise with which             of an Open-Ended Foundation Model in Section 3 lives at
to sate its curiosity (Schmidhuber, 1991a; Burda et al., 2018;        the intersection between open-endedness and AIGAs.
Shyam et al., 2019). In principle, our definition of novelty
collapses such aleatoric uncertainty by taking the expecta-           Similarly open-endedness is related to, but distinct from,
tion. In practice, we can only estimate the expectation, so it        continual RL (Abel et al., 2023). A continual RL problem is
may be useful to subtract from the loss an estimate of the            one in which the best agents never stop learning. However,
aleatoric uncertainty as in Mavor-Parker et al. (2022). We            as observed by (Sigaud et al., 2023), this does not neces-
hope that future work will examine such subtleties required           sarily imply that the agent policies accumulate increasing
for an algorithmic implementation of our definition.                  novelty. Rather, a continual RL agent could cycle among
                                                                      some set of strategies. In the case where continual RL does
The synergies between foundation models and open-                     produce policies which are open-ended according to some
endedness have previously been discussed by Jiang et al.              observer, this open-endedness will have a scope that is re-
(2022). The authors propose a general notion of exploration           stricted by the environment.
and detail how open-endedness can be used to solve explo-
ration problems when training foundation models. Our work
follows in this line of thinking, providing a formal definition
of open-endedness to make the discussion precise, and fur-
ther developing the connections between open-endedness

                                                                  20


--- page break ---
