# Formula-first novelty gate

**Gate date:** 27 August 2026  
**Scope:** four frozen contribution units in `NOVELTY_GATE_TARGETS.yaml`  
**Decision ceiling:** bounded public-corpus assessment; no absolute priority claim

## 1. Method and corpus boundary

This gate compares normalized mathematical statements, not titles or prose.
For each target it records exact formula fingerprints, small instances,
cross-disciplinary aliases, and the closest primary sources found. A failed
search is evidence only about the searched corpus.

The inspected corpus comprised frozen arXiv sources listed in
`SOURCE_PROVENANCE.json`, same-day arXiv-focused and public-web searches,
Crossref/publisher metadata reached through those searches, and attempted
zbMATH Open exact-topic searches. Search-engine routing to zbMATH was noisy
and did not produce a reliable direct result set. MathSciNet, comprehensive
non-English literature, inaccessible full text, unpublished work, and
specialist knowledge remain outside the gate.

The allowed unit outcomes are:

- **COLLISION:** the unit is already stated or directly implied in prior art;
- **BRIDGE:** known ingredients are joined by a residual statement not found;
- **BOUNDED UNCERTAINTY:** no collision was found, but the corpus is not
  sufficient for a priority claim;
- **CLEAR TO PROVE:** no collision was found after a sufficiently strong
  search boundary; and
- **STOP:** the candidate should not proceed as a novelty claim.

No target below receives an absolute `CLEAR TO PROVE` disposition.

## 2. Search log

### 2.1 Dickson/Chebyshev all-amplitude rank

Formula and alias queries included combinations of:

- `q(D_d`, `2N`, `epsilon`, Dickson polynomial and amplitude;
- `C[D_d]` module, paired residues, dihedral permutation module;
- Chebyshev phase, cyclic rank, exponential integral, twisted de Rham;
- zero-dimensional Abelian integral, inverse Puiseux support; and
- attainable-rank sequences for degrees three through nine.

The exact residual formula and rank sequences produced no independent
scholarly match. The originating Atlas and its fixed-seed predecessor were
excluded as independent novelty evidence.

The closest additional primary source was F. Pakovich, *On polynomials
orthogonal to all powers of a Chebyshev polynomial on a segment*,
arXiv:math/0212040. Its theorem says that, for fixed endpoints
`a,b` with `T_n(a)=T_n(b)`, the derivatives `T_m'` satisfying the displayed
gcd endpoint condition form a basis of the moment-vanishing space
`V(T_n,a,b)`. Its proof uses Chebyshev expansions, inverse branches,
Puiseux series and dihedral monodromy.

This is a close structural antecedent but not the frozen target. It fixes one
segment and classifies amplitudes whose entire moment sequence vanishes.
The target ranges over every polynomial primitive, takes the complete
rapid-decay period system, and computes its cyclic rank by active paired
residue blocks. Pakovich's theorem neither states the free
`C[T_n]` all-amplitude decomposition in the target normalization nor the
formula `q=2N+epsilon` or its attainable-rank parity consequence.

### 2.2 Exceptional Ritt amplitude module

Exact formula queries included:

- `x^7+7x^4/4`, `4x^7+7x^4`;
- `x^10-5x^4/2`, `2x^10-5x^4`;
- `x^11+11x^8/4`, `4x^11+11x^8`;
- `(x^4+x)^3` with amplitude, module, Abelian integral and support; and
- `S4 x C3`, standard representation, Ritt collision and polynomial
  monodromy.

No exact scholarly match was found for the three corrected generators, the
five support blocks, or the all-amplitude rank formula. Behajaina--Konig--
Neftin is a direct collision for the phase's Ritt structure and monodromy
group: the normalized collision `(X^3+1)^3 X^3` is the same degree-twelve
phase and has monodromy `S_4 x C_3`. The general use of monodromy
subrepresentations and zero-dimensional Abelian integrals also collides with
the older literature.

The residual unit is therefore only the explicit amplitude module, including
its correction coefficients, support partition and exact all-amplitude rank
formula.

### 2.3 Support-to-complete-system order

Formula and alias queries included:

- inverse Puiseux support with minimal order or minimal telescoper;
- root-value span with polynomial moments or monodromy;
- exponential Gauss--Manin, Brieskorn module and cyclic vector;
- rapid-decay periods and scalar differential equations; and
- first reduced dependence, Hermite reduction and hyperexponential
  telescoping.

Bostan--Chen--Chyzak--Li--Xin explicitly prove that the first linear
dependence among residual forms produces a minimal telescoper. The quotient
reduction, first-dependence construction, minimality mechanism and
certificate production are consequently a **COLLISION**, not a new
algorithm.

Hien--Roucairol provide rapid-decay integral representations for exponential
Gauss--Manin systems, while Hien proves the perfect algebraic-de Rham/rapid-
decay homology pairing. These supply known ingredients for complete-system
minimality.

No inspected source stated the remaining normalized identity

\[
\operatorname{ord}_{\min}
=q(P,G'\,dx)
=|\Sigma(P;G)|
=\dim\operatorname{span}_{\mathrm{red}}\{G(x_i)\},
\]

or the repaired standard-ray block bounds in the frozen form. That residual
unit is a bridge from inverse-root support and zero-dimensional monodromy to
the complete exponential-period operator order. The individual-cycle
equality originally proposed in the companion note is false and is excluded.

### 2.4 Arbitrary-perturbation-degree zero-cycle Bautin bound

The 2025 paper of Bravo--Mardešić--Novikov--Pontigo-Herrera explicitly asks
for a degree-uniform zero-cycle Bautin-index bound.  The frozen target is the
ordinary parameter-content statement

\[
\mathcal B_\infty=\mathcal B_{d-1}
\]

for every exact degree-\(d\) phase and every perturbation of arbitrary fixed
degree.

Formula and alias queries included combinations of:

- `Bautin index`, zero-cycle, higher Melnikov and polynomial deformation;
- Cayley--Hamilton with Melnikov or Bautin ideals;
- differentiated recurrence and parameter content;
- `M_mu` with zero-dimensional cycles; and
- power-phase and `x^d` first-nonzero Melnikov order.

The frozen 2021 and 2025 zero-cycle TeX sources contain no Cayley--Hamilton,
Lagrange--Bürmann or recurrence formulation of the bound.  Batenkov--Yomdin,
*Taylor Domination, Difference Equations, and Bautin Ideals*
(arXiv:1411.7629), is the closest primary antecedent: it proves that a
polynomial sequence satisfying a recurrence of length (d) has Bautin ideal
generated by its first (d) entries.  That result does not directly state the
zero-cycle theorem because the \(\mu\)-th Melnikov coefficient applies
\(D_t^{\mu-1}\) to the \(\mu\)-th power moment.  The residual step is the
infinity-monodromy proof that differentiation is injective on zero-cycle
polynomial integrals and therefore preserves ordinary parameter content.

Batenkov--Binyamini's Abel-equation moment Bautin bound concerns a different
moment sequence and gives a quadratic degree bound; it is contextual rather
than a collision.  No exact statement of the frozen (d-1) result was found
in the bounded primary corpus.  Briskin--Yomdin's 1997 algebraic-family
framework is an additional close antecedent.  The 2025 problem's ambient ideal
convention is terse.  Proposition 6.1 of the manuscript now proves that its
parameter content is exactly the ordinary local Taylor-coefficient Bautin
ideal defined by Batenkov--Yomdin.  Alternative localizations, radicals, or
analytic-parameter ideals remain outside the target.

## 3. Unit dispositions

| Target | Contribution unit | Outcome | Reason |
|---|---|---|---|
| A | Chebyshev/Dickson basis, inverse-branch Fourier machinery | **COLLISION** | Pakovich and later moment literature already contain these ingredients. |
| A | all-amplitude paired module with `q=2N+epsilon` and parity spectrum | **BOUNDED UNCERTAINTY** | No exact collision found; close fixed-segment and moment-problem antecedents require a broader specialist search. |
| B | Ritt collision and `S_4 x C_3` monodromy | **COLLISION** | Explicitly present in Behajaina--Konig--Neftin. |
| B | five corrected amplitude summands and all-amplitude rank formula | **BOUNDED UNCERTAINTY** | Exact formulas and aliases produced no collision in the bounded corpus. |
| Bridge | reduction, first residual dependence, minimal telescoper and witness | **COLLISION** | Explicit creative-telescoping prior art. |
| Bridge | inverse-support/root-span to complete-system order identity | **BRIDGE** | Known ingredients; the exact bridge was not found in the inspected sources. |
| Bridge | repaired standard-ray block bounds | **BOUNDED UNCERTAINTY** | Mathematically retained, but no dedicated historical-priority search has closed the gap. |
| Bridge | unrestricted individual-cycle equality | **STOP** | Falsified by the retained Dickson/Bessel counterexample. |
| C | polynomial-recurrence Bautin principle | **COLLISION** | Batenkov--Yomdin prove the general undifferentiated recurrence theorem. |
| C | Cayley--Hamilton/monodromy bound `B_infinity=B_(d-1)` for arbitrary perturbation degree | **BOUNDED UNCERTAINTY** | No exact collision found; close 1997/2014 antecedents require specialist review. |
| C | degree-box consequence `b_coeff(m)<=m-1` | **BOUNDED UNCERTAINTY** | The quantifiers match the published problem for the explicit ordinary Taylor-coefficient convention; identification with the source's terse `b(m)` remains conditional. |

## 4. Decision

The gate supports continued preparation of one integrated candidate paper,
not three claims of established historical priority.

Permitted wording:

- “candidate all-amplitude classification not located in the bounded search”
  for Result A;
- “candidate explicit amplitude module for a known exceptional Ritt
  collision” for Result B; and
- “Atlas-specific support-to-order bridge and benchmark” for the supporting
  bridge; and
- “candidate ordinary coefficient bound
  \(b_{\mathrm{coeff}}(m)\le m-1\)” and the conditional statement that it
  answers the zero-cycle degree-box problem if the source's \(b(m)\) uses
  that convention.

Forbidden wording includes “first”, “new algorithm”, “previously unknown” or
“three open problems solved” without a later specialist novelty review. The
mathematical proofs and deterministic replays may be evaluated independently
of this historical-priority uncertainty.

## 5. Remaining gate work

Before a publication-ready or priority claim, obtain:

1. a MathSciNet and direct zbMATH search using the normalized formulas and
   subject aliases;
2. backward and forward citation-chain inspection from Pakovich's 2004
   Chebyshev theorem, the 2009 polynomial-moment solution, the 2013
   hyperexponential telescoping paper and the 2026 monodromy paper;
3. specialist searches in exponential Gauss--Manin/D-module terminology;
4. an independent expert's assessment of whether the support-to-order bridge
   is standard or implicit;
5. a zero-cycle/Bautin specialist's assessment of Proposition 6.1 and the
   differentiated-recurrence novelty boundary; and
6. a dated search appendix recording databases, query strings, result counts,
   inclusions, exclusions and inaccessible items.
