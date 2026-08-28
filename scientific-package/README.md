# Cyclicity Atlas open-problem laboratory

This ignored workspace records exploratory theorem routes derived from the
immutable `v0.7.0-candidate` Atlas package.  Nothing here is publication
evidence by itself.

The working rules are:

1. state each candidate theorem exactly;
2. attach an exact falsification test before drafting prose;
3. preserve rejected routes and rediscoveries;
4. keep Atlas replay, new computation, proof, novelty, independent review and
   publication readiness separate.

The frozen upstream package used in the first pass has SHA-256
`3a132530f31c1af3870de7af7a13d41389ffbf051ab2760b3c0110173c268e8a`.

`PROBLEM_SELECTION_GATE.md` is the controlling research-selection record.
After the hostile quantifier screen, the active integrated trio is the Dickson
all-amplitude classification, the repaired exceptional Ritt fused-module
classification, and the uniform zero-cycle coefficient Bautin bound.
`RESULT_PACKAGE_C.md` is now explicitly a supporting operator bridge;
`RESULT_PACKAGE_ZERO_CYCLE_BAUTIN.md` is the third-result dossier.  All remain
theorem candidates rather than publication evidence.

## Non-specialist guide

This is one integrated candidate paper, not a claim that three historically
posed open problems have been solved.  It contains two classifications prompted
by the Atlas and one ordinary coefficient-Bautin theorem candidate; the
support-to-order result is supporting infrastructure.

| Candidate unit | Plain-language question | Candidate answer | What it may enable | What it does not establish |
|---|---|---|---|---|
| Dickson amplitudes | Which independent period channels can a polynomial amplitude activate for a Dickson phase? | A paired-module decomposition gives the exact rank `2N + epsilon`; odd degree realizes only even ranks, while even degree realizes every rank. | Structural classification of complete rapid-decay period systems in this family. | A new inverse-series method, an individual-contour order formula, or historical priority. |
| Exceptional Ritt phase | How do all amplitudes split for the known phase `(x^4+x)^3`? | Five explicit modules of ranks `1, 1, 3, 3, 3` classify every polynomial primitive. | An exact amplitude catalogue for this one degree-twelve collision. | Discovery of the collision or its monodromy group, which are prior art. |
| Coefficient Bautin bound | How many Melnikov orders are needed to generate the ordinary parameter-coefficient ideal for a zero-cycle? | For a degree-`d` phase the candidate cutoff is `d-1`, giving `b_coeff(m) <= m-1` in the full degree box. | A finite algebraic stopping bound under the stated ordinary Taylor-coefficient convention. | A result for alternative analytic or radical ideal conventions. |
| Support-to-order bridge | Can complete-system differential-equation order be predicted from inverse support? | The candidate identifies complete-system order with active support/root-value rank and supplies corrected standard-ray bounds. | Exact symbolic prediction and certificate benchmarks. | A new creative-telescoping algorithm or an unrestricted individual-cycle equality. |

Here a *phase* is the polynomial in the exponential, an *amplitude* is the
polynomial multiplying it, a *channel* is one non-trace Fourier component of
the inverse expansion, and a *zero-cycle* is a weighted sum of roots whose
weights total zero.  A coefficient Bautin ideal records the perturbation-
parameter coefficients appearing in the local displacement series.

**These results do not bound real planar limit cycles.**  They concern
polynomial exponential periods and zero-dimensional cycles under the stated
algebraic conventions.

`THEOREM_H_SUPPORT_RANK.md` contains the self-contained reconstruction
of the Atlas support/rank bridge and its standard-ray realization; this is
same-programme proof work, not independent review.  The unrestricted
cycle-wise order formula is rejected by the explicit modified-Bessel
counterexample in the manuscript.  Private development audits are retained
locally but are excluded from the public package and are not publication
evidence.

`NOVELTY_GATE_TARGETS.yaml` freezes the contribution units from the first
portfolio and must be refreshed before any release decision.
`NOVELTY_GATE_REPORT.md` records formula and alias searches, close
antecedents, and unit-level `COLLISION`, `BRIDGE`, `BOUNDED UNCERTAINTY` and
`STOP` outcomes. It is a bounded search record, not proof of historical
priority.

`THEOREM_D_BAUTIN_BOUND.md`, `check_general_bautin_bound.py` and
`screen_power_bautin_uniform.py` contain the proof and exact
excluded-range falsifiers for the third theorem.  The result covers arbitrary
fixed perturbation degree and gives \(b_{\mathrm{coeff}}(m)\le m-1\) under
the ordinary parameter-content convention.  The source's \(b(m)\) inherits
this bound only if its terse ideal uses that convention.  The earlier sextic
case study is retained only
in the private development workspace; it is not one of the three claims and
is excluded from the public allowlist.

`CANDIDATE_PREPRINT.pdf` is the deterministic anonymous journal-style
rendering of the integrated manuscript.  Its main scientific content is now
screened as two amplitude classifications and one uniform zero-cycle Bautin
theorem candidate, with the support-to-order result retained as a bridge; rebuild
it with:

```sh
bash build_preprint.sh
```

`BILINGUAL_ABSTRACT.md` contains aligned English and Traditional-Chinese
abstracts. `REFEREE_CONFIGURATION.md` records the authorized simulated-panel
configuration, and `REFEREE_PACKET.md` is a read-only specialist handoff.
Neither file records independent human review.

## End-to-end deterministic replay

### Prerequisites and frozen input

The recorded environment is Python 3.14.6 with `sympy==1.14.0`, Pandoc 3.9
with Lua support, and pdfTeX 3.141592653-2.6-1.40.29 from TeX Live 2026.
`REPLAY_REQUIREMENTS.txt` pins the Python dependency.  Byte-identical PDF
reproduction additionally depends on compatible fonts, locale, Pandoc and TeX;
`REPRODUCIBILITY_ENVIRONMENT.md` records that non-hermetic boundary.

Replay also requires the frozen Atlas archive as an input.  Its required
SHA-256 is:

```text
3a132530f31c1af3870de7af7a13d41389ffbf051ab2760b3c0110173c268e8a
```

The archive is not trusted by path or filename.  The checker verifies this
digest before extracting the input into a fresh temporary directory.

### One path-neutral lifecycle

Choose absolute paths for the extracted candidate source and the downloaded
Atlas archive.  The staging destination must not already exist.

```sh
package_source=/absolute/path/to/extracted/candidate-package
atlas_archive=/absolute/path/to/cyclicity-support-fusion-atlas-v0.7.0-candidate.zip
replay_parent="$(mktemp -d)"
staged_root="$replay_parent/candidate"

test "$(shasum -a 256 "$atlas_archive" | awk '{print $1}')" = \
  "3a132530f31c1af3870de7af7a13d41389ffbf051ab2760b3c0110173c268e8a"

python3 "$package_source/stage_candidate_package.py" \
  --source "$package_source" \
  --output "$staged_root"

python3 "$staged_root/check_candidate_package.py" \
  --root "$staged_root" \
  --replay \
  --atlas-archive "$atlas_archive" \
  --exact-root \
  --output "$staged_root/PACKAGE_INTEGRITY_RECEIPT.json"

python3 "$staged_root/check_candidate_package.py" \
  --root "$staged_root" \
  --replay \
  --atlas-archive "$atlas_archive" \
  --exact-root \
  --verify-stored-receipt
```

For this candidate lifecycle, the stored receipt is expected to report:

- `status: "pass"`;
- `replay_requested: true`;
- `package_allowlist_verified: true` and
  `exact_release_root_verified: true`;
- `command_execution_count: 13` and `artifact_comparison_count: 14`;
- one `byte_identical: true` record for every retained replay artifact; and
- an `established` claim that explicitly records byte-identical replay.

A run without `--replay` checks package identity and embedded receipt integrity
only.  Its receipt must report zero replay commands and comparisons, must not
claim replay under `established`, and must list replay as not executed under
`not_established`.

### Assurance distinctions

| Evidence | Establishes | Does not establish |
|---|---|---|
| Manifest, hashes and exact-root check | Identity and membership of the checked package bytes. | Mathematical truth, source quality or novelty. |
| Byte-identical replay | The retained commands reproduce the retained finite artifacts in the recorded environment. | The universal theorems, independent reconstruction or peer review. |
| Written proof | A mathematical argument that specialists can inspect. | Acceptance, historical priority or correctness without review. |
| Simulated/internal review | Model-mediated objections and repair prompts from the same programme. | Independent human or institutional validation. |
| Bounded novelty audit | No collision was found in the recorded corpus and searches. | Absolute priority or a systematic literature review. |
| Candidate packaging | A coherent anonymous unrefereed handoff. | Publication authorization or deployment. |

`PACKAGE_MANIFEST.json` and `check_candidate_package.py` therefore freeze and
replay the local candidate package, but a passing receipt is not independent
review, peer review, proof correctness, novelty, publication authorization or
deployment authorization.
