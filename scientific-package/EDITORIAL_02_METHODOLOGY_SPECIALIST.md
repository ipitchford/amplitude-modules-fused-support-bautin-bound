# Methodology Specialist Report

## Scope, expertise, conflicts

Reviewed only the frozen archive `amplitude-modules-fused-support-bautin-bound-v0.1.0-candidate-review.zip`. Its SHA-256 matches the supplied digest `7e7f8f9b3d09feca0ea6019045d946dc4e845b73eb8bc7fe027aa3cea807f0d1`. I did not edit files and excluded the packaged hostile review, panel synthesis, and other reviewer materials.

Expertise applied: algebraic and analytic proof architecture, monodromy representations, symbolic computation, coefficient ideals, and reproducibility. No personal or financial conflict is possible. The material and review were handled in the same model-mediated research environment, however, so this is **internal model-mediated review only**, not independent human peer review or independent reconstruction.

## Summary assessment

The manuscript has a coherent dependency structure:

\[
\text{formal moment/support theorem}
\rightarrow
\text{projector descent}
\rightarrow
\text{Dickson and exceptional-Ritt classifications},
\]

while the coefficient-Bautin theorem is independent and proceeds through Lagrange–Bürmann, derivative injectivity, and Cayley–Hamilton.

Several parts are notably strong. The formal transform and corrected falling-factorial Wronskian in `CANDIDATE_MANUSCRIPT.md:296-386` are carefully designed; the polynomial projector descent in `CANDIDATE_MANUSCRIPT.md:457-484` addresses the lattice issue that bare dimension counting would miss; the Dickson quadratic obstruction in `CANDIDATE_MANUSCRIPT.md:541-583` is uniform in degree and nonzero parameter; and the exceptional trace filter plus CRT fusion in `CANDIDATE_MANUSCRIPT.md:637-713` gives a convincing all-coefficient-degree argument. The Bautin proof in `CANDIDATE_MANUSCRIPT.md:947-1068` also appears structurally sound **for the explicitly defined ordinary parameter-content/Taylor-coefficient ideal**.

The package correctly distinguishes finite checks from proof. Nevertheless, one load-bearing equivalence in the support theorem is under-explained, the mapping to the source problem remains conditional and unauditable from this archive, and the full replay is not self-contained.

## Critical findings

No Critical defect was established in this scoped review. This is not a positive proof certification.

## Major findings

### M1. The proof does not explicitly bridge the local Fourier span to the manuscript’s full monodromy-orbit definition

**Locations:** `CANDIDATE_MANUSCRIPT.md:274-293`, `388-398`; `THEOREM_H_SUPPORT_RANK.md:231-245`; consumed at `THEOREM_0_MONODROMY_BLOCKS.md:160-170`.

The manuscript defines the reduced root-value quantity as the span of the **full monodromy orbit of a root-value vector**. The proof then Fourier-transforms the locally labelled inverse germs \(G(x_j(t))\) and proves that their local conjugate-function or inertia-orbit span has dimension \(|\Sigma|\). The equivalence between these two representations is not stated or proved. It is subsequently used to assert that every nonzero projected polynomial has the full irreducible \(\Gamma\)-block, making this a load-bearing gap with a possible appearance of circularity.

**Remedy:** Insert an equivariant lemma comparing:

1. the \(\mathbf C\)-span of the conjugate germs \(G(x_j)\) in the splitting field;
2. the full \(\Gamma\)-orbit span of the root-value vector;
3. the inertia-cycle Fourier span; and
4. their ranks after generic specialization.

Explicitly show that vanishing Fourier relations analytically continue through every monodromy element, or prove the equivalence via the rank of the \(\Gamma\)-equivariant evaluation map. Then invoke that lemma before projector descent.

### M2. The claimed connection to the published Bautin problem remains a conditional semantic translation, not a verified source match

**Locations:** `CANDIDATE_MANUSCRIPT.md:902-945`, `1089-1096`; `THEOREM_D_BAUTIN_BOUND.md:60-97`, `117-124`; `SOURCE_PROVENANCE.json:276-290`, `308-322`.

Proposition 6.1 convincingly identifies parameter content with a local Taylor-coefficient ideal in \(R=\mathbf C[\boldsymbol a]\). It does not establish that this is the ambient ideal intended by source [17]. The manuscript acknowledges this and conditions the “answers Problem 8.4” statement appropriately. However, the frozen source snapshots are not in the review archive: provenance points to `/tmp/csf-zero-2312/source.tar` and `/tmp/csf-prior-art-1411/source.tar`. Therefore the source definition, contraction, localization, branch aggregation, radicalization, and base-point semantics cannot be audited from the frozen submission.

**Remedy:** Either:

- include an exact source-definition excerpt and a formal translation lemma specifying ambient ring, coefficient extraction, determinations, contraction, localization, and order of radicalization; or
- present Theorem C solely as the standalone \(b_{\mathrm{coeff}}\) theorem and remove any suggestion beyond the current explicit conditional that it resolves the source problem.

### M3. The standard-ray/full-rank realization needs a complete analytic lemma

**Locations:** `CANDIDATE_MANUSCRIPT.md:400-438`; `THEOREM_H_SUPPORT_RANK.md:247-319`; used in `CANDIDATE_MANUSCRIPT.md:815-851`.

The ray matrix and its Vandermonde rank are plausible and algebraically clear. What remains compressed is the analytic passage: construction of an \(s\)-flat rapid-decay cycle family over the sector, proof that the consecutive rays give the stated homology basis for the general centred phase, uniform domination after \(u=s^{1/d}x\), and identification of actual period monodromy with the formal Kummer characters. These steps support the cycle-contact statement and hence the lower bound in (5.4).

**Remedy:** Add a lemma with the flat family, orientation, Stokes-sector restrictions, uniform convergence estimate, basis proof or precise citation, and the pairing identification. This issue affects the supporting cycle-specific theorem, not the Dickson, Ritt, or Bautin headline results.

### M4. Full replay is not independently executable from the frozen submission

**Locations:** `README.md:66-72`; `REPRODUCIBILITY_ENVIRONMENT.md:17-20`; `PACKAGE_MANIFEST.json:2`; `check_candidate_package.py:260-459`, especially `571-577`.

The archive-contained exact-root integrity check passes. I also reproduced byte-identically:

- support/rank receipt, ordinary and `-O`;
- exceptional channel-independence receipt;
- Bautin content-bridge receipt;
- general Bautin receipt;
- power-phase Bautin receipt;
- standalone weighted-order receipt, ordinary and `-O`;
- generated TeX and PDF.

The Atlas-dependent Dickson, exceptional-amplitude, producer-oracle, mutation, and stored full-replay checks could not be rerun because the separately frozen Atlas archive is required but not included.

**Remedy:** Supply the exact Atlas archive as a frozen supplementary input, or provide archive-contained standalone replacements for every Atlas-dependent computation. Run and retain the full command using `--replay`, `--atlas-archive`, `--exact-root`, and `--verify-stored-receipt`.

## Minor findings

- Make the precise topological vector space/domain of the bounded-above Laurent transform and its \(K_0\)-linear extension explicit at `CANDIDATE_MANUSCRIPT.md:311-350`.
- State explicitly that affine normalization preserves \(q\), non-trace residue support, and generic root-span.
- Correct the unmatched TeX delimiter at `CANDIDATE_MANUSCRIPT.md:1438`.

## Recommendation

**Major Revision**

The main algebraic architecture is promising and the Bautin argument is strong under its stated coefficient convention. Acceptance should wait for the root-span/monodromy equivalence to be written without ambiguity, the source convention to be either established or strictly separated, the standard-ray analytic lemma to be completed, and the full frozen replay to become independently executable.

## Confidence

**4/5 — high** for proof architecture, exact-computation boundaries, and reproducibility assessment; **moderate** for the intended source-ideal interpretation because the actual frozen source bytes were unavailable in the submission.

## Release conditions

1. Add and independently check the equivariant root-span/monodromy lemma.
2. Complete or precisely cite the standard-ray analytic realization.
3. Establish the exact source-ideal translation or retain the result solely as \(b_{\mathrm{coeff}}\).
4. Provide and rerun the complete frozen replay input set.
5. Obtain independent human specialist review of both the monodromy/support proof and the Bautin ideal convention.
6. Continue describing finite computations, receipt replay, internal review, and theorem proof as distinct assurance levels.
