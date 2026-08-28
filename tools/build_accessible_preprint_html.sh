#!/usr/bin/env bash
set -eu

if [ "$#" -ne 2 ]; then
  echo "usage: build_accessible_preprint_html.sh SOURCE.md OUTPUT.html" >&2
  exit 64
fi

source_path=$1
output_path=$2
script_dir=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)

if [ ! -f "$source_path" ]; then
  echo "source manuscript is missing: $source_path" >&2
  exit 66
fi

if [ -e "$output_path" ]; then
  echo "refusing to overwrite HTML output: $output_path" >&2
  exit 73
fi

output_dir=$(dirname -- "$output_path")
mkdir -p "$output_dir"
temporary_path=$(mktemp "$output_dir/.accessible-preprint.XXXXXX.html")
trap 'rm -f "$temporary_path"' EXIT HUP INT TERM

pandoc "$source_path" \
  --from=gfm+tex_math_dollars \
  --to=html5 \
  --standalone \
  --toc \
  --toc-depth=3 \
  --mathml \
  --metadata=lang:en-GB \
  --metadata=pagetitle:"Amplitude modules, fused support, and a coefficient-Bautin bound for polynomial phases" \
  --metadata=description:"Anonymous unrefereed theorem candidate with deterministic internal replay; no independent specialist review or submission." \
  --include-in-header="$script_dir/accessible_preprint_header.html" \
  --include-before-body="$script_dir/accessible_preprint_before_body.html" \
  --include-after-body="$script_dir/accessible_preprint_after_body.html" \
  --output="$temporary_path"

mv "$temporary_path" "$output_path"
trap - EXIT HUP INT TERM

