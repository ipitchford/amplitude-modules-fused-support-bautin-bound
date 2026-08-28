# Pre-proof problem-selection gate

**Date:** 28 August 2026  
**Status:** active research-selection control  
**Purpose:** prevent technically correct but low-value statements from consuming
proof and packaging effort

## 1. Why this gate exists

The first research pass selected tractable statements, completed internal
candidate proofs, and only then performed a sufficiently direct
primary-literature comparison.  That ordering was wrong.  It produced useful
mathematics, but it did not establish three results as solutions to historically
posed publishable open problems or as three independent priority claims.

No further main-theorem proof work is authorized by this research plan until a
candidate passes every gate below.  Existing proof arguments and failed routes
are preserved as evidence; they do not acquire main-result status merely
because they replay or have an internal candidate-proof disposition.

## 2. Mandatory gates

| Gate | Required evidence | Failure disposition |
|---|---|---|
| G1. Recognised open target | Exact locator in the current Atlas **and** either a current external primary-source problem statement or a field-level capability whose absence is documented; a superseded source-history conjecture is insufficient | `STOP` |
| G2. Residual novelty | Frozen formula, aliases, small instances, primary-source and citation-chain comparison; no collision on the load-bearing unit | `STOP` or `BRIDGE_ONLY` |
| G3. Audience consequence | A specialist audience, a concrete capability or classification that becomes available, and an explanation of why the result is not merely an explicit example of a known theorem | `STOP` if both breadth and depth are low |
| G4. Early falsifier | A short exact counterexample/collision test that runs before a long proof | `PAUSE` until supplied |
| G5. Manageable risk | No chain requiring more than two unresolved high-risk assumptions | `PIVOT` |
| G6. Independent contribution | The residual claim is not merely the Atlas theorem, a standard algorithm, or a direct specialization of a cited theorem | `STOP` or supporting lemma only |

Search failure never proves novelty.  `GO` below means permission to run the
next bounded screen, not permission to claim priority or publication readiness.

An Atlas-labelled direction that lacks an external anchor can still survive,
but only if the output is a broad classification or mechanism rather than a
catalogue of examples.  Conversely, an externally stated open problem does not
pass automatically: one tiny instance already implicit in an earlier example
is not enough.

## 3. Retrospective disposition of the current draft

| Existing unit | Internal status | Selection status | Reason |
|---|---|---|---|
| general monodromy-block amplitude theorem | internal candidate proof | `BRIDGE_ONLY` | Pakovich--Muzychuk already classify the invariant subspaces; Gavrilov--Pakovich combine them with Puiseux filtering.  The complex central-projector descent and Atlas support interpretation are useful infrastructure, not yet a high-impact standalone problem. |
| Dickson all-amplitude formula | internal candidate proof; a second same-programme implementation agrees on bounded cases | `RETAIN_IN_INTEGRATED_TRIO` | Pakovich's fixed-segment Chebyshev theorem is close, but the complete-system all-amplitude rank law and odd/even attainable-rank classification did not collide in the bounded search; substantial enough inside the combined paper, not assessed as a standalone paper |
| exceptional degree-twelve amplitude module | internal candidate proof after trace repair; a second same-programme checker agrees on bounded cases | `RETAIN_IN_INTEGRATED_TRIO` | exact correction polynomials, hidden trace cancellation and the complete fused module remain a distinct hard classification unit |
| generic first-dependence operator algorithm | internal candidate proof | `STOP_AS_NOVELTY` | minimal hyperexponential telescoping by first reduced dependence is prior art |
| standard-ray block order bounds; general Dickson block-mass equality demoted | internal candidate proof of two-sided bounds only | `SCREEN` | the bounds are a potentially useful analytic residual, but exact block-mass equality is not retained without a direct differential-module derivation and a Stokes/cycle literature collision search |
| binomial Laurent solution module | internal candidate-proof specialization | `STOP_AS_NOVELTY` | direct consequence of Pakovich's Laurent-moment theorem plus deck grading |

The existing manuscript is therefore an exploratory theorem draft, not evidence
that the objective has been met.

## 4. Screened portfolio

### Screened case study — the sextic zero-cycle family

The 2025 primary source states three separate open questions in its concluding
section: determine the structure and zeros of first nonzero Melnikov functions;
describe low-degree bifurcation diagrams; and bound the zero-cycle Bautin
index.  It singles out

`f=x^6`, `C=(1,2,1,-1,-2,-1)`, `g=x^2+x^3`

for study.  The selected scope replaces the single perturbation by the full
reduced family

`g=a0+a1*x+...+a5*x^5`,

since terms in `C[f]` are trace terms for the cycle.  Roots are ordered by
`x_j=omega^j*t^(1/6)`.

The hostile quantifier screen changes the disposition.  The source asks for
uniform structure over degrees, phases and cycles.  Fixing one sextic phase
and one cycle gives a coherent and useful family-level case study, but it does
not establish the source's three broad questions as three historical
open-problem solutions.  Z1--Z3 below are therefore retained together as
supporting evidence and a worked application, not counted as three headline
results.

#### Z1 — first nonzero Melnikov structure and zero count

**Exact output.**  Derive the all-order identity

`M_mu=(-1)^mu/mu! * (d/dt)^(mu-1) Integral_C(g^mu)`

and specialise it to classify the first nonzero coefficient for every point
of the sextic parameter space.  State the number of regular zeros, counted
over all cycle determinations, on every stratum.

**Independence.**  The classical Lagrange--B\"urmann identity is supporting
machinery, not the claimed result.  The contribution is the complete
family-level stratification and zero count.  The 2021 paper treats only one
closely related perturbation and gives no parameter-family classification.

**Decision:** `RETAIN_IN_ONE_CASE_STUDY`; do not count separately.

#### Z2 — the low-degree bifurcation diagram

**Exact output.**  Give the algebraic parameter strata on which the first
nonzero Melnikov function has two, one, or zero distinct regular `t`-values at
which at least one determination vanishes, matching the counting convention
of the 2025 paper.  Include the transition to the centre locus and all
endpoint/leading-coefficient degeneracies.  Do not claim a diagram for the
full displacement function unless it is separately established.  Branchwise
roots in `T=t^(1/6)` are an intermediate calculation and must not be reported as
the paper's zero count.

**Independence.**  This answers the 2025 low-degree bifurcation question for a
complete nontrivial family, rather than restating a generic sparse-polynomial
discriminant.

**Decision:** `RETAIN_IN_ONE_CASE_STUDY`; do not count separately.

#### Z3 — the Bautin ideal and index

**Exact output.**  In the coefficient ring `C[a0,...,a5]`, prove that the
coefficient Bautin ideal is

`(a1, a5, a2*a3, a3*a4)`

and is generated by orders one and two.  Identify its radical components with
the `C[x^2]` and `C[x^3]` composition centres.  State explicitly which
definition of Bautin ideal is used and whether the result is ordinary-ideal,
radical, or merely set-theoretic.

**Sharpness.**  `g=x^2+x^3` has `M_1=0` and `M_2!=0`, so index two is attained.

**Decision:** `RETAIN_IN_ONE_CASE_STUDY`; do not count separately.

### Selected external candidate — uniform zero-cycle Bautin bound

**External target.**  Bravo--Marde\v{s}i\'c--Novikov--Pontigo-Herrera (2025),
concluding problem following their definition of the zero-cycle Bautin index:
bound the index when `deg f, deg g <= m`, uniformly over cycles.

**Atlas role.**  The Atlas Fourier-channel criterion separates the trace
channel from genuine cycle channels.  Combined with Lagrange--B\"urmann
expansion, it converts the `mu`-th displacement coefficient into a derivative
of the zero-cycle power moment of `g^mu`.

**Exact output.**  For every monic phase `f` of degree `d`, every zero-cycle
`C` of `f`, and a polynomial perturbation family of arbitrary fixed
degree, define the ordinary
parameter-content Bautin ideals and prove

`B_infinity = B_(d-1)`.

The internal candidate proof combines the all-order Lagrange--Bürmann identity
with Cayley--Hamilton in `R[t,x]/(f-t)`.  The crucial step is that
differentiation is injective on zero-cycle polynomial integrals: an element of
the kernel is single-valued, and averaging its infinity-monodromy orbit kills
the zero-cycle.  Differentiation therefore preserves parameter content
exactly, with no restriction on `deg g`.

**Definition gate.**  This is an ordinary coefficient-ideal result.  A finite
jet lemma proves that parameter content equals the ordinary local
Taylor-coefficient Bautin ideal.  The theorem does not claim a bound for
alternative localized, radical, or analytic-parameter ideals.

**Scope gate.**  The theorem covers the complete degree box
`deg f,deg g<=m` and yields `b_coeff(m)<=m-1` under the ordinary
Taylor-coefficient convention.  It transfers to the source's `b(m)` only if
that terse ideal uses the same convention.  Independent human specialist
review of the interpretation remains required for an assurance upgrade; it is
not supplied by the internal model-mediated editorial gate.

**Collision gate.**  Batenkov--Yomdin (2014) prove a general Bautin-ideal
theorem for polynomial recurrences.  That is a close antecedent and must be
cited.  Their theorem does not directly handle the order-dependent
derivatives converting the moment sequence to the Melnikov sequence; the
monodromy-injectivity/content-preservation argument is the residual unit.  Exact
phrase and formula searches in the 2021 and 2025 zero-cycle sources and the
two closest Bautin papers found no statement of this bound.  Search absence
does not establish priority.

**Early falsifier.**  Generic quotient matrices in rectangular cases
`(d,n)=(2,4),(3,5)` pass exact Cayley--Hamilton and monodromy-average
checks.  Representative power phases with `deg g>deg f` pass higher-order
ideal reductions.  Complex-cycle sharpness is
`d-1`; integer cycles have a certified lower witness `d/p`, with `p` the
least prime divisor.  These domains are kept distinct.

**Decision:** `GO_AS_THIRD_HEADLINE_CANDIDATE`, subject to internal adversarial
review and the stated ordinary-coefficient, conditional-source-mapping wording.
Independent human specialist review remains an assurance-upgrade gate.

### Rejected narrower unit — the isolated named perturbation

**External target.**  The same 2025 paper asks for the structure and zero count
of first nonzero Melnikov functions and names the phase `f=z^6`, cycle
`(1,2,1,-1,-2,-1)`, and perturbation `g=z^2+z^3`.

**Screen result.**  The named example alone is `STOP_AS_MAIN_RESULT`: a closely
related `z^6`, `z^2+z^3` example with the same Fourier support and an explicit
second coefficient already appears in the 2021 zero-cycle centre paper.  Under
the standard root ordering the newly named cycle gives

`M_2(t) = (5/2)(1-sqrt(3)i)t^(-1/6)`,

up to the paper's sign/normalisation convention, so it has no regular zeros.
That is a useful check, not a paper-scale contribution.

**Residual candidate.**  An all-order Lagrange--Fourier formula for arbitrary
polynomial phase, perturbation and cycle may support Z1 and a genuine
structure theorem.  Because Lagrange--B\"urmann inversion is classical, the
identity itself is `BRIDGE_ONLY` unless the resulting classification or sharp
zero bound survives a broader object-level priority audit.

**Decision:** `BRIDGE_ONLY_PENDING_CONSEQUENCE`.

### Deferred broader unit — sparse bifurcation and real Chebyshev diagrams

**External targets.**  The 2025 paper separately asks for low-degree
bifurcation diagrams and for real-domain zero bounds/Chebyshev behaviour.

**Atlas role.**  For power phases the Atlas DFT support turns the tangential
integral into a sparse polynomial in `t^(1/d)`.  This identifies a candidate
discriminant arrangement and an ordered-monomial Chebyshev system.

**Selection risk.**  A direct sparse-discriminant restatement or Descartes-rule
corollary is too standard to count.  The candidate survives only if the full
diagram, multiplicities and deck identifications are classified for a
nontrivial family, or if the Chebyshev statement extends beyond the power
family.

**Decision:** `DISCOVERY_GATE`; no main claim has yet passed G3 or G6.

## 5. Atlas-internal portfolio retained for comparison

### Candidate P1 — complete amplitude spectra for every Atlas low-rank phase

**Named target.**  `AMPLITUDE_LAURENT_EXTENSION.md`, section 9, and
`COMBINED_AMPLITUDE_LAURENT.md`, section 21: classification of amplitudes of
bounded induced rank.

**Exact proposed output.**  For each of the six all-degree Atlas phase
families, determine the monodromy character blocks, give explicit free
`C[P]`-module generators for every block, and state the complete attainable
rank spectrum, including all collision strata.

**Impact if successful.**  This converts the Atlas's abstract support oracle
into an explicit all-amplitude classification on its entire low-rank locus.
It is broad enough to subsume the Dickson and exceptional calculations rather
than presenting them as unrelated small theorems.

**Risks.**  Prior polynomial-moment decompositions may already imply some
family rows; the cubic-over-power collision strata presently have compressed
or finite-window-only arguments.

**Earliest tests.**  Before further proof, (i) search each family formula and
module generator against the primary moment/monodromy corpus, and (ii) run an
exact bounded counterexample search over every claimed block lattice, with the
search bound and non-inference boundary frozen in advance.

**Decision:** `GO_TO_COLLISION_AND_FALSIFIER_GATE`.  It counts as one problem,
not six.

### Candidate P2 — cycle-specific minimal order from monodromy blocks

**Named target.**  `MANUSCRIPT.md`, sections 14.1--14.2: the generic order
corollary does not determine the order of a chosen cycle, which can annihilate
active channels.

**Exact proposed output.**  For a stated standard rapid-decay ray system,
classify the minimal scalar order of each weighted cycle in terms of the
differential submodules generated by the monodromy blocks; make all equality
conditions effective for the Atlas families.

**Impact if successful.**  It upgrades a generic complete-system statement to
the actual contour-dependent ODE seen in applications.

**Risks.**  The abstract bounds may be standard differential-module theory;
effectivity may require a separate irreducibility proof for every block.

**Earliest tests.**  Search the exact block-contact statement in primary
Gauss--Manin, Stokes, cyclic-vector and creative-telescoping literature.  Then
test the smallest reducible and irreducible two-channel examples; any failure
of the proposed equality criterion stops the general claim.

**Decision:** `GO_TO_COLLISION_GATE`; no new operator catalogue before it
passes.

### Candidate P3 — finite structural Laurent criterion beyond deck grading

**Named target.**  `AMPLITUDE_LAURENT_EXTENSION.md`, section 9, and
`COMBINED_AMPLITUDE_LAURENT.md`, section 21: finite structural conditions
equivalent to the Laurent coefficient test for controlled phases.

**Exact proposed output.**  First select a non-binomial controlled Laurent
family outside the already classified composition/deck and known exceptional
case-study mechanisms.  Only then freeze a proposed finite structural
criterion and prove equivalence to all moment vanishings.

**Impact if successful.**  It would replace an infinite coefficient test by a
finite algebraic classification on a genuinely new family, directly serving
the Laurent moment-problem audience.

**Risks.**  This is the highest-risk candidate: known exotic solution modules
defeat naive composition-only statements, and finite-prefix stabilization is
not proof.

**Earliest tests.**  A family is admissible only if (i) its monodromy and known
moment decomposition are not already classified, (ii) exact kernel dimensions
stabilize under two separately increased windows, and (iii) the proposed module
survives adversarial non-composition amplitudes.  Failure of any test returns to
family selection rather than proof writing.

**Decision:** `DISCOVERY_GATE`; no family has yet passed.

## 6. Risk-adjusted ranking

| Candidate | Impact if true | Present feasibility | Novelty risk | Next action |
|---|---:|---:|---:|---|
| uniform zero-cycle Bautin bound | high | high | medium | integrate as a full degree-box candidate under the explicit coefficient convention, then seek independent human specialist review for assurance upgrade |
| Z1--Z3 sextic zero-cycle family | medium | high | medium | retain as one supporting case study, not three claims |
| P1 all-six-family amplitude spectra | high | medium | medium-high | external-anchor and formula collision screen |
| P2 cycle-specific minimal order | medium-high | medium | high | primary differential-module collision search |
| Z3 bifurcation/Chebyshev classification | medium-high | medium | high | require nontrivial family-level output before proof |
| P3 non-binomial Laurent criterion | high | low-medium | high | select family only after reconnaissance |

The third headline candidate is now the full-degree Bautin theorem.  The
sextic calculations remain one supporting case study.  The Atlas-internal
P1/P2 results may enter as methods or appendices but do not replace a failed
external unit.  If the differentiated-recurrence theorem collides with prior
art or receives a negative independent human specialist review, the correct
outcome is a narrower candidate or fewer headline results—not relabeling the
sextic subquestions as three established historical open-problem solutions.

## 7. Decision rhythm

After every bounded search or falsifier run, record one of `GO`, `PIVOT`,
`BRIDGE_ONLY`, or `STOP` before doing more algebra.  Reassess the portfolio
whenever a primary-source collision appears.  Package replay certifies bytes
and computations only; it is deliberately downstream of problem selection.

## 8. Candidate-release governance

This selection gate decides which claims may enter the integrated candidate; it
does not itself authorize publication.  An Evidence Press release may make only
an explicitly anonymous unrefereed candidate available, and only after the
internal model-mediated editorial gate returns `PASS` or `PASS_WITH_NOTES`, the
deterministic package gates pass on the same repaired frozen bytes, and the user
separately authorizes publication.

Internal editorial review, same-programme implementations, replay and public
candidate availability do not establish independent human specialist review,
independent reproduction, historical priority, formal verification or peer
review.  Independent human specialist review and broader priority resolution
remain unresolved and are required for any corresponding assurance upgrade.
Results A and B remain Atlas-family classifications.  Result C remains the
ordinary coefficient theorem for `b_coeff`; its mapping to the cited source's
terse `b(m)` remains conditional on that source using the same convention.
