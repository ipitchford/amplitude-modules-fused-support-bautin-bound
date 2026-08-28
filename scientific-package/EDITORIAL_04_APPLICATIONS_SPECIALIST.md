# Applications and Cross-Disciplinary Review

## Scope, expertise, conflicts

- Reviewed only the frozen archive specified. SHA-256 verified exactly as `7e7f8f9b3d09feca0ea6019045d946dc4e845b73eb8bc7fe027aa3cea807f0d1`.
- Focus: accessibility, cross-disciplinary significance, plausible uses, anonymous unrefereed-candidate fit, reproducibility language, and risk of misleading a mathematically literate non-specialist.
- I did not inspect other reviewer reports or communicate with other reviewers.
- No known personal, institutional, or financial conflict. Author identity was unavailable.
- This is internal model-mediated review, not external peer review, independent specialist validation, or independent mathematical reproduction. I did not attempt specialist verification of the universal proofs or historical priority.

## Contribution summary

This is one integrated theorem-candidate paper containing:

1. Two Atlas-family classifications:
   - an all-amplitude Dickson module/rank classification;
   - an explicit fused-module classification for the known exceptional Ritt phase \((x^4+x)^3\).
2. One ordinary Taylor-coefficient Bautin theorem candidate:
   \(\mathcal B_\infty=\mathcal B_{d-1}\), hence
   \(b_{\mathrm{coeff}}(m)\le m-1\), with transfer to the cited source’s \(b(m)\) explicitly conditional on its ideal convention.
3. A supporting support-to-period-order bridge and reproducible symbolic benchmark.

It is not three historically posed open problems solved.

The cross-disciplinary link among polynomial monodromy, rapid-decay periods, twisted de Rham methods, creative telescoping, and zero-cycle Bautin ideals is intellectually credible. Its plausible uses are theoretical classification, prediction of complete-system differential-equation order, and exact symbolic benchmarking. The package does not establish an engineering application, a real planar limit-cycle bound, or a general applied cyclicity result.

## Findings

### Critical

None within this review remit.

### Major

1. **Prominent “SOLVED” and “re-review passed” wording can override the candidate disclaimers for non-specialists.**

   - `RESULT_PACKAGE_A.md:3-6`: “SOLVED AS A THEOREM CANDIDATE”.
   - `RESULT_PACKAGE_B.md:3-8`: “SOLVED AS A THEOREM CANDIDATE”.
   - `RESULT_PACKAGE_ZERO_CYCLE_BAUTIN.md:3-7`: “INTERNALLY SOLVED”.
   - `STATUS.md:4-10`: “major-revision response complete” and “targeted same-system re-review passed”, before clarifying the lack of independent specialist review.
   - The correct ceiling is stated well at `STATUS.md:134-142` and `CANDIDATE_MANUSCRIPT.md:3-9`, but readers should not have to reconcile competing status signals.

   Replace the banners with “candidate proof, internally checked” or equivalent. At every first-use status surface, state that review was internal and model-mediated. State prominently that A and B are Atlas-family classifications and C is the sole externally anchored coefficient-Bautin theorem candidate.

2. **The manuscript is not yet accessible to a mathematically literate non-specialist.**

   - `CANDIDATE_MANUSCRIPT.md:11-48` introduces Kummer channels, twisted de Rham quotients, cyclic rank, non-trace residues, parameter content and Melnikov orders without orientation.
   - `CANDIDATE_MANUSCRIPT.md:50-106` moves directly into four formal problems; the useful common finite-cover mechanism appears only at lines 98-106.
   - `CANDIDATE_MANUSCRIPT.md:1185-1212` explains technical significance but not what capability each theorem newly supplies or what it does not imply.

   Add a one-page reader’s guide defining phase, amplitude, channel/rank, zero-cycle and coefficient Bautin ideal; include one small example per headline result and a compact “known input / residual candidate / consequence / excluded inference” table. Explicitly say that no result here bounds real planar limit cycles.

3. **The checker’s claim-boundary text falsely implies replay when replay was not requested.**

   - `check_candidate_package.py:569-590` correctly records the replay flag and execution counters.
   - `check_candidate_package.py:591-595` nevertheless unconditionally says the receipt establishes “requested byte-identical replay”.
   - Running the contained checker with exact-root verification but without `--replay` produced `status=pass`, `replay_requested=false`, zero commands and zero artifact comparisons, while retaining that statement.

   The stored frozen receipt itself records a genuine replay (`PACKAGE_INTEGRITY_RECEIPT.json:13,31-208`), so this does not negate that receipt. The producer must nevertheless make its established-claims text conditional on `replay`, and a regression control should reject replay language when execution count is zero.

4. **The end-to-end reproduction route is too buried and development-path-specific.**

   - `README.md:51-72` gives the preprint build command but delegates release replay elsewhere.
   - The canonical lifecycle appears in `REFEREE_PACKET.md:143-166`.
   - Result dossiers use hard-coded `/tmp/csf-atlas-v070/...` paths, e.g. `RESULT_PACKAGE_A.md:37-47` and `RESULT_PACKAGE_B.md:53-61`.
   - `REPRODUCIBILITY_ENVIRONMENT.md:12-20` commendably discloses that the PDF build is not fully hermetic and that the external Atlas archive is required.

   Put one public replay procedure in the README: prerequisites, Atlas acquisition and hash verification, path-neutral commands, expected receipt fields, and the distinction among package identity, computational replay and independent mathematical reproduction.

### Minor

1. `CANDIDATE_PREPRINT.pdf` is visually legible and includes prominent candidate assurance, but its document properties report `Tagged: no`. Supply tagged PDF or accessible HTML alongside the machine-readable Markdown/TeX.

2. `BILINGUAL_ABSTRACT.md:21-29` and `:50-59` contain parenthetical notation such as `degree-(d)` rather than consistently delimited mathematics. Correct this before publishing the bilingual surface.

3. The manuscript explicitly says the licence, DOI and release URL are pending (`CANDIDATE_MANUSCRIPT.md:8-9`; `STATUS.md:130-132`). That is honest, but an actual release needs a package licence and explicit publication authorization.

## Recommendation

**Major Revision**

The integrated contribution is coherent enough for an anonymous unrefereed Evidence Press candidate, and the manuscript contains unusually good limitations, prior-art boundaries and assurance distinctions. Release now would nevertheless risk readers taking “SOLVED” and “re-review passed” as external validation, while the opening remains too specialist-dependent and the checker has a concrete replay-semantics defect.

**Confidence:** 4/5 for accessibility, applications, release framing and reproducibility language; 2/5 for theorem correctness and historical novelty, which lie outside this review’s specialist remit.

## Explicit release conditions

1. Put the exact boundary on the PDF first page, README, bilingual abstract and every result dossier: **two Atlas-family classifications plus one ordinary coefficient-Bautin theorem candidate; not three historically posed open problems solved**.
2. Remove prominent “SOLVED” labels and identify every simulated or same-system review as internal model-mediated review.
3. Fix the non-replay receipt wording, add a regression test, regenerate the manifest/receipt/archive, and rerun the full replay.
4. Add the non-specialist reader’s guide, examples, significance table and explicit non-application boundary.
5. Consolidate path-neutral end-to-end replay instructions in the README.
6. Add an explicit package licence and separate publication authorization.
7. Provide an accessible publication surface.
8. Do not upgrade the assurance beyond “anonymous unrefereed theorem candidate” without genuinely independent specialist proof review and a broader priority search.
