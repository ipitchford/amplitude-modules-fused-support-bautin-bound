# Read-only referee packet

**Prepared:** 27 August 2026  
**Purpose:** specialist review handoff  
**Status:** candidate package with deterministic internal replay; no
independent specialist review has occurred

## Bound scientific targets

PACKAGE_MANIFEST.json is the sole hash authority for the manuscript,
theorem notes, source-provenance record, programs and receipts.  Reviewers
should reject a handoff whose package checker does not reproduce that manifest
and its embedded receipt digests.

## Claim map

### Load-bearing bridge

\[
q(P,G'\,dx)=|\Sigma(P;G)|
=\dim\operatorname{span}_{\mathrm{red}}\{G(x_i)\}.
\]

The proof is self-contained in the candidate but follows the Atlas proof
architecture and was produced by the same research programme.

### Result A

For \(P=D_d(x,a)\), \(a\ne0\), the unique Dickson paired-module expansion
satisfies

\[
q(D_d,G'\,dx)=2N(G)+\varepsilon(G).
\]

Odd \(d\) realizes exactly the even ranks; even \(d\) realizes every rank.

### Result B

For \(P=(x^4+x)^3\), five explicit non-trace summands have ranks
\(1,1,3,3,3\), disjoint supports, and classify all polynomial primitives.
The monodromy group used in the proof is prior art; the amplitude module and
rank formula are the residual candidate contribution.

### Supporting operator bridge

The first twisted-quotient dependence gives a primitive operator with a
direct telescoping witness. Its complete-system minimal order is
\(|\Sigma(P;G)|\). For specified standard ray-cycles, touched channels and
monodromy blocks give corrected two-sided bounds.  No general Dickson
block-mass equality is retained without a separate differential-module
derivation.

### Result C

For a monic phase \(f\) of exact degree \(d\), every zero-cycle, and every
polynomial perturbation of arbitrary fixed degree, the ordinary
parameter-content Bautin
ideal satisfies

\[
\mathcal B_\infty=\mathcal B_{d-1}.
\]

The proposed proof combines the all-order zero-cycle Melnikov identity,
monodromy injectivity of differentiation, and Cayley--Hamilton for
multiplication by \(g\) in \(R[t,x]/(f-t)\).  It gives the full degree-box
bound \(b_{\mathrm{coeff}}(m)\le m-1\) under the stated parameter-content
convention.  It implies the source's bound only if its terse \(b(m)\) uses
that ordinary coefficient convention.  The
\(d-1\) bound is sharp for complex-weight cycles; the
supplied integer-cycle construction proves only the lower witness \(d/p\),
with \(p\) the least prime divisor of \(d\).

## Mandatory adverse evidence

- The unrestricted rule “individual period order equals touched-channel
  count” is false.  The manuscript gives the \(D_3\)/modified-Bessel
  counterexample directly.
- Theorem B's original CRT paragraph did not exclude residues 4 and 8.  The
  revised target inserts a Newton fibre-trace lemma; reviewers should assess
  that repair rather than relying on bounded series checks.
- Finite exact tests are falsification evidence, not replacements for
  all-degree proofs.
- Pakovich's 2004 fixed-segment Chebyshev moment theorem is a close antecedent
  to Result A's basis machinery. It is not an exact collision found by this
  programme, but it keeps historical novelty at bounded uncertainty.
- Batenkov--Yomdin's 2014 polynomial-recurrence theorem is a close general
  antecedent to Result C. The proposed residual contribution is the
  infinity-monodromy injectivity lemma and exact preservation of parameter
  content through differentiation, not Cayley--Hamilton recurrence itself.
- The source problem states its ideal chain tersely.  Proposition 6.1 proves
  that the manuscript's parameter content equals the ordinary local
  Taylor-coefficient Bautin ideal; a specialist should audit that equivalence
  and the source comparison.

## Highest-priority review questions

1. Is the formal moment map well defined on the stated bounded-above
   completion, and is its inverse/isomorphism argument complete?
2. Does the falling-factorial Vandermonde calculation prove cyclic rank for
   every active residue set, using correctly that the relevant
   \(\alpha_r\) are nonintegral?
3. Does central-projector descent really produce polynomial
   \(\mathbf C[P]\)-modules with no hidden finite poles?
4. Does the fibre-trace projection in Theorem B remove exactly the quartic
   trace channel for arbitrary \(\mathbf C[P]\)-coefficients, and do the
   remaining monodromy and CRT steps then give exactly three channels?
5. Is Hien's perfect pairing applied correctly to this one-variable,
   parameter-dependent exponential connection?
6. Are the standard-ray hypotheses sufficient for the lower block bound, and
   is any claim accidentally stated for arbitrary contours?
7. In Result C, does infinity-monodromy averaging prove that every
   \(D_t^q\) is injective on zero-cycle polynomial integrals, and therefore
   preserve parameter content exactly?
8. Does Proposition 6.1 correctly identify parameter content with the
   ordinary local Taylor-coefficient Bautin ideal, and does the branchwise
   Lagrange--Bürmann identity correctly retain zero weights on additional
   roots when \(\deg g>\deg f\)?
9. Has Batenkov--Yomdin or later work already extracted this exact zero-cycle
   Melnikov ideal consequence from polynomial recurrences?
10. Has prior art already stated either all-amplitude module classification or
   the support-to-complete-system-order identity?
11. Does Pakovich's Chebyshev moment theorem, or its citation chain, imply the
    claimed all-amplitude rank formula after a standard translation that the
    present novelty audit missed?

## Claim-to-artifact map

| Claim or finite assertion | Written target | Exact executable evidence |
|---|---|---|
| support/rank bridge | `THEOREM_H_SUPPORT_RANK.md` | `check_support_rank_reconstruction.py` and `support_rank_reconstruction_receipt.json` |
| Dickson module formula | `THEOREM_A_DICKSON.md` | `check_dickson_amplitude.py` and `dickson_amplitude_receipt.json` |
| exceptional fused modules and trace filter | `THEOREM_B_EXCEPTIONAL_RITT.md` | `check_exceptional_amplitudes.py`, `check_exceptional_channel_independence.py` and their receipts |
| complete-system operator construction | `THEOREM_C_WEIGHTED_ORDER.md` | the producer and standalone weighted-order implementations, verifiers and receipts |
| coefficient/Taylor bridge | `THEOREM_D_BAUTIN_BOUND.md`, Lemma 1.1 | `check_bautin_content_bridge.py` and `bautin_content_bridge_receipt.json` |
| Cayley--Hamilton Bautin cutoff and witnesses | `THEOREM_D_BAUTIN_BOUND.md` | `check_general_bautin_bound.py`, `screen_power_bautin_uniform.py` and their receipts |
| package fail-closed behavior | package manifest and checker | `check_package_mutations.py` and `package_mutation_receipt.json` |

The programs are bounded falsification and byte-replay evidence.  The written
proofs, not the case counts, carry every all-degree statement.

## Replay command

The release handoff is the staged directory, not the larger development tree.
From the development directory, first assemble the exact allowlist into a new
destination:

    python3 stage_candidate_package.py \
      --output /tmp/cyclicity-open-problems-public

Then, from the staged directory, with the frozen Atlas archive available:

    python3 check_candidate_package.py \
      --root /tmp/cyclicity-open-problems-public \
      --replay \
      --atlas-archive /tmp/csf-atlas-v070/package.zip \
      --exact-root \
      --output /tmp/cyclicity-open-problems-public/PACKAGE_INTEGRITY_RECEIPT.json

A second run with `--verify-stored-receipt` confirms that the stored receipt is
the result for the exact directory now containing it.

Replay establishes byte identity and exact internal computations only. It
does not establish proof correctness, independent reconstruction, novelty,
peer review, or publication authorization.

## Permitted disposition

At present, a reviewer may recommend further review, revision, or rejection.
No reviewer should label the package “published,” “peer reviewed,” or
“independently validated” without new external evidence.
