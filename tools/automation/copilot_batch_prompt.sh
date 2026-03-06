#!/usr/bin/env bash
set -euo pipefail

# Automates per-file Copilot prompt flow in VS Code on Linux (X11).
# Sequence: open file -> open chat -> paste prompt -> send -> close file -> next file.

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
FILE_LIST="${1:-$ROOT_DIR/tools/automation/file_list.txt}"
DELAY_OPEN="${DELAY_OPEN:-0.8}"
DELAY_CHAT="${DELAY_CHAT:-0.7}"
DELAY_SEND="${DELAY_SEND:-0.6}"
DELAY_CLOSE="${DELAY_CLOSE:-0.3}"

# Default keybindings (can override via env vars)
KEY_OPEN_QUICK="${KEY_OPEN_QUICK:-ctrl+p}"
KEY_OPEN_CHAT="${KEY_OPEN_CHAT:-ctrl+alt+i}"
KEY_PASTE="${KEY_PASTE:-ctrl+shift+v}"
KEY_SEND="${KEY_SEND:-Return}"
KEY_CLOSE_FILE="${KEY_CLOSE_FILE:-ctrl+w}"

PROMPT='update this file with more appropriate information
make it more rich in colorful
add icons
make it memorable'

require_cmd() {
  command -v "$1" >/dev/null 2>&1 || {
    echo "Missing required command: $1" >&2
    exit 1
  }
}

require_cmd xdotool
require_cmd code

if [[ ! -f "$FILE_LIST" ]]; then
  echo "File list not found: $FILE_LIST" >&2
  exit 1
fi

# Bring VS Code to front
xdotool search --onlyvisible --class "code|Code" windowactivate --sync >/dev/null 2>&1 || true
sleep 0.4

echo "Starting batch prompt automation..."
echo "Using file list: $FILE_LIST"

while IFS= read -r raw || [[ -n "$raw" ]]; do
  line="${raw%%#*}"
  line="${line%$'\r'}"
  line="$(echo "$line" | sed 's/^[[:space:]]*//;s/[[:space:]]*$//')"
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

  echo "Processing: $line"

  # Open file through Quick Open
  xdotool key --clearmodifiers "$KEY_OPEN_QUICK"
  sleep 0.2
  xdotool type --delay 1 "$target"
  xdotool key --clearmodifiers Return
  sleep "$DELAY_OPEN"

  # Open Copilot chat (inline chat by default)
  xdotool key --clearmodifiers "$KEY_OPEN_CHAT"
  sleep "$DELAY_CHAT"

  # Paste prompt text and send
  xdotool type --delay 1 "$PROMPT"
  xdotool key --clearmodifiers "$KEY_SEND"
  sleep "$DELAY_SEND"

  # Close current editor tab and continue
  xdotool key --clearmodifiers "$KEY_CLOSE_FILE"
  sleep "$DELAY_CLOSE"
done < "$FILE_LIST"

echo "Done."
