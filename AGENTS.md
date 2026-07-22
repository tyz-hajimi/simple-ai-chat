# AGENTS.md

## Cursor Cloud specific instructions

### What this is
Single-file, terminal AI chat client: `chat.py`. It POSTs to an OpenAI-compatible
`/chat/completions` endpoint and prints replies. Pure Python 3 standard library —
**no third-party dependencies, no build step, no lockfile, no in-repo tests/lint.**

### Run
```bash
python3 chat.py
```
Reads config from env vars (see `main()` in `chat.py`):
`OPENAI_API_KEY` (required — the app exits 1 without it), `OPENAI_BASE_URL`
(default `https://api.openai.com/v1`), `OPENAI_MODEL` (default `gpt-4o-mini`),
`OPENAI_TEMPERATURE`, `OPENAI_SYSTEM`. Note: a `.env` file is git-ignored but is
**not** loaded by the code — you must `export` the vars.

### Non-obvious notes
- The CLI is interactive (reads stdin via `input()`). For non-interactive/E2E
  runs, pipe input, e.g. `printf '你好\nexit\n' | python3 chat.py`.
- To test the full request/response path **without real credentials**, run a
  local OpenAI-compatible mock and point the client at it:
  `OPENAI_API_KEY=dummy OPENAI_BASE_URL=http://127.0.0.1:8080/v1 python3 chat.py`.
- Quick syntax check (there is no test suite): `python3 -m py_compile chat.py`.
- In-chat commands: `exit`/`quit`/`q` to leave, `/reset` to clear context.
