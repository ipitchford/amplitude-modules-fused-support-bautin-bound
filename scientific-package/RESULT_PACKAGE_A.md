# Result package A: all-degree Dickson amplitudes

**Problem:** classify the induced cyclic rank of every polynomial amplitude
for \(P=D_d(x,a)\), uniformly for \(d\ge2\) and \(a\ne0\).  
**Disposition:** **INTERNAL CANDIDATE PROOF; BOUNDED NARROW NOVELTY**  
**Publication state:** Atlas-family component of one integrated anonymous
unrefereed candidate

## Exact result

Every primitive \(G\) has a unique paired Dickson expansion over
\(\mathbf C[D_d]\).  If \(N(G)\) counts the nonzero unordered pairs and
\(\varepsilon(G)\) records the even-degree midpoint, then

\[
q(D_d,G'\,dx)=2N(G)+\varepsilon(G).
\]

The written candidate proof of the module and channel-noncancellation statement
is complete within the package.  Equality with cyclic rank follows within that
candidate proof from the self-contained reconstruction in
THEOREM_H_SUPPORT_RANK.md.

Odd \(d\) realizes exactly \(0,2,\ldots,d-1\); even \(d\) realizes every
rank \(0,\ldots,d-1\).

## Bound theorem and evidence

The bound files are `THEOREM_A_DICKSON.md`,
`THEOREM_H_SUPPORT_RANK.md`, `support_rank_reconstruction_receipt.json` and
`dickson_amplitude_receipt.json`.  `PACKAGE_MANIFEST.json` is the sole current
authority for their SHA-256 values and for the frozen Atlas archive digest;
hashes are not duplicated in this prose dossier.

The 171 exact nondegenerate cases at \(a=1,2,-1/2\), plus the excluded
\(a=0\) degeneration control, are bounded falsification evidence, not the
proof.

## Replay

From the laboratory directory:

    python3 check_dickson_amplitude.py \
      --atlas-root /tmp/csf-atlas-v070/extracted/cyclicity-support-fusion-atlas-v0.7.0-candidate \
      --maximum-degree 9 \
      --output /tmp/dickson-amplitude-replay.json

The replay requires the frozen Atlas extraction at the displayed path.  It
does not require network access.

## Novelty ceiling

Puiseux/Fourier support separation and individual Chebyshev/Lucas exponential
integrals are prior art.  The residual candidate contribution is the
all-amplitude \(\mathbf C[D_d]\)-module classification and exact rank formula,
not the underlying inverse-series method or special-function identity.

## Candidate-release gates

- internal model-mediated editorial acceptance or acceptance with notes on the
  repaired frozen bytes;
- immutable release packaging and deterministic replay on those bytes; and
- separate user authorization for an explicitly anonymous unrefereed release.

Independent human proof review, independent specialist review of the
reconstructed support theorem and an expanded specialist priority search remain
unresolved.  They are required for an assurance upgrade, not falsely supplied
by internal editorial review or candidate release.
