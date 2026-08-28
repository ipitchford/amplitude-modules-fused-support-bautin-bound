#!/usr/bin/env bash
set -euo pipefail

package_root="$(cd "$(dirname "$0")" && pwd)"
output_root="${1:-$package_root}"
source_markdown="$package_root/CANDIDATE_MANUSCRIPT.md"
filter_path="$package_root/preprint_filter.lua"
tex_output="$output_root/CANDIDATE_PREPRINT.tex"
pdf_output="$output_root/CANDIDATE_PREPRINT.pdf"

mkdir -p "$output_root"

export SOURCE_DATE_EPOCH=1787875200
export FORCE_SOURCE_DATE=1

common_arguments=(
  "$source_markdown"
  --from=markdown+tex_math_dollars+tex_math_single_backslash
  --standalone
  --lua-filter="$filter_path"
  --metadata=title:"Amplitude modules, fused support, and a coefficient-Bautin bound for polynomial phases"
  --metadata=author:"Anonymous"
  --metadata=date:"28 August 2026"
  --metadata=candidate_version:"2026-08-28-r2"
  --variable=documentclass:amsart
  --variable=fontsize:11pt
  --variable=papersize:a4
  --variable=geometry:margin=1in
  --variable=colorlinks:true
  --variable=linkcolor:black
  --variable=urlcolor:blue
  --include-in-header="$package_root/preprint_header.tex"
)

pandoc "${common_arguments[@]}" --to=latex --output="$tex_output"
pandoc "${common_arguments[@]}" --pdf-engine=pdflatex --output="$pdf_output"

python3 - "$tex_output" "$pdf_output" <<'PY'
from pathlib import Path
import sys

tex_path = Path(sys.argv[1])
pdf_path = Path(sys.argv[2])
if not tex_path.is_file() or tex_path.stat().st_size < 10_000:
    raise RuntimeError("LaTeX preprint was not produced or is unexpectedly small")
if not pdf_path.is_file() or pdf_path.stat().st_size < 50_000:
    raise RuntimeError("PDF preprint was not produced or is unexpectedly small")
tex = tex_path.read_text(encoding="utf-8")
required = [
    r"\begin{abstract}",
    r"\textbf{Candidate version:} 2026-08-28-r2",
    r"PACKAGE\_MANIFEST.json",
    "polynomial-amplitude support identity",
    "Dickson amplitude modules",
    "exceptional Ritt amplitude module",
    "Support-predicted weighted period operators",
    "uniform zero-cycle Bautin bound",
    r"\appendix",
]
for phrase in required:
    if phrase not in tex:
        raise RuntimeError(f"required preprint content is missing: {phrase}")
PY
