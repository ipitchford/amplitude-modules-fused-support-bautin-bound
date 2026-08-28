# Stage 2 novelty audit: three headline results and one supporting bridge

**Audit date:** 28 August 2026  
**Audit type:** bounded primary-source comparison  
**Status:** bounded candidate novelty only; no priority, independent specialist
review or peer-review claim is made.  This audit does not itself authorize
publication.

## Audit question

For each proposed theorem, what exact claim survives comparison with the
closest primary literature inspected by this programme?

This is a subtraction audit.  It does not ask whether the surrounding subject
is old or new.  It records which tempting claims are already supported by
prior work and states the narrower residual contribution that may still merit
publication.

The audit is relative to the sources and searches listed below.  It is not a
systematic review, and absence from those searches is not proof of novelty.

## Executive disposition

| Result | Residual contribution permitted by this audit | Disposition |
|---|---|---|
| A. Dickson amplitudes | All-degree free-module decomposition for arbitrary polynomial primitives and the exact formula \(q=2N+\varepsilon\), including the parity-dependent attainable-rank classification | **BOUNDED_UNCERTAINTY** |
| B. Exceptional Ritt amplitudes | The explicit five-summand amplitude module for \(P=(x^4+x)^3\), its correction coefficients, support partition and exact rank formula for every polynomial primitive | **BOUNDED_UNCERTAINTY; STRONGEST RESIDUAL UNIT** |
| C. Uniform zero-cycle Bautin bound | Ordinary parameter-content stabilization \(\mathcal B_\infty=\mathcal B_{d-1}\) for every degree-\(d\) phase, every cycle and every polynomial perturbation; hence \(b_{\mathrm{coeff}}(m)\le m-1\), conditionally identifying the source's \(b(m)\) | **BOUNDED_UNCERTAINTY; FULL DEGREE-BOX CANDIDATE** |
| Bridge. Weighted period order | The identity between inverse support/root span and exact complete-system minimal order, the standard-ray touched-channel/block bounds, and a reproducible standalone certificate benchmark | **BRIDGE; ALGORITHM COLLIDES WITH PRIOR ART** |

The present evidence supports one integrated paper rather than three
independent priority claims.

## Companion-note disposition

A user-supplied note proposed a general monodromy-block theorem, a
cycle-specific active-channel order formula, and a binomial Laurent
classification; a second version supplied by the user attempts repairs.

- A corrected block theorem is incorporated as an organizing result.  It is a
  concise consequence of multiplicity-free monodromy plus the reconstructed
  root-span/support theorem, with central projectors supplying polynomial
  module descent.  Its novelty has not been separately established.
- The original cycle-specific equality is excluded because an isolated
  \(D_3\) residue gives a non-half-integer modified Bessel solution of
  minimal order two, not the predicted order one.  The second note correctly
  replaces it with lower channel-count and upper block-mass bounds.  Those
  bounds are retained
  for the standard ray-cycle system using the reconstructed
  Fourier--Gamma/formal-monodromy argument.  Their historical novelty has not
  been separately established.
- The binomial Laurent classification is included only as a contextual
  corollary.  Pakovich's 2013 theorem already supplies the
  doubly-transitive classification, and the remaining deck grading is also
  explicitly anticipated there.

The detailed correctness audits are retained in ATTACHMENT_AUDIT.md and
ATTACHMENT_2_AGREEMENT_AUDIT.md.

## Corpus and search protocol

The load-bearing comparison corpus consists of frozen source responses recorded
in SOURCE_PROVENANCE.json:

1. Pakovich--Muzychuk, *Solution of the polynomial moment problem*,
   arXiv:0710.4085v2.
2. Pakovich, *On polynomials orthogonal to all powers of a Chebyshev
   polynomial on a segment*, arXiv:math/0212040.
3. Gavrilov--Pakovich, *Moments on Riemann surfaces and hyperelliptic Abelian
   integrals*, arXiv:1107.3029v1.
4. Alvarez Sanchez--Bravo Trinidad--Mardesic, *Vanishing Abelian integrals on
   zero-dimensional cycles*, arXiv:1101.1777v2.
5. Behajaina--Konig--Neftin, *Monodromy groups of polynomials of composition
   length 2*, arXiv:2603.27609v2.
6. Charbonnier--Chidambaram--Garcia-Failde--Giacchetto, *Shifted Witten
   classes and topological recursion*, arXiv:2203.16523v2.
7. Fantini--Fenyes, *The Regularity of ODEs and Thimble Integrals with Respect
   to Borel Summation*, arXiv:2407.01412v4.
8. Bostan--Chen--Chyzak--Li--Xin, *Hermite Reduction and Creative Telescoping
   for Hyperexponential Functions*, arXiv:1301.5038v1.
9. Hien--Roucairol, *Integral representations for solutions of exponential
   Gauss--Manin systems*, arXiv:0704.1739v1.  The local e-print response did not
   extract; only the authoritative arXiv abstract-page claim was used.
10. Pakovich, *On rational functions orthogonal to all powers of a given
   rational function on a curve*, arXiv:0910.2105v1, including its
   doubly-transitive Laurent-moment theorem.
11. Hien, *Periods for flat algebraic connections*, arXiv:0803.3463v1,
    especially the perfect period pairing in Theorem 5.2.
12. Bravo--Mardešić--Novikov--Pontigo-Herrera, *Infinitesimal and tangential
    16-th Hilbert problem on zero-cycles*, arXiv:2312.03081v1, including its
    concluding Bautin-index problem.
13. Álvarez--Bravo--Christopher--Mardešić, *Infinitesimal Center Problem on
    zero cycles and the composition conjecture*, arXiv:2006.07600v1.
14. Batenkov--Yomdin, *Taylor Domination, Difference Equations, and Bautin
    Ideals*, arXiv:1411.7629v1.
15. Batenkov--Binyamini, *Uniform upper bounds for the cyclicity of the zero
    solution of the Abel differential equation*, arXiv:1504.02208v1.
16. Briskin--Yomdin, *Algebraic Families of Analytic Functions, I*,
    Journal of Differential Equations 136 (1997), 248--267.

The earlier Stage 1 comparison also retained Chen--Kauers
(arXiv:1108.4508), Bostan--Lairez--Salvy (arXiv:1301.4313), the trigonometric
moment paper (arXiv:1108.0172v2) and the Laurent case study
(arXiv:0910.2691v1).

On 27 August 2026, bounded public-web exact-phrase searches were also run for
the three exceptional generators

\[
x^7+\tfrac74x^4,\qquad
x^{10}-\tfrac52x^4,\qquad
x^{11}+\tfrac{11}{4}x^8
\]

and for the displayed Dickson module/rank formula.  No exact scholarly match
was located.  Search-engine coverage, indexing lag, notation changes,
non-English literature and inaccessible material remain blind spots.

A fresh same-day pass also queried arXiv-focused combinations of “polynomial
exponential periods”, “Dickson polynomial”, “amplitude cyclic rank”,
“primitive-amplitude support”, “twisted de Rham”, and “inverse Puiseux
support”, followed by exact-web searches for the displayed rank notation,
the coefficient \(x^7+\tfrac74x^4\), “support-predicted period operator”, and
“polynomial-amplitude support theorem”.  The only exact topical hit for the
new terminology was the Atlas itself; the remaining returns were unrelated
uses of Dickson polynomials, support prediction, or de Rham rank.  This
narrows the indexed-web collision risk but does not extend the audit to
MathSciNet, zbMATH, inaccessible journals, or specialist knowledge.

The formula-first follow-up is recorded in `NOVELTY_GATE_REPORT.md`. It also
inspected Pakovich's 2004 Chebyshev moment theorem from frozen primary source.
That theorem is a close antecedent: for fixed endpoints it gives a Chebyshev-
derivative basis for the amplitudes whose moments all vanish, and it uses the
same inverse-branch/Puiseux/dihedral ingredients. It does not state the
complete-system cyclic rank for every amplitude, the paired
\(\mathbf C[T_n]\)-module formula, or \(q=2N+\varepsilon\). Its proximity is
why Result A is now classified as bounded uncertainty rather than established
novelty.

## Result A: Dickson amplitude modules

### Claims removed by prior art

Pakovich--Muzychuk explicitly expands \(Q(P_i^{-1}(z))\) as Puiseux series,
turns linear root-value relations into Fourier-vector constraints, separates
series by disjoint support, and uses those supports to obtain composition
decompositions.  Consequently, inverse-at-infinity support separation, Fourier
residue bookkeeping and its connection with polynomial decomposition are not
new methods here.

The zero-dimensional Abelian-integral literature likewise treats monodromy
orbits, irreducible permutation subspaces and Puiseux expansions.  Those
ingredients cannot be advertised as newly introduced by Result A.

For Chebyshev-normalised Dickson phases, individual Lucas/Chebyshev amplitudes
already occur in exponential thimble integrals.  Charbonnier et al. construct
Airy--Lucas integrals with a Lucas amplitude and derive a second-order
differential equation.  Fantini--Fenyes identify integrals

\[
\int_{\mathcal C} e^{zT_n(u)}U_{m-1}(u)\,du
\]

with rational-parameter modified Bessel functions.  Thus the special-function
identity for a single generator, and the fact that its period can have order
two, are prior art.

### Residual claim

The claim not located in the audited literature is the simultaneous
classification for every polynomial primitive:

\[
G=H_0(D_d)+
\sum_{1\le j<d/2}
\bigl(H_j(D_d)D_j+K_j(D_d)D_{d-j}\bigr)
+\mathbf 1_{2\mid d}H_{d/2}(D_d),
\]

with exact induced rank

\[
q(D_d,G'\,dx)=2N(G)+\varepsilon(G).
\]

The residual candidate contribution includes the fact that odd \(d\) admits only the
even ranks \(0,2,\ldots,d-1\), whereas even \(d\) admits every rank from
\(0\) to \(d-1\).  This parity correction supersedes the broader Stage 1
wording that every bounded rank occurs in every degree.

### Claim ceiling

Result A may be described as a candidate all-amplitude module classification
not located in the bounded search, using the reconstructed support theorem.
It may not be
described as the discovery of the Puiseux/Fourier method, of the
Chebyshev--Bessel integral, or of second-order equations for individual
Lucas amplitudes.

## Result B: exceptional Ritt-fusion amplitudes

### Claims removed by prior art

The use of full symmetric monodromy and its irreducible standard
representation is well established in the zero-dimensional Abelian-integral
literature.  Gavrilov--Pakovich explicitly formulate vanishing through
irreducible monodromy subspaces, and Alvarez Sanchez et al. use transposition
branch cycles and connected chains of transpositions.

More decisively, Behajaina--Konig--Neftin treat the exact collision

\[
(X^3+1)^3X^3=X^3\circ((X^3+1)X)
\]

and identify its monodromy group as \(S_4\times C_3\).  Since
\((X^3+1)X=X^4+X\), this is precisely the phase
\(P=(x^4+x)^3\).  The monodromy group, the Ritt-move nature of the collision,
and the existence of its \(S_4\) factor are therefore direct recent prior art.

### Residual claim

The exact amplitude classification not located in the audited sources is

\[
\mathbf C[x]=\mathbf C[Q]\oplus M_0\oplus M_1\oplus M_2
\quad\text{over }\mathbf C[P],
\]

where \(Q=x^4+x\) and

\[
\begin{aligned}
M_0&=\langle x,\ x^7+\tfrac74x^4,\ x^{10}-\tfrac52x^4\rangle,\\
M_1&=\langle x^2,\ x^5,\ x^{11}+\tfrac{11}{4}x^8\rangle,\\
M_2&=\langle x^3,\ x^6,\ x^9\rangle.
\end{aligned}
\]

For the unique decomposition

\[
G=A_0(P)+A_1(P)Q+A_2(P)Q^2+m_0+m_1+m_2,
\]

the residual theorem asserts

\[
q(P,G'\,dx)=
\mathbf1_{A_1\ne0}+\mathbf1_{A_2\ne0}
+3\sum_{i=0}^2\mathbf1_{m_i\ne0},
\]

with the five disjoint support sets

\[
\{4\},\quad\{8\},\quad
\{1,7,10\},\quad\{2,5,11\},\quad\{3,6,9\}.
\]

The novelty candidate is the amplitude module, its correction coefficients,
and its all-amplitude rank formula—not the monodromy classification used to
prove it.

### Claim ceiling

Result B may be described as a candidate explicit amplitude-module theorem for
a known exceptional Ritt collision.  The 2026 monodromy paper must be cited
prominently, and no priority claim may be made for the group-theoretic
identification.

## Result C: full-degree zero-cycle coefficient Bautin bound

### Claims removed or limited by prior art and scope

Bravo--Mardešić--Novikov--Pontigo-Herrera explicitly pose the uniform
zero-cycle Bautin-index problem.  This supplies the external target but not
the result.  Their wording permits \(\deg f<\deg g\le m\), and the revised
candidate proof covers that range because reduction modulo \(f-t\) gives a
rank-\(d\) algebra for every finite perturbation degree.

Batenkov--Yomdin prove a general theorem that a polynomial sequence generated
by a recurrence of length (d) has Bautin ideal generated by its first (d)
entries.  Consequently, the abstract recurrence-to-ideal principle is prior
art.  Batenkov--Binyamini study a different Abel-equation moment Bautin index
and do not state the zero-cycle Melnikov bound.

### Residual claim

For fixed monic (f) of degree (d), any zero-cycle (C), and a complete
polynomial perturbation family of arbitrary fixed degree, define the ordinary
ideal generated by
the perturbation-parameter content of the first (k) Melnikov coefficients.
The candidate result is

\[
\mathcal B_\infty=\mathcal B_{d-1}.
\]

The Melnikov sequence is not the undifferentiated moment recurrence covered
directly by the 2014 theorem: its \(\mu\)-th term is

\[
M_\mu=\frac{(-1)^\mu}{\mu!}D_t^{\mu-1}\int_Cg^\mu.
\]

The residual mechanism is that differentiation is injective on zero-cycle
polynomial integrals.  Infinity monodromy averages any single-valued such
integral over a zero orbit cycle, forcing it to vanish.  Differentiation
therefore preserves parameter content exactly, and the undifferentiated
Cayley--Hamilton recurrence transfers to all Melnikov coefficients without a
degree restriction on (g).

The bound is sharp after complex scalar extension of cycles.  For integer
cycles, only the explicit lower witness (d/p), with (p) the least prime
divisor, is claimed.

### Claim ceiling

Result C may be described as the ordinary Taylor-coefficient theorem
\(b_{\mathrm{coeff}}(m)\le m-1\).  Proposition 6.1 proves that this ideal
equals parameter content.  It answers the 2025 degree-box problem only if the
source's terse \(b(m)\) uses that convention, and must not be described as
settling alternative analytic-function-ring, pre-contraction radical, or
singular-base-point conventions.

## Supporting bridge: support-predicted minimal weighted operators

### Claims removed by prior art

Hien--Roucairol establish rapid-decay period-integral representations for
solutions of exponential Gauss--Manin systems, and Hien's Theorem 5.2 proves
the perfect algebraic de Rham/rapid-decay homology pairing used for
complete-system minimality.  The general relationship between exponential
periods and differential systems, including the perfectness input, is
therefore not new.

Bostan et al. give a reduction algorithm for hyperexponential functions,
define residual forms, prove that their first linear dependence produces a
minimal telescoper, and provide an order bound.  Chen--Kauers and
Bostan--Lairez--Salvy supply additional order-aware and reduction-based
creative-telescoping antecedents.  Therefore:

- quotient reduction modulo total derivatives is prior art;
- taking the first Krylov/residual dependence is prior art;
- minimal telescoper construction is prior art; and
- certificate production and order bounds are prior art.

The standalone implementation in this workspace is a reconstruction and
benchmark, not a new algorithmic paradigm.

### Residual claim

Using the reconstructed support theorem, the candidate contribution is the
specific bridge

\[
\operatorname{ord}_{\min}(P,A)
=q(P,G'\,dx)
=|\Sigma(P;G)|
=\dim\operatorname{span}_{\mathrm{red}}\{G(x_i)\},
\qquad G'=A,
\]

for the complete rapid-decay period system, together with a direct exact
reducer, primitive operator normalization and replayable residual certificate.

For a standard ray-cycle with touched channel set \(R\), the repaired companion
result retains only the derived standard-ray bound

\[
|R|\le\operatorname{ord}_{\min}(I_n)
\le\sum_{B\cap R\ne\varnothing}|B|\le q(P,G'\,dx),
\]

No general exact Dickson block-mass equality is retained: it was demoted because
the required scalar differential-module derivation is incomplete.  The
two-sided standard-ray bound has not received a separate priority search and is
not presented as a fourth novelty claim.

This predicts the complete-system minimal order from inverse support or
reduced root values before the dependence computation.  A specified
ray-cycle is governed only by the stated bounds unless a sharpness
criterion applies; no generic-individual-period minimality claim is made.
Rank zero means every period vanishes and is represented by the equation
\(I=0\).

### Claim ceiling

The weighted-order result is publishable only as an Atlas-derived bridge and
exact benchmark accompanying Results A--C.  It must not be titled or described
as a new creative-telescoping algorithm.

## Publication decision

The bounded audit supports continued manuscript development under the title

> **Amplitude modules, fused support, and a coefficient-Bautin bound for
> polynomial phases**

The paper should present:

1. Result A as an all-degree structural theorem;
2. Result B as an explicit exceptional-collision theorem; and
3. Result C as a uniform ordinary coefficient Bautin bound for the full
   degree box.

The weighted-order construction should remain the effective bridge,
certificate consequence and reproducibility layer.

This audit does not itself make the paper publication-ready.  An Evidence Press
release may make only an explicitly anonymous unrefereed candidate available,
and only after:

- the internal model-mediated editorial gate returns `PASS` or
  `PASS_WITH_NOTES` on repaired, frozen bytes;
- the ordinary and optimized replay, negative controls, PDF checks and
  immutable manifests pass on those same bytes;
- the licence and venue decisions are recorded; and
- the user separately authorizes publication.

Independent human specialist review of the reconstructed support theorem and
complete proofs, together with an expanded specialist priority search, remain
unresolved.  They are required for any upgrade to specialist-review, priority,
peer-review or stronger assurance status; neither internal model-mediated
editorial review nor candidate release satisfies them.

## Assurance statement

The current evidence distinguishes:

1. exact symbolic checks and deterministic replay;
2. written proof arguments;
3. a second implementation produced within the same programme;
4. internal model-mediated adversarial and editorial review;
5. independent external reconstruction or review;
6. novelty assessment;
7. peer review; and
8. public release.

Items 1--4 are presently available only within the same programme.  This audit
advances item 6 only in a bounded, candidate sense and does not imply item 5 or
7.  Item 8, if separately authorized and completed, would establish public
availability only; it would not upgrade items 5--7.
