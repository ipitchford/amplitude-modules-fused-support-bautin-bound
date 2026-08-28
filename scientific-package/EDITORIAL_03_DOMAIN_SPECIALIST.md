## Domain Specialist Report

**Submission:** `amplitude-modules-fused-support-bautin-bound-v0.1.0-candidate-review.zip`  
**Verified SHA-256:** `7e7f8f9b3d09feca0ea6019045d946dc4e845b73eb8bc7fe027aa3cea807f0d1`

### Scope, expertise, and conflicts

I reviewed the frozen manuscript, theorem dossiers, problem-selection/novelty records, and source-provenance metadata. I did not inspect `BAUTIN_HOSTILE_REVIEW.md`, `PANEL_REVIEW_SYNTHESIS.md`, `REFEREE_PACKET.md`, or other reviewer reports.

My review scope covers algebraic analysis, polynomial covers and monodromy, Dickson/Ritt decomposition, twisted de Rham cyclic modules, zero-cycle Melnikov functions, and coefficient Bautin ideals. Exhaustive historical priority and the intended ambient ideal in source [17] are outside what can be established from the frozen package alone.

No personal or financial conflict is applicable. There is an important procedural limitation: this is **internal model-mediated review only**, not independent human specialist review or peer review.

### Summary

The mathematical core is promising and unusually careful about its assurance ceiling. The Dickson classification is supported by a clean free-module decomposition and a convincing nonsquare-discriminant argument preventing loss of either paired channel. The repaired exceptional Ritt result now has a credible all-degree mechanism: quartic \(S_4\) irreducibility supplies all non-trace quartic modes, while the fibre-trace calculation and mod-\(3\) grading isolate the three claimed degree-twelve blocks. The coefficient-Bautin result is the strongest general theorem: the all-order Lagrange–Bürmann formula, injectivity of differentiation on zero-cycle polynomial integrals, and Cayley–Hamilton recurrence form a coherent proof of \(\mathcal B_\infty=\mathcal B_{d-1}\).

I found no explicit counterexample or fatal theorem error. The main obstacles are journal-level proof presentation and claim provenance. The load-bearing support theorem is too compressed in the manuscript, the abstract incorrectly groups all three results as Atlas-derived, and the exceptional Ritt “collision” is not actually displayed. Residual novelty remains bounded and cannot support priority.

### Critical findings

**None identified.**

### Major findings

1. **The load-bearing support theorem needs a fuller journal-level proof.**  
   **Location:** `CANDIDATE_MANUSCRIPT.md`, lines 287–398, especially 302–350 and 388–398.  
   **Issue:** The theorem appears mathematically coherent, and the separate `THEOREM_H_SUPPORT_RANK.md` supplies useful detail, but the manuscript compresses several essential steps into “after affine normalization” and “formal integration by parts.” It also jumps quickly from Fourier components to the reduced monodromy-orbit span. Since Theorems A and B depend on this result, the published paper itself should carry the full argument.  
   **Remedy:** Add the affine-invariance calculation; display the monomial identity
   \[
   (r+nd)\mu_{r,n}+d\mu_{r,n+1}=0;
   \]
   verify connection compatibility explicitly; and state that the inertia orbit alone recovers every nonzero Fourier eigenspace, so its span already has dimension \(|\Sigma|\), hence so does the full monodromy orbit.

2. **The abstract conflates two Atlas subproblem classifications with the externally motivated Bautin theorem.**  
   **Location:** `CANDIDATE_MANUSCRIPT.md`, lines 13–14; `BILINGUAL_ABSTRACT.md`, lines 9–10 and 43–44. Compare the correct distinction at manuscript lines 67–82.  
   **Issue:** A and B are indeed Atlas-internal family/subproblem classifications. C is an independently published degree-box question from [17], with only the coefficient-ideal interpretation resolved here. Saying that all three candidates were “suggested by” or “arise from” the Atlas obscures problem provenance.  
   **Remedy:** Replace this with: “We study two Atlas-derived amplitude-classification subproblems and one externally posed zero-cycle Bautin problem.” Preserve the same distinction in both languages.

3. **The exceptional Ritt collision is named but not exhibited as a collision.**  
   **Location:** `CANDIDATE_MANUSCRIPT.md`, lines 76–78, 212–215, and 585–700.  
   **Issue:** The manuscript gives \(P=(x^4+x)^3\) but never displays the two inequivalent decompositions:
   \[
   P=X^3\circ(X^4+X)=\bigl(X(X+1)^3\bigr)\circ X^3.
   \]
   This weakens the polynomial-decomposition exposition and makes the relationship to imported source [6] unnecessarily opaque.  
   **Remedy:** Display both decompositions, give the exact theorem/proposition locator in [6], and state explicitly that the new claim is the amplitude-module/support classification, not the Ritt collision or monodromy group.

4. **Residual novelty and priority are not independently established.**  
   **Location:** `CANDIDATE_MANUSCRIPT.md`, lines 192–260 and 1239–1263; `NOVELTY_AUDIT.md`, lines 59–137 and 139–324.  
   **Issue:** The manuscript is commendably conservative, but the frozen evidence is a bounded search, with acknowledged blind spots and source snapshots referenced outside the archive. Result A is close to Pakovich’s Chebyshev theorem; B imports the exact collision and its monodromy; C is close to general recurrence/Bautin-ideal theorems. The residual units are plausible, but priority is unresolved.  
   **Remedy:** Before journal submission, conduct independent specialist searches through MathSciNet, zbMATH, citation chains, and non-English literature; add exact theorem/page locators for every imported result; retain “not located in a bounded search” unless stronger evidence is obtained.

### Minor findings

- **Define “nondegenerate” in the abstract.** At `CANDIDATE_MANUSCRIPT.md`, lines 21–23, write “\(a\ne0\)” directly.
- **Repair malformed mathematics.** `CANDIDATE_MANUSCRIPT.md`, line 1438 has “group is `(S_{N/h}`”; use \(\,S_{N/h}\,\).
- **Repair abstract math delimiters.** `BILINGUAL_ABSTRACT.md`, lines 21–24 and 50–51 use plain `(d)` rather than \(d\).
- **Sharpen terminology on cycle coefficients.** At manuscript lines 1070–1087, retain the distinction between integral zero-cycles and complexified cycle modules wherever “sharp” is mentioned, including abstracts and conclusions.

### Requested classification checks

- **A/B:** Verified. The body correctly treats them as two explicit Atlas-family/subproblem classifications, not as two independently sourced named open problems (`CANDIDATE_MANUSCRIPT.md`, lines 67–78; `STATUS.md`, lines 134–142). The abstract wording should be corrected as above.
- **C and \(b(m)\):** Verified. The unconditional theorem is for the explicitly defined \(b_{\mathrm{coeff}}(m)\). Identification with source [17]’s \(b(m)\) is consistently conditional in the main abstract, prior-art discussion, Theorem C, convention boundary, README, status, and bilingual abstract. That boundary must remain unchanged.

### Recommendation

**Major Revision**

This is not a rejection: I found the theorem arguments coherent enough to justify revision and independent specialist review. Major revision is warranted because the load-bearing proof needs expansion, problem provenance must be corrected at abstract level, the Ritt decomposition should be explicit, and novelty/priority remain unresolved.

### Confidence

**3/5 overall.**

- Internal theorem-coherence assessment: **4/5**
- Exhaustive novelty/priority assessment: **2/5**
- Identification of source [17]’s exact \(b(m)\) convention: **2/5**

### Release conditions

Before any journal-like or publication-ready release:

1. Complete the four major revisions above.
2. Keep A/B labelled Atlas-subproblem classifications.
3. Keep \(b_{\mathrm{coeff}}(m)\le m-1\) unconditional only for the manuscript’s defined coefficient ideal, and any statement about source \(b(m)\) explicitly conditional.
4. Obtain independent human specialist review of both the support/monodromy proofs and the zero-cycle Bautin argument.
5. Complete an independent priority review and update the claim ceiling without asserting priority from search absence.
6. Do not describe this report as peer review or independent validation; it is **internal model-mediated review only**.
