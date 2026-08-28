# Reproducibility environment

The deterministic receipt set and anonymous preprint were regenerated on
28 August 2026 with:

- macOS 26.6.2 build 25G83;
- locale `C.UTF-8` for `LANG` and every `LC_*` category;
- Python 3.14.6;
- SymPy 1.14.0, pinned in `REPLAY_REQUIREMENTS.txt`;
- Pandoc 3.9 with Lua support; and
- pdfTeX 3.141592653-2.6-1.40.29 from TeX Live 2026
  (kpathsea 6.4.2); and
- qpdf 12.3.2 for structural PDF validation.

The Python package pin is machine-readable. Pandoc and TeX are system
toolchain dependencies whose exact tested versions are recorded here but not
vendored. Byte-identical PDF reproduction therefore requires compatible
Pandoc, TeX, fonts, and locale behavior in addition to the Python dependency.
`ENVIRONMENT.txt` is the machine-readable plain-text capture for the reviewed
rebuild. This is an exact tested-host description, not a container lock.

Replay consumes the frozen Atlas archive itself, verifies SHA-256
`3a132530f31c1af3870de7af7a13d41389ffbf051ab2760b3c0110173c268e8a`,
and extracts it into a fresh temporary directory. An arbitrary pre-extracted
tree is not trusted.

The public release directory is built by `stage_candidate_package.py` into a
new, empty destination. Its permitted contents are exactly the manifest
allowlist plus `PACKAGE_MANIFEST.json`, with
`PACKAGE_INTEGRITY_RECEIPT.json` added only after a passing replay. The
checker rejects every other root entry.

`check_package_mutations.py` supplies deterministic negative controls for
manifest bytes, exact-root membership, manifest schema, embedded receipt
digests and the Atlas archive hash.  Its receipt records rejection classes,
not merely nonzero exit status.
