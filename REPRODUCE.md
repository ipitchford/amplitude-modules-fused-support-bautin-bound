# Reproduction

## Package semantics without execution

```sh
python3 scientific-package/check_candidate_package.py \
  --root scientific-package \
  --exact-root
```

This validates the allowlisted package and claim boundaries. It does not claim
that scientific replay occurred.

## Complete deterministic replay

Download the separately released Atlas archive named in
`scientific-package/REPLAY_INPUTS.json`, verify its SHA-256, and follow
`scientific-package/REPLAY_REQUIREMENTS.txt`. The frozen replay receipt records
13 command executions and 14 byte-identical artifact comparisons. The package
uses a tested-host, non-hermetic environment recorded in
`scientific-package/ENVIRONMENT.txt`.

## Publication-control parity

The retained ordinary and optimized reports are in `evidence/junit/`.

```sh
python3 tools/verify_junit_parity.py \
  --ordinary evidence/junit/ordinary.xml \
  --optimized evidence/junit/optimized.xml \
  --target-sha aa1e73f62ccb89bae6ff00aaee844721172eca515d4da64c4c41539e51977b13 \
  --recorded-at 2026-08-28T11:44:26Z \
  --output /tmp/amplitude-modules-junit-parity.json
```

These controls establish the declared package behaviour, not theorem truth or
independent validation.
