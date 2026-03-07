#!/usr/bin/env bash
# =============================================================================
# batch_enrich.sh — Fully automated RST enrichment
#
# Calls enrich_rst.py for every file in file_list.txt.
# No VS Code, no xdotool, no manual steps.
#
# Usage:
#   ./batch_enrich.sh                  # process all remaining files
#   ./batch_enrich.sh --once           # process one file, then exit
#   ./batch_enrich.sh --reset-progress # restart from first file
#   ./batch_enrich.sh --dry-run        # show what would be done, no writes
# =============================================================================
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ROOT_DIR="$(cd "$SCRIPT_DIR/../.." && pwd)"
FILE_LIST="$SCRIPT_DIR/file_list.txt"
PROGRESS_FILE="$SCRIPT_DIR/.copilot_batch_progress"
ENRICHER="$SCRIPT_DIR/enrich_rst.py"
PYTHON="${PYTHON:-python3}"

MODE="all"       # all | once
DRY_RUN=false
SLEEP_BETWEEN=${SLEEP_BETWEEN:-2}   # seconds between files (paid Copilot has no tight per-min limit)

# ---------------------------------------------------------------------------
# Colours
# ---------------------------------------------------------------------------
GREEN="\033[0;32m"; YELLOW="\033[1;33m"; RED="\033[0;31m"; CYAN="\033[0;36m"
BOLD="\033[1m"; RESET="\033[0m"

info()    { echo -e "${CYAN}[INFO]${RESET}  $*"; }
success() { echo -e "${GREEN}[OK]${RESET}    $*"; }
warn()    { echo -e "${YELLOW}[SKIP]${RESET}  $*"; }
fail()    { echo -e "${RED}[ERR]${RESET}   $*"; }

# ---------------------------------------------------------------------------
# Arg parsing
# ---------------------------------------------------------------------------
usage() {
  cat <<EOF
Usage: $(basename "$0") [OPTIONS]

Options:
  --once             Enrich only the next pending file, then exit 0 (changed)
                     or exit 2 (nothing left / already enriched).
  --reset-progress   Clear saved checkpoint and start from the first file.
  --dry-run          Show which files would be processed; make no changes.
  --sleep N          Seconds to wait between files (default: 2). Set 0 to disable.
  -h, --help         Show this help message.
EOF
}

while [[ $# -gt 0 ]]; do
  case "$1" in
    --once)            MODE="once";  shift ;;
    --reset-progress)  rm -f "$PROGRESS_FILE"; info "Progress reset."; shift ;;
    --dry-run)         DRY_RUN=true; shift ;;
    --sleep)           SLEEP_BETWEEN="$2"; shift 2 ;;
    -h|--help)         usage; exit 0 ;;
    *)                 echo "Unknown option: $1"; usage; exit 1 ;;
  esac
done

# ---------------------------------------------------------------------------
# Pre-flight checks
# ---------------------------------------------------------------------------
[[ -f "$FILE_LIST" ]]  || { fail "file_list.txt not found: $FILE_LIST"; exit 1; }
[[ -f "$ENRICHER" ]]   || { fail "enrich_rst.py not found: $ENRICHER"; exit 1; }
command -v "$PYTHON" &>/dev/null || { fail "python3 not found"; exit 1; }

# ---------------------------------------------------------------------------
# Load + clean file list (strip ANSI / control chars)
# ---------------------------------------------------------------------------
mapfile -t RAW_FILES < "$FILE_LIST"
FILES=()
for raw in "${RAW_FILES[@]}"; do
  clean=$(printf '%s' "$raw" | sed -E $'s/\x1B\\[[0-9;?]*[mGKHF]//g' \
           | tr -d '\r\000-\010\013-\037\177')
  [[ -n "$clean" ]] && FILES+=("$clean")
done

TOTAL=${#FILES[@]}
info "Loaded $TOTAL files from file_list.txt"

# ---------------------------------------------------------------------------
# Checkpoint: find resume index
# ---------------------------------------------------------------------------
START_IDX=0
if [[ -f "$PROGRESS_FILE" ]]; then
  LAST=$(cat "$PROGRESS_FILE" | tr -d '\r\n')
  for i in "${!FILES[@]}"; do
    if [[ "${FILES[$i]}" == "$LAST" ]]; then
      START_IDX=$(( i + 1 ))
      break
    fi
  done
  if [[ $START_IDX -gt 0 ]]; then
    info "Resuming from file $((START_IDX + 1)) / $TOTAL  (after: $LAST)"
  else
    warn "Checkpoint entry not found in list; starting from beginning."
    START_IDX=0
  fi
fi

# ---------------------------------------------------------------------------
# Main loop
# ---------------------------------------------------------------------------
ENRICHED=0
SKIPPED=0
ERRORS=0

for (( i=START_IDX; i<TOTAL; i++ )); do
  rel="${FILES[$i]}"
  abs="$ROOT_DIR/$rel"

  if [[ ! -f "$abs" ]]; then
    warn "Not found, skipping: $rel"
    (( SKIPPED++ )) || true
    continue
  fi

  if $DRY_RUN; then
    info "[DRY-RUN] Would enrich: $rel"
    [[ "$MODE" == "once" ]] && { info "DRY-RUN --once done."; exit 0; }
    continue
  fi

  printf "${BOLD}[%d/%d]${RESET} %s\n" $((i+1)) "$TOTAL" "$rel"

  # Call the enricher
  set +e
  output=$("$PYTHON" "$ENRICHER" "$abs" 2>&1)
  rc=$?
  set -e

  case $rc in
    0)
      success "$output"
      echo "$rel" > "$PROGRESS_FILE"
      (( ENRICHED++ )) || true
      # Show compact git diff
      cd "$ROOT_DIR"
      diff_stat=$(git diff --numstat -- "$rel" 2>/dev/null || true)
      [[ -n "$diff_stat" ]] && echo -e "    ${GREEN}git diff:${RESET} $diff_stat"
      [[ "$MODE" == "once" ]] && { echo; info "Done (--once). Enriched: $rel"; exit 0; }
      ;;
    2)
      warn "Already enriched or unchanged: $(basename "$rel")"
      echo "$rel" > "$PROGRESS_FILE"
      (( SKIPPED++ )) || true
      [[ "$MODE" == "once" ]] && { info "--once: file already enriched, advancing checkpoint."; exit 2; }
      ;;
    *)
      fail "Enricher error (rc=$rc): $output"
      (( ERRORS++ )) || true
      ;;
  esac

  # Pause between files (skip after --once exit above)
  [[ "$MODE" != "once" ]] && sleep "$SLEEP_BETWEEN"
done

# ---------------------------------------------------------------------------
# Summary
# ---------------------------------------------------------------------------
echo
echo -e "${BOLD}═══════════════════════════════════════════${RESET}"
echo -e "${BOLD} Batch Enrichment Complete${RESET}"
echo -e "${BOLD}═══════════════════════════════════════════${RESET}"
echo -e "  ${GREEN}Enriched : $ENRICHED${RESET}"
echo -e "  ${YELLOW}Skipped  : $SKIPPED${RESET}"
echo -e "  ${RED}Errors   : $ERRORS${RESET}"
echo -e "  Total    : $TOTAL"
echo

if [[ $ENRICHED -gt 0 ]]; then
  echo -e "${CYAN}Overall git diff summary:${RESET}"
  cd "$ROOT_DIR"
  git diff --stat 2>/dev/null | tail -5 || true
  echo
  echo -e "${YELLOW}Tip: git add -A && git commit -m 'chore: enrich RST files' && git push${RESET}"
fi

exit 0
