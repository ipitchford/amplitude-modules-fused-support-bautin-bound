# Evidence Press R2 Confirmation Review

## Scope, expertise, and conflicts

I performed the single bounded confirmation review of only:

- `amplitude-modules-fused-support-bautin-bound-v0.1.0-candidate-r2.zip`
- `amplitude-modules-r2-fast-gates-receipt.json`
- The bundled R1–R9 control documents, `EDITORIAL_06_SYNTHESIS.md` and `REVIEW_RESPONSE_MATRIX.md`

I did not conduct a new novelty search or inspect separate reviewer reports. This is an internal model-mediated review, not external peer review, independent specialist validation, legal clearance, or independent reproduction. I have no human professional credentials, and the shared model/repository environment is an independence limitation.

The candidate remains explicitly bounded: it is not three historically posed open problems solved.

## Identity and gate verification

- Required R2 ZIP SHA-256: `aa1e73f62ccb89bae6ff00aaee844721172eca515d4da64c4c41539e51977b13`
- Observed R2 ZIP SHA-256: exact match
- Fast-gate receipt physical SHA-256: `519a14c21672d8ab987f061ad7861b92130ea436ac08f34c919dc5468a8c1583`
- Fast-gate result: 8/8 commands passed
- Bound Git head: `52504ae815f61841325c6cda3b414d69dd55c702`
- Stored full-replay receipt:
  - 13 executed commands
  - 14 artifact comparisons
  - 14 replay records
  - 72 manifest entries
  - all 14 comparisons byte-identical
- Ordinary and optimized no-replay checks independently passed with:
  - `replay_requested=false`
  - `command_execution_count=0`
  - `artifact_comparison_count=0`

The replay-claim correction is therefore effective: the checker no longer describes zero-execution validation as byte-identical replay.

## R1–R9 confirmation

- **R1 — root-span/monodromy:** Addressed. `CANDIDATE_MANUSCRIPT.md:403-475` and `THEOREM_H_SUPPORT_RANK.md:245-325` now supply the finite exceptional set, multiplicity-free inertia decomposition, nonvanishing evaluation on each irreducible summand, and the equivariant orbit-span argument. Theorem B invokes it at `CANDIDATE_MANUSCRIPT.md:762-769`.
- **R2 — standard-ray family:** Addressed. `CANDIDATE_MANUSCRIPT.md:478-557` and `THEOREM_H_SUPPORT_RANK.md:329-421` construct the rotating flat family, orientations, sole relation, asymptotics, continuation action, and character pairing for the stated standard consecutive rays.
- **R3 — governance:** Partially addressed; residual release-binding defects remain below.
- **R4 — stale claims:** Addressed scientifically. The general Dickson block-mass equality is explicitly disclaimed in `NOVELTY_AUDIT.md:368-379` and `CANDIDATE_MANUSCRIPT.md:983` onward. The Bautin statement is consistently conditional.
- **R5 — problem provenance:** Addressed. `README.md:28-31` and `CANDIDATE_MANUSCRIPT.md:13-14,69-70` identify A and B as Atlas-family classifications and C as externally motivated, not three historical open problems.
- **R6 — Ritt locator:** Addressed. `CANDIDATE_MANUSCRIPT.md:704-722` displays
  `X^3∘(X^4+X)=(X(X+1)^3)∘X^3`
  and points to `[6, Theorems 2.2(1) and 2.3(1)]`.
- **R7 — replay and release binding:** Replay semantics and exact receipt counts are repaired, but mandatory release evidence remains incomplete.
- **R8 — authorization/licences:** The structural gate reports 24/24 sources as `AUTHORIZED_REFERENCE_ONLY_NOT_REDISTRIBUTED`, with unique source IDs. `LICENSES.md:3-15` separates CC0 prose/data, MIT code, reference-only citations, the separately distributed Atlas input, and review-report provenance. This is package-contract confirmation, not independent legal validation.
- **R9 — reader/accessibility:** The reader guide, glossary, and explicit real-planar-limit-cycle exclusion are present in `README.md:26-48`. The required accessible delivery artifact is not complete.

## Residual findings

### Critical

None.

### Major

1. **R7: Required JUnit replay evidence is absent.**  
   The archive contains no JUnit/XML artifact or equivalent uniquely identified ordinary/optimized testcase inventory. This leaves the repository’s package-replay requirement—and R7’s ordinary/optimized parity evidence—unfulfilled despite the passing JSON receipts.

2. **R7/R3: The frozen release binding remains pre-confirmation and does not bind this R2 archive as the reviewed release target.**  
   `EDITORIAL_DISPOSITION.json` still records the prior R1 target, `MAJOR_REVISION_HOLD_FOR_REPAIR`, `implementation_complete_pending_rebuild_and_preflight`, and confirmation pending. `PACKAGE_MANIFEST.json` does not directly record the R2 ZIP digest, reviewed commit/tree, dependency description, and final confirmation disposition as a single coherent release binding. `PUBLIC_RELEASE_UNIT.md:3-25` describes these as work still required before tagging.

3. **R9: Accessible HTML is absent and the PDF is untagged.**  
   The ZIP has no HTML artifact; `pdfinfo` reports `Tagged: no`. This is the same unresolved item acknowledged at `REVIEW_RESPONSE_MATRIX.md:25`, while `EDITORIAL_06_SYNTHESIS.md:140` requires accessible HTML alongside the PDF. Markdown source improves inspectability but does not satisfy that explicit delivery condition.

### Minor

1. `STATUS.md:145-146` still says no licence statement has been created, although the archive now contains `LICENSE`, `LICENSE-CODE`, and `LICENSES.md`.
2. The fast-gate receipt binds the Git head and manifest hash but does not itself record the R2 archive SHA-256. This can be repaired in the final confirmation/release receipt without changing the scientific manuscript.

## Recommendation

**HOLD**

Confidence: **0.94 overall**; high confidence in the archive identity, receipt counts, absent HTML/JUnit evidence, and stale release binding; moderate-high confidence that the R1 and R2 textual repairs close the specified editorial objections within their stated scopes.

The hold is based on concrete R7/R9 release-contract defects, not on the remaining lack of external specialist review, priority adjudication, or peer review. Those remain candidly disclosed assurance dimensions and are not, by themselves, grounds for this hold.

## Explicit release conditions

Release as an **Anonymous, unrefereed Evidence Press candidate** only after:

1. Retaining JUnit evidence with unique testcase identities, exact aggregate parity, and matching ordinary/optimized inventories, including the required negative controls.
2. Creating a final immutable confirmation/release record that binds the R2 ZIP hash, reviewed Git commit/tree, scientific target, manifest, dependency description, claim/case identifiers, disposition, allowlist, and public-release-unit declaration.
3. Providing accessible HTML alongside the PDF and completing presentation/accessibility QA.
4. Reconciling the stale licence and preflight wording without strengthening any scientific, novelty, priority, or validation claim.
5. Preserving the explicit wording that this is an anonymous unrefereed candidate, internally model-reviewed, not externally validated, and not three historically posed open problems solved.
