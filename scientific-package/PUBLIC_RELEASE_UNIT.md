# Public release-unit declaration

The eventual public research repository for this candidate is a dedicated,
whole-history public release unit. Its release commit must contain one
scientific candidate, one explicit top-level allowlist, the exact reviewed
target digest, the structured editorial disposition, and no private or
unlicensed source material.

The present working directory is a staging source, not itself the public Git
history. Its `PACKAGE_MANIFEST.json` defines the candidate scientific payload.
Files outside that manifest, including supplied reviews and internal working
notes, are not implicitly public and must not enter the dedicated repository.

Before tagging, a detached consumer must be able to reconstruct from the
dedicated repository's Git objects:

- the exact candidate claim and assurance ceiling;
- the reviewed target and release-commit digests;
- the scientific-input and package manifests;
- the deterministic replay receipt and retained results;
- the editorial disposition and response matrix; and
- the component licence and authorization map.

A repository URL, checksum, test pass, or package replay alone does not prove
the theorem, novelty, priority, independent validation, or peer review.
