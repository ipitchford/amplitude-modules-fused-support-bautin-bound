# Supporting bridge package: support-predicted weighted period order

**Problem:** construct an exact scalar operator for arbitrary polynomial
amplitudes and identify its complete-system minimal order from Atlas support.  
**Disposition:** **DERIVED SUPPORTING THEOREM CANDIDATE, INTERNALLY CHECKED**  
**Publication state:** anonymous unrefereed candidate and reproducibility
component; not a standalone new algorithm, independent validation, or peer
review

## Exact result

For \(G'=A\), the first dependence among

\[
[A\,dx],[PA\,dx],[P^2A\,dx],\ldots
\]

in the twisted de Rham quotient yields an operator annihilating every admitted
rapid-decay period.  The standalone implementation emits a primitive
\(\mathbf Z[s]\)-operator and \(C(x,s)\) satisfying

\[
\sum_jc_j(s)P(x)^jA(x)=\partial_xC+sP'C.
\]

Using the reconstructed support theorem, with complete-system minimality
justified by Hien's perfect rapid-decay/de Rham period pairing (Theorem 5.2),
its minimal
complete-system order is

\[
|\Sigma(P;G)|
=\dim\operatorname{span}_{\mathrm{red}}\{G(x_i)\}.
\]

No generic-individual-period minimality claim is made.

For a specified standard ray-cycle with touched channel set \(R\), the
formal-moment and Fourier--Gamma realization supplies the channel contact
needed for the repaired companion-note refinement

\[
|R|\le\operatorname{ord}_{\min}(I_n)
\le\sum_{B\cap R\ne\varnothing}|B|\le q(P,G'\,dx).
\]

No general equality with the block-mass upper bound is retained.  A proposed
Dickson specialization was demoted because the displayed scalar gauge
equivalence had not been derived self-containedly.  The explicit
\(D_3\)/Bessel counterexample to the former exact channel-count formula
remains valid and independently checkable.

## Bound theorem, implementation and evidence

The bound files are `THEOREM_C_WEIGHTED_ORDER.md`,
`THEOREM_H_SUPPORT_RANK.md`, `standalone_weighted_order_oracle.py`,
`amplitude_order_oracle_receipt.json`,
`standalone_weighted_order_receipt.json` and
`support_rank_reconstruction_receipt.json`.  `PACKAGE_MANIFEST.json` is the
sole current authority for their SHA-256 values; hashes are not duplicated in
this prose dossier.

The two implementations agree on all primitive coefficients in seven cases of
orders zero through four.  This is independent-program reconstruction within
one programme, not independent human reproduction.

## Replay

    python3 check_amplitude_order_oracle.py \
      --atlas-root /tmp/csf-atlas-v070/extracted/cyclicity-support-fusion-atlas-v0.7.0-candidate \
      --output /tmp/weighted-producer-replay.json

    python3 check_standalone_weighted_order_oracle.py \
      --producer-receipt amplitude_order_oracle_receipt.json \
      --output /tmp/weighted-standalone-replay.json

    python3 standalone_weighted_order_oracle.py \
      --phase "(x**4+x)**3" \
      --amplitude "4*x**3+1"

## Novelty ceiling

Hermite reduction, residual forms, first-dependence minimal telescopers and
rapid-decay exponential period systems are prior art.  The residual candidate
contribution is the support/root-span prediction of exact
complete-system order and the attached benchmark.  It must not be described as
a new creative-telescoping algorithm.

## Open assurance gates

- independent specialist review of the reconstructed standard-ray channel
  argument and support theorem;
- independent specialist proof and software review;
- expanded specialist novelty search;
- immutable release packaging before candidate publication.

The first three items remain required before any corresponding assurance
upgrade.  They are not represented as satisfied by internal editorial review.
