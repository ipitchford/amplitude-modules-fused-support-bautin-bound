# Response to the five-role editorial gate

## Bound review target

The five reports reviewed
`amplitude-modules-fused-support-bautin-bound-v0.1.0-candidate-review.zip`,
SHA-256
`7e7f8f9b3d09feca0ea6019045d946dc4e845b73eb8bc7fe027aa3cea807f0d1`.
All five returned Major Revision.  The reports are internal model-mediated
editorial review, not external peer review or independent specialist
validation.

## Consolidated response

| Condition | Disposition | Implemented evidence | Residual release check |
|---|---|---|---|
| R1 — root-span/monodromy equivalence | Accepted | Lemma 2.2 in `CANDIDATE_MANUSCRIPT.md` and Lemma 5.1 in `THEOREM_H_SUPPORT_RANK.md` identify the conjugate-function, inertia-Fourier, and generic full-orbit spans with an explicit finite excluded set. | Rebuild, replay, and confirmation review. |
| R2 — standard-ray realization | Accepted | Lemma 2.3 in the manuscript and Lemma 6.1 in the standalone theorem specify the flat sectorial family, orientations, basis, domination, Gamma/Vandermonde limit, and Fourier pairing. | Scope remains standard consecutive rays, not arbitrary contours or Stokes crossings. |
| R3 — coherent release governance | Accepted | `STATUS.md`, `PROBLEM_SELECTION_GATE.md`, `NOVELTY_AUDIT.md`, and the supersession note in `PANEL_REVIEW_SYNTHESIS.md` distinguish candidate-release authorization from unresolved assurance upgrades. | Confirmation may authorize only an anonymous unrefereed candidate. |
| R4 — stale/strong claims | Accepted | The Dickson block-mass equality was removed from `NOVELTY_AUDIT.md`; `RESULT_PACKAGE_A.md`, `RESULT_PACKAGE_B.md`, `RESULT_PACKAGE_C.md`, and `RESULT_PACKAGE_ZERO_CYCLE_BAUTIN.md` now use candidate/internal-check language; unbound independent-recomputation wording was removed or classified. | Automated phrase and claim-ceiling checks. |
| R5 — problem provenance | Accepted | The manuscript, bilingual abstract, README, status, and dossiers say A/B are Atlas-family classifications and C is an externally motivated ordinary coefficient-Bautin theorem candidate. | Future catalogue and press copy must use the same boundary. |
| R6 — Ritt collision boundary | Accepted | The two decompositions are displayed in the manuscript; [6, Theorems 2.2(1) and 2.3(1)] are cited for the imported collision/monodromy, while the residual amplitude classification is stated separately. | Citation and PDF checks. |
| R7 — replay and release binding | Accepted in source; final binding pending | `check_candidate_package.py` makes replay claims conditional and fail-closed; `README.md` gives one path-neutral lifecycle and assurance table; `PUBLIC_RELEASE_UNIT.md` defines the dedicated-history contract. | Regenerate all receipts, build the dedicated Git release unit, bind the reviewed target/tree, and retain ordinary/optimized and negative-control evidence. |
| R8 — provenance and licences | Accepted | All 24 `SOURCE_PROVENANCE.json` records have explicit reference-only authorization status; two missing cited sources were frozen and hashed; `SOURCE_CONVENTION_AUDIT.md` records the Bautin semantic boundary; `LICENSE`, `LICENSE-CODE`, `LICENSES.md`, and `PUBLIC_DOMAIN.md` implement the component map. | Verify that no source snapshot bytes enter the public package and complete public-repository licence QA. |
| R9 — reader/accessibility layer | Accepted in manuscript/source | The manuscript has a reader orientation, README has a plain-language result table/glossary and real-limit-cycle exclusion, and bilingual notation was corrected. | Supply accessible HTML and complete PDF/site presentation QA. |

## Claim response

The repaired candidate does **not** claim three historically posed open
problems solved.  Its maximum wording is:

> Anonymous unrefereed theorem candidate containing two Atlas-family
> all-amplitude classifications and one ordinary coefficient-Bautin theorem
> candidate, supported by producer-side deterministic replay.

Independent theorem validation, specialist review, peer review, formal
verification, comprehensive priority, and independent reproduction remain
unresolved.  They are required before any corresponding assurance upgrade.

## Next and only model-review step

After a new manifest-bound archive is rebuilt and passes the complete replay
and publication-ready deterministic preflight, one confirmation review may
check R1-R9 against that new hash.  No further ordinary model-review round is
authorized.
