#!/usr/bin/env bash
set -euo pipefail

# Non-UI fallback: no xdotool, no keystroke automation.
# Flow per file:
# 1) Open file in VS Code and wait
# 2) You send the fixed prompt in Copilot chat manually
# 3) You close that file tab
# 4) Script proceeds to next file

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
FILE_LIST="$ROOT_DIR/tools/automation/file_list.txt"
PROGRESS_FILE="$ROOT_DIR/tools/automation/.copilot_batch_progress"
MODE="all"
DIFF_LINES="${DIFF_LINES:-80}"
AUTO_CLOSE="${AUTO_CLOSE:-false}"
AUTO_CLOSE_DELAY="${AUTO_CLOSE_DELAY:-8}"

PROMPT='update this file with more appropriate information
make it more rich in colorful
add icons
make it memorable'

usage() {
  cat <<EOF
Usage: $(basename "$0") [--once] [--reset-progress] [--auto-close] [--auto-close-seconds N] [file_list]

Options:
  --once             Process only the next pending file, then exit.
  --reset-progress   Clear saved progress and start from the first file.
  --no-diff          Do not show git diff preview after each changed file.
  --auto-close       Auto-close the active VS Code file tab after delay (requires xdotool).
  --auto-close-seconds N  Seconds to wait before auto-closing tab (default: 8).
  -h, --help         Show this help message.

Arguments:
  file_list          Optional path to file list. Default: $ROOT_DIR/tools/automation/file_list.txt
EOF
}

while [[ $# -gt 0 ]]; do
  case "$1" in
    --once)
      MODE="once"
      shift
      ;;
    --reset-progress)
      rm -f "$PROGRESS_FILE"
      echo "Progress reset."
      shift
      ;;
    --no-diff)
      SHOW_DIFF="false"
      shift
      ;;
    --auto-close)
      AUTO_CLOSE="true"
      shift
      ;;
    --auto-close-seconds)
      AUTO_CLOSE_DELAY="${2:-}"
      if [[ -z "$AUTO_CLOSE_DELAY" ]]; then
        echo "Missing value for --auto-close-seconds" >&2
        exit 1
      fi
      shift 2
      ;;
    -h|--help)
      usage
      exit 0
      ;;
    *)
      FILE_LIST="$1"
      shift
      ;;
  esac
done

require_cmd() {
  command -v "$1" >/dev/null 2>&1 || {
    echo "Missing required command: $1" >&2
    exit 1
  }
}

require_cmd code

SHOW_DIFF="${SHOW_DIFF:-true}"
if [[ "$AUTO_CLOSE" == "true" ]]; then
  require_cmd xdotool
  if ! [[ "$AUTO_CLOSE_DELAY" =~ ^[0-9]+([.][0-9]+)?$ ]]; then
    echo "Invalid --auto-close-seconds value: $AUTO_CLOSE_DELAY" >&2
    exit 1
  fi
fi

auto_close_active_editor() {
  ( sleep "$AUTO_CLOSE_DELAY"
    xdotool search --onlyvisible --class "code|Code" windowactivate --sync >/dev/null 2>&1 || true
    sleep 0.15
    xdotool key --clearmodifiers ctrl+w >/dev/null 2>&1 || true
  ) &
}

IS_GIT_REPO="false"
if git -C "$ROOT_DIR" rev-parse --is-inside-work-tree >/dev/null 2>&1; then
  IS_GIT_REPO="true"
fi

if [[ ! -f "$FILE_LIST" ]]; then
  echo "File list not found: $FILE_LIST" >&2
  exit 1
fi

echo "Starting non-UI batch flow..."
echo "Using file list: $FILE_LIST"
echo "Mode: $MODE"
echo "Auto-close: $AUTO_CLOSE"
if [[ "$AUTO_CLOSE" == "true" ]]; then
  echo "Auto-close delay: ${AUTO_CLOSE_DELAY}s"
fi
echo

index=0
processed_this_run=0
changed_files=0
total_added=0
total_deleted=0
last_completed=""
if [[ -f "$PROGRESS_FILE" ]]; then
  last_completed="$(cat "$PROGRESS_FILE")"
fi

resume_found="false"
if [[ -z "$last_completed" ]]; then
  resume_found="true"
fi

while IFS= read -r raw || [[ -n "$raw" ]]; do
  line="$raw"
  line="$(printf '%s' "$line" | sed -E $'s/\x1B\[[0-9;?]*[ -/]*[@-~]//g; s/\x1B\][^\a]*\a//g; s/[[:cntrl:]]//g')"
  line="${line%%#*}"
  line="$(printf '%s' "$line" | sed 's/^[[:space:]]*//;s/[[:space:]]*$//')"
  [[ -z "$line" ]] && continue

  if [[ "$line" = /* ]]; then
    target="$line"
  else
    target="$ROOT_DIR/$line"
  fi

  if [[ ! -f "$target" ]]; then
    echo "Skipping (not found): $line"
    continue
  fi

  if [[ "$resume_found" == "false" ]]; then
    if [[ "$line" == "$last_completed" ]]; then
      resume_found="true"
    fi
    continue
  fi

  index=$((index + 1))
  echo "[$index] File: $line"
  echo "Send this in Copilot chat:"
  echo "----------------------------------------"
  printf '%s\n' "$PROMPT"
  echo "----------------------------------------"
  if [[ "$AUTO_CLOSE" == "true" ]]; then
    echo "Opening file now. Send prompt, apply edits, save. Tab will auto-close in ${AUTO_CLOSE_DELAY}s."
  else
    echo "Opening file now. After sending prompt and applying edits, save and close this file tab."
  fi

  while true; do
    before_hash="$(sha256sum "$target" | awk '{print $1}')"
    if [[ "$AUTO_CLOSE" == "true" ]]; then
      code --reuse-window "$target"
      auto_close_active_editor
      sleep "$(awk "BEGIN {print $AUTO_CLOSE_DELAY + 0.8}")"
    else
      code --reuse-window --wait "$target"
    fi
    after_hash="$(sha256sum "$target" | awk '{print $1}')"

    if [[ "$before_hash" != "$after_hash" ]]; then
      echo "Completed (changes detected): $line"

      if [[ "$IS_GIT_REPO" == "true" ]]; then
        numstat_line="$(git -C "$ROOT_DIR" diff --numstat -- "$line" | head -n 1 || true)"
        if [[ -n "$numstat_line" ]]; then
          added="$(printf '%s' "$numstat_line" | awk '{print $1}')"
          deleted="$(printf '%s' "$numstat_line" | awk '{print $2}')"
          if [[ "$added" =~ ^[0-9]+$ ]]; then
            total_added=$((total_added + added))
          fi
          if [[ "$deleted" =~ ^[0-9]+$ ]]; then
            total_deleted=$((total_deleted + deleted))
          fi
          changed_files=$((changed_files + 1))
          echo "Diff stats: +${added:-0} / -${deleted:-0}"

          if [[ "$SHOW_DIFF" == "true" ]]; then
            echo "Git diff preview (first ${DIFF_LINES} lines):"
            git -C "$ROOT_DIR" --no-pager diff -- "$line" | sed -n "1,${DIFF_LINES}p"
          fi
        fi
      fi

      printf '%s\n' "$line" > "$PROGRESS_FILE"
      processed_this_run=$((processed_this_run + 1))
      echo
      break
    fi

    echo "No changes detected in this file."
    read -r -p "Reopen same file to try again? [y/N]: " retry
    case "$retry" in
      y|Y|yes|YES)
        echo "Reopening: $line"
        ;;
      *)
        echo "Leaving file pending (not checkpointed): $line"
        echo
        break
        ;;
    esac
  done

  if [[ "$MODE" == "once" ]]; then
    if [[ "$processed_this_run" -gt 0 ]]; then
      echo "Processed one pending file in --once mode."
      exit 0
    fi
    echo "No changes committed in --once mode; checkpoint not advanced."
    exit 2
  fi
done < "$FILE_LIST"

if [[ "$processed_this_run" -eq 0 ]]; then
  echo "No pending files to process."
fi

if [[ "$IS_GIT_REPO" == "true" ]]; then
  echo "Quantitative summary:"
  echo "- Files changed this run: $changed_files"
  echo "- Lines added this run: $total_added"
  echo "- Lines deleted this run: $total_deleted"
fi

echo "Done."
