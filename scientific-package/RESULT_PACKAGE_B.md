# Result package B: exceptional Ritt-fusion amplitudes

**Problem:** classify every polynomial amplitude for
\(P=(x^4+x)^3\), including cancellation inside the exceptional fused
summands.  
**Disposition:** **INTERNAL CANDIDATE PROOF; STRONGEST BOUNDED NARROW NOVELTY
UNIT**  
**Publication state:** Atlas-family component of one integrated anonymous
unrefereed candidate

## Exact result

With \(Q=x^4+x\), every primitive has a unique decomposition

\[
G=A_0(P)+A_1(P)Q+A_2(P)Q^2+m_0+m_1+m_2
\]

over the three displayed modules \(M_0,M_1,M_2\).  Their support blocks are

\[
\{1,7,10\},\qquad\{2,5,11\},\qquad\{3,6,9\},
\]

and the two proper-composition channels are \(\{4\}\) and \(\{8\}\).
By the reconstructed support/rank theorem,

\[
q(P,G'\,dx)=
\mathbf1_{A_1\ne0}+\mathbf1_{A_2\ne0}
+3\sum_i\mathbf1_{m_i\ne0}.
\]

The written candidate proof of the direct module decomposition and all-degree
noncancellation statement is complete within the package.  The missing
exclusion in the original CRT paragraph is supplied by the Newton fibre-trace
lemma: \(M_0,M_1\) are \(Q\)-trace-free, while \(M_2\) has constant trace and
hence contributes only residue zero in the quartic trace channel.  Within the
candidate theorem, every rank \(0,\ldots,11\) occurs.

## Bound theorem and evidence

The bound files are `THEOREM_B_EXCEPTIONAL_RITT.md`,
`THEOREM_H_SUPPORT_RANK.md`, `support_rank_reconstruction_receipt.json`,
`exceptional_amplitude_receipt.json` and
`exceptional_channel_independence_receipt.json`.  `PACKAGE_MANIFEST.json` is
the sole current authority for their SHA-256 values and for the frozen Atlas
archive digest; hashes are not duplicated in this prose dossier.

The 23 Atlas/Krylov cases and bounded exact minors are falsification evidence,
not replacements for the proof.  The revised standalone channel checker also
verifies the exact Newton recurrence and generator traces used by the
all-degree trace lemma.

## Replay

    python3 check_exceptional_amplitudes.py \
      --atlas-root /tmp/csf-atlas-v070/extracted/cyclicity-support-fusion-atlas-v0.7.0-candidate \
      --output /tmp/exceptional-amplitude-replay.json

    python3 check_exceptional_channel_independence.py \
      --max-coefficient-degree 6 \
      --output /tmp/exceptional-channel-replay.json

## Novelty ceiling

Behajaina--Konig--Neftin already identify this exact Ritt collision and its
\(S_4\times C_3\) monodromy.  The candidate contribution is the explicit
amplitude module, correction coefficients, support partition and all-amplitude
rank formula.  No monodromy-priority claim is permitted.

## Candidate-release gates

- internal model-mediated editorial acceptance or acceptance with notes on the
  repaired frozen bytes;
- immutable release packaging and deterministic replay on those bytes; and
- separate user authorization for an explicitly anonymous unrefereed release.

Independent human proof review, independent specialist review of the
reconstructed support theorem and an expanded specialist priority search remain
unresolved.  They are required for an assurance upgrade, not falsely supplied
by internal editorial review or candidate release.
