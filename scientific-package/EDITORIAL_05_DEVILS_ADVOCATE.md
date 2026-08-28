# Devil’s-Advocate Review

## Scope, expertise, and conflicts

- Reviewer: `/root/publication_adversary`, model-mediated mathematical and release-governance reviewer.
- Frozen target: `amplitude-modules-fused-support-bautin-bound-v0.1.0-candidate-review.zip`.
- Verified SHA-256: `7e7f8f9b3d09feca0ea6019045d946dc4e845b73eb8bc7fe027aa3cea807f0d1` — exact match.
- Read-only review. I did not edit the package.
- I did not open `BAUTIN_HOSTILE_REVIEW.md`, `PANEL_REVIEW_SYNTHESIS.md`, `REFEREE_CONFIGURATION.md`, `REFEREE_PACKET.md`, or other reviewers’ reports.
- Inspected: manuscript, theorem/dossier files, novelty records, manifests, provenance, receipts, and checker source. Tools were `shasum`, selective `unzip`, `rg`, `nl`, `jq`, and read-only `--help` execution.
- The package does not identify a reviewed Git commit or case ID, so I cannot supply them in the independence declaration.
- Conflict/assurance statement: this is an internal model-mediated review, not external peer review, independent specialist validation, or independent institutional reproduction.

## Summary

The package has real strengths: Theorem C’s Cayley–Hamilton/monodromy argument is coherent on its explicitly defined ordinary coefficient ideal; the Dickson and exceptional modules are stated precisely; failed claims are preserved; and the manuscript repeatedly distinguishes bounded computation, proof, novelty, review, and release.

Publication should nevertheless remain blocked. A load-bearing root-span equality changes mathematical objects between the standalone theorem and the manuscript without proving their equivalence, and that equality is then used in the monodromy-block argument and Theorem B. Separately, the archive cannot satisfy this repository’s release contract: it lacks commit/case/scientific-target binding, source authorization statuses, a public-release-unit declaration, a complete offline source corpus, and the required single lifecycle/JUnit replay evidence. The novelty dossier also retains an exact Dickson block-mass claim explicitly demoted elsewhere.

The defensible contribution ceiling remains: one integrated unrefereed candidate containing two Atlas-family classifications, one ordinary coefficient-Bautin theorem candidate, and one supporting bridge. It is not three historically posed open problems solved.

## Strongest counter-argument

The strongest case against acceptance is that the package’s most important equality is not frozen consistently. `CANDIDATE_MANUSCRIPT.md:274-294` defines reduced root-value span as the span of the monodromy orbit of a specialized numerical vector. Its proof at `388-398`, however, establishes independence of Fourier-projected algebraic functions. `THEOREM_H_SUPPORT_RANK.md:44-56,231-245` states and proves the latter constant-span object, not the former monodromy-orbit object. These quantities may be equivalent at a suitably generic fibre, but that equivalence requires an explicit equivariant rank/specialization lemma and an excluded-locus argument. None is supplied. The manuscript then uses the disputed equality at `486-489` to force complete monodromy blocks and at `631-635` to establish all three quartic channels in Theorem B. Consequently, deterministic checks of selected inverse-series and Krylov cases do not close the logical chain.

Even if repaired mathematically, the archive is not a release unit under the repository contract. Its checker authenticates bytes and required phrases, not semantic coherence, source authorization, Git-tree identity, or a complete offline evidence corpus. A passing receipt therefore cannot support publication readiness.

## Critical findings

### C1 — Root-span definition mismatch leaves a load-bearing proof gap

- Locations: `CANDIDATE_MANUSCRIPT.md:274-294,388-398,486-489,631-635`; `THEOREM_H_SUPPORT_RANK.md:44-56,231-245`.
- Evidence: the manuscript defines a generic specialized monodromy-orbit span, while the standalone theorem proves the constant span of conjugate algebraic functions using Fourier inversion.
- Reproducible check: compare the two definitions and the final paragraphs of their respective proofs.
- Impact: the root-span equality, general block theorem, and Theorem B’s “all three quartic channels” step are not established as written.
- Required repair: freeze one exact object; prove an equivariant generic-specialization lemma showing equality with the monodromy-orbit span, including the exceptional locus, or narrow the manuscript claim and repair every dependent theorem. Subject the replacement proof to fresh independent specialist review.

### C2 — The artifact cannot satisfy the repository’s public-release contract

- Locations: `PACKAGE_MANIFEST.json:1-4`; `check_candidate_package.py:80-87,134-148,491-542`; `PACKAGE_INTEGRITY_RECEIPT.json:3-10,26-32`; `REPRODUCIBILITY_ENVIRONMENT.md:12-26`; `REPLAY_REQUIREMENTS.txt:1`; archive root listing.
- Evidence:
  - No case ID, claim ID, reviewed commit, Git-tree digest, scientific-target digest, or dependency-lock digest is present.
  - The checker’s closed manifest schema does not permit those bindings.
  - `PUBLIC_RELEASE_UNIT.md` and a package licence are absent.
  - Replay is 13 separate commands plus two render comparisons, not the required single exact lifecycle argv with ordinary/optimized JUnit inventory parity.
  - The required Atlas archive is external to the ZIP.
- Impact: exact bytes are authenticated, but the reviewed Git state, scientific target, full-history release unit, and detached offline lifecycle are not.
- Required repair: create a new package schema binding the case, claim, reviewed commit/tree, target digest, dependency lock, command vector, retained results, structured review disposition, and complete lifecycle/JUnit evidence; include the public-release-unit declaration and perform whole-history privacy, credential, and legal review.

### C3 — Every provenance record lacks the mandatory authorization status

- Locations: `SOURCE_PROVENANCE.json:2-19` and identically across all 22 source records; examples at `21-50` and `53-66`.
- Evidence: records include an `authorization_basis` but no `authorization_status`. Several licence fields explicitly say redistribution was not assessed or the page licence was not inferred.
- Impact: under repository rule 8, unknown authorization blocks packaging regardless of the presence of a licence label.
- Required repair: add schema-validated exact-snapshot authorization status and basis for every source; fail closed on unknown/escalated status; resolve the manuscript/package’s own licence separately.

## Major findings

### M1 — A stale exact Dickson block-mass claim contradicts the controlling theorem

- Locations: `NOVELTY_AUDIT.md:367-377`; contrary statements at `RESULT_PACKAGE_C.md:37-50`, `THEOREM_C_WEIGHTED_ORDER.md:206-217`, and `CANDIDATE_MANUSCRIPT.md:848-851`.
- Evidence: the novelty audit says there is “exact block-mass order for Dickson ray-cycles”; all three controlling mathematical files say no general Dickson block-mass equality is retained.
- Impact: the packaged novelty/claim record overstates the supporting result.
- Required repair: delete the exact-equality wording or supply the missing scalar differential-module proof. Regenerate manuscript derivatives, manifest, receipts, and review target hashes.

### M2 — Two load-bearing prior-art citations are not bound to provenance records

- Locations: `CANDIDATE_MANUSCRIPT.md:217-219,1322-1329`; `NOVELTY_AUDIT.md:100-103`; complete `SOURCE_PROVENANCE.json`.
- Evidence: Chen–Kauers arXiv:1108.4508 and Bostan–Lairez–Salvy arXiv:1301.4313 are cited for order-aware/reduction-based creative telescoping but have no frozen provenance entries.
- Impact: those source-dependent prior-art assertions lack inspectable frozen targets in the package.
- Required repair: freeze and hash the exact cited versions with coverage, exclusions, transformations, licence, authorization status, and citation anchors, or remove the assertions.

### M3 — “Independently recomputed” is an unbound assurance claim

- Location: `PROBLEM_SELECTION_GATE.md:43-47`; contrast `STATUS.md:111-126,140-142`.
- Evidence: Results A and B are described as “reportedly independently recomputed,” but no independent specialist or institutional reconstruction is established; the package elsewhere acknowledges only same-programme/model-mediated checking.
- Impact: readers could misclassify an internal/model check as independent validation.
- Required repair: identify the exact actor, method, target digest, and independence class, or replace the phrase with “separate model-mediated/internal computation.”

## Minor findings

### m1 — Source timestamps are not exact

- Location: `SOURCE_PROVENANCE.json:13` and corresponding `retrieved_at` fields throughout.
- Evidence: “2026-08-27; exact time not recorded.”
- Impact: weakens audit ordering and supersession evidence.
- Repair: use caller-supplied UTC timestamps in the next frozen provenance version.

### m2 — Dependency capture is insufficient for detached byte-identical replay

- Locations: `REPLAY_REQUIREMENTS.txt:1`; `REPRODUCIBILITY_ENVIRONMENT.md:6-15`.
- Evidence: only `sympy==1.14.0` is machine-pinned; Python, Pandoc, TeX, fonts, locale, and transitive dependencies are descriptive.
- Impact: stored byte parity is credible for the recorded host but not reproducibly locked for a detached consumer.
- Repair: add hash-locked dependencies and a reproducible toolchain/container specification, or lower the byte-identical replay claim.

## Recommendation

**Major**

The mathematical issues appear potentially repairable, so I do not recommend outright rejection. Acceptance or minor revision is impossible while C1–C3 remain unresolved.

Confidence: **high (0.88)** for the internal inconsistencies and governance defects; **moderate-high (0.75)** for the mathematical severity because this review did not consult external sources or receive independent specialist verification.

## Explicit release conditions

Release requires all of the following:

1. Repair and independently review the root-span/monodromy-orbit equivalence and all dependent uses.
2. Remove or prove the stale Dickson block-mass equality.
3. Bind every cited source to a frozen, inspectable provenance target.
4. Add validated authorization statuses and resolve licences for every redistributed or relied-upon snapshot.
5. Bind a new package to one case, exact claim, reviewed Git commit/tree, target digest, dependency lock, and structured adversarial disposition.
6. Add `PUBLIC_RELEASE_UNIT.md`, an explicit top-level allowlist, and documented whole-history privacy, credential, and legal review.
7. Supply one exact offline lifecycle command with ordinary/optimized testcase parity and retained JUnit/result artifacts.
8. Regenerate all derived files, hashes, receipts, and review records after repairs.
9. Obtain genuine independent specialist reviews of the support theorem, exceptional Ritt classification, and coefficient-Bautin theorem, plus a broader specialist novelty assessment.
10. Preserve the claim ceiling: this package does not establish three historically posed open problems solved, peer review, independent validation, priority, or authorization to publish.

<oai-mem-citation>
<citation_entries>
MEMORY.md:54-71|note=[used prior candidate boundary and known channel-order failure to preserve assurance scope]
</citation_entries>
<rollout_ids>
01a042e2-9c88-7113-88dd-a43adac95085
</rollout_ids>
</oai-mem-citation>
