# Amplitude modules, fused support, and a coefficient-Bautin bound

This repository publishes version `0.1.0-candidate` of an **anonymous,
unrefereed theorem candidate** about polynomial phases. It contains two
Atlas-derived amplitude-classification candidates and one externally motivated
ordinary coefficient-Bautin theorem candidate.

The release does **not** establish that three historically posed open problems
have been solved. It has deterministic internal replay and a documented
model-mediated editorial process, but no independent specialist validation,
journal peer review, formal verification, settled priority, or submission.

Versioned record: [10.5281/zenodo.22143919](https://doi.org/10.5281/zenodo.22143919)

All versions: [10.5281/zenodo.22143918](https://doi.org/10.5281/zenodo.22143918)

## Read the candidate

- [Accessible HTML](release-assets/CANDIDATE_PREPRINT.html)
- [PDF](scientific-package/CANDIDATE_PREPRINT.pdf)
- [Manuscript source](scientific-package/CANDIDATE_MANUSCRIPT.md)
- [Claim and assurance boundary](ASSURANCE.md)
- [Reproduction instructions](REPRODUCE.md)

## What is claimed

1. A cyclic-rank classification for polynomial amplitudes of nondegenerate
   Dickson phases.
2. A fused-support classification for the exceptional collision
   `P=(x^4+x)^3`.
3. A bound `b_coeff(m) <= m-1` for the explicitly defined ordinary
   coefficient Bautin index. Transfer to a cited source's terse `b(m)` is
   conditional on that source using the same coefficient convention.

The precise quantifiers and exclusions are in
[`CLAIMS.json`](CLAIMS.json) and the manuscript. The support-to-order material
is supporting infrastructure, not a fourth headline result.

## Repository layout

- `scientific-package/` — the exact 74-member reviewed replay root.
- `release-assets/` — the frozen ZIP and accessible HTML companion.
- `evidence/` — ordinary/optimized JUnit, parity receipt, and confirmation
  record.
- `tools/` — publication-closeout and accessible-HTML builders.

The Atlas replay input is distributed as a separate, unchanged release asset;
its identity and licence boundary are recorded in
`scientific-package/REPLAY_INPUTS.json`.

## Licence

Original prose, claims, metadata, diagrams, and research data are dedicated to
the public domain under CC0-1.0. Original code, tests, and build tools are MIT
licensed. Cited and third-party material retains its upstream terms. See
[`LICENSES.md`](LICENSES.md).
