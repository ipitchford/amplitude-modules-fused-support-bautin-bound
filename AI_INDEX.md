# AI index — amplitude-modules-fused-support-bautin-bound

## Identity and version

Documentation addendum: 2026-09-24. Indexes [source commit c860333d3a1a](https://github.com/ipitchford/amplitude-modules-fused-support-bautin-bound/tree/c860333d3a1ab513834a613854bd9da28d2b15b4) and candidate tag `v0.1.0-candidate`. This index was added after that release: it is **not** part of the original tag, DOI archive or frozen manifest. Existing release files and checksums remain unchanged. For historical manifest/allow-list checks, use a clean checkout of that tag, not this documentation-enriched branch. The addendum is authenticated by Git history.

[Release identity and DOI](README.md) · [Evidence Press context](https://evidencepress.org/releases/amplitude-modules-fused-support-bautin-bound/)

## Exact scope

Candidate classifications for polynomial amplitudes of nondegenerate Dickson phases and fused support for P=(x^4+x)^3, plus b_coeff(m) ≤ m−1 for the defined ordinary coefficient Bautin index. Transfer to a historical b(m) is conditional on matching conventions; this is not three settled historical open problems.

The linked manuscript and claim register control all hypotheses and quantifiers; this index is a navigation aid, not a substitute proof.

## Claim and evidence map

- [scientific-package/CANDIDATE_MANUSCRIPT.md](scientific-package/CANDIDATE_MANUSCRIPT.md) — Exact definitions and statements.
- [CLAIMS.json](CLAIMS.json) — Claim register.
- [ASSURANCE.md](ASSURANCE.md) — Assurance.
- [REPRODUCE.md](REPRODUCE.md) — Commands and replay boundary.
- [scientific-package/REPLAY_INPUTS.json](scientific-package/REPLAY_INPUTS.json) — External Atlas input identity.
- [scientific-package/REPLAY_REQUIREMENTS.txt](scientific-package/REPLAY_REQUIREMENTS.txt) — Full replay requirements.
- [PROVENANCE.md](PROVENANCE.md) — Provenance.
- [LICENSES.md](LICENSES.md) — Rights.

## Reproduce

From the indexed release root, after inspecting the commands and installing the documented environment:

```sh
python3 scientific-package/check_candidate_package.py --root scientific-package --exact-root
```

This command checks package semantics, not scientific replay. Full replay needs the separately released hash-bound Atlas archive and the environment in scientific-package/ENVIRONMENT.txt. The recorded full replay has 13 commands and 14 byte-identical comparisons.

## Trust boundary and safe reuse

Internal deterministic replay and model-mediated review do not establish independent specialist validation or formal verification. Support-to-order infrastructure is not a fourth headline result.

No new mathematical validation, formalisation, independent reproduction or novelty audit was performed for this documentation repair. Preserve the anonymous attribution and existing citation metadata. Distinguish producer checks, finite formal results, universal written arguments and external review. Before downstream reuse, match the exact statement and dependency scope and check subsequent corrections; a DOI or successful command alone is not proof of correctness.

## Licence and provenance

Use the rights/provenance sources linked above and [README](README.md); cited and third-party material retains its own terms. This new index is dedicated under CC0-1.0, without changing any existing licence or attribution.

