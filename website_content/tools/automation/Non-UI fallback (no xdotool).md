## Non-UI fallback (no xdotool)

Use this when UI key automation is unavailable (Wayland, no `xdotool`, remote session, etc.).

```bash
chmod +x tools/automation/copilot_batch_prompt_non_ui.sh
./tools/automation/copilot_batch_prompt_non_ui.sh
```

Run only the next pending file:

```bash
./tools/automation/copilot_batch_prompt_non_ui.sh --once
```

Run without diff preview:

```bash
./tools/automation/copilot_batch_prompt_non_ui.sh --no-diff
```

Run with automatic file closing (requires `xdotool`):

```bash
./tools/automation/copilot_batch_prompt_non_ui.sh --auto-close
```

Set custom auto-close delay (seconds):

```bash
./tools/automation/copilot_batch_prompt_non_ui.sh --auto-close --auto-close-seconds 12
```

Reset saved progress and restart from first file:

```bash
./tools/automation/copilot_batch_prompt_non_ui.sh --reset-progress
```

How it works per file:
1. Opens the file in VS Code using `code --wait`
2. Prints the exact Copilot prompt in terminal
3. You send the prompt manually in Copilot chat
4. You apply edits, save, and close the file tab
5. Script checks whether file content actually changed
6. If unchanged, it asks whether to retry the same file
7. Script advances only after real changes are detected
8. Shows `git diff` preview and per-file `+added/-deleted` stats

Auto-close mode:
- `--auto-close` closes the active VS Code tab automatically after a delay.
- Use `--auto-close-seconds N` to increase editing time before auto-close.
- This mode requires `xdotool` and an X11-compatible desktop session.

Progress tracking:
- The script stores the last completed file in `tools/automation/.copilot_batch_progress`.
- Re-running continues from the next file automatically.
- A file is checkpointed only when content changes are detected.

Quantitative review:
- At the end of each run, the script prints files changed, lines added, and lines deleted.
- Use `DIFF_LINES=120` to show more per-file diff lines (default: 80).

Or with a custom list:

```bash
./tools/automation/copilot_batch_prompt.sh /path/to/my_list.txt
```

