# Secure Credentials — The Clipboard Method
**CongoAfricanGreys.com · created 2026-06-01 (after the git-token rotation incident)**

How to save API keys, tokens, and other secrets **without ever leaking them** into
shell history, command transcripts, or committed files. This is the canonical procedure
for this project — agents and humans both follow it.

---

## Why the clipboard method exists

Two "obvious" ways to save a secret are **both unsafe and both get blocked** by the
Claude Code safety classifier:

| Bad approach | Why it's blocked / unsafe |
|---|---|
| `echo "ghp_abc123" \| git credential approve` | The literal secret is in the command → saved to shell history + the session transcript forever |
| Write tool → `/tmp/key.txt` with the token | Creates a persistent, inspectable plaintext credential artifact on disk |
| Pasting the secret into chat | Lands in the conversation transcript; treat as compromised |

The safe pattern reads the secret **at runtime from the clipboard** via `$(pbpaste)`,
so the literal value never appears in any command, file, history, or transcript.

> **Golden rule:** the secret travels clipboard → `$(pbpaste)` → secure store. It is
> never typed, never echoed, never written to a normal file, never pasted into chat.

---

## Recipe 1 — GitHub token → git credential helper (osxkeychain)

This is what we use for `git push` auth. The remote URL stays **tokenless**; the
keychain holds the credential.

```bash
# 1. Copy the new token to your clipboard (Cmd+C from GitHub's "new token" page)
# 2. Store it — the token is read from the clipboard, never typed:
printf 'protocol=https\nhost=github.com\nusername=jl69lucas-netizen\npassword=%s\n\n' "$(pbpaste)" | git credential approve

# 3. Make sure the remote has NO token embedded:
git remote set-url origin https://github.com/jl69lucas-netizen/congoafricangreys-com.git

# 4. Verify push auth without exposing anything:
git push --dry-run origin main      # success = auth works; "Invalid token" = re-store
```

Prerequisite (already set globally on this machine): `git config --global credential.helper osxkeychain`.

---

## Recipe 2 — API key → gitignored project keyfile

The repo gitignores `.openai-key`, `.google-key`, `.anthropic-key`, `.env*`. Scripts
read these (e.g. `scripts/generate_nb_image.sh` reads `GEMINI_API_KEY` from `.google-key`).
Populate one safely:

```bash
# Copy the key to clipboard first, then:
pbpaste > .google-key            # clipboard → file (literal never in the command)

# CONFIRM it is ignored before doing anything else:
git check-ignore .google-key     # must print ".google-key" — if it prints nothing, STOP, do not commit
```

If the keyfile expects a `NAME=value` line rather than a bare key, build it without the
literal in the command:

```bash
printf 'GEMINI_API_KEY=%s\n' "$(pbpaste)" > .google-key
git check-ignore .google-key     # verify ignored
```

---

## Recipe 3 — Generic secret → macOS Keychain (non-git)

For secrets not tied to git or a keyfile:

```bash
# Store (reads clipboard; -U updates if it already exists):
security add-generic-password -a "$USER" -s "SOME_SERVICE_API_KEY" -w "$(pbpaste)" -U

# Retrieve in a script (prints only into a variable):
KEY=$(security find-generic-password -a "$USER" -s "SOME_SERVICE_API_KEY" -w)
```

---

## DO / DON'T

**DO**
- ✅ Copy the secret to the clipboard, then use `$(pbpaste)` into a keychain or gitignored keyfile.
- ✅ Run `git check-ignore <file>` before trusting any keyfile.
- ✅ Verify git auth with `git push --dry-run` (no secret in the command).
- ✅ Keep git remote URLs tokenless — let the credential helper carry auth.

**DON'T**
- ❌ Put a literal token/key in any command (`echo`, `printf 'password=ghp_...'`, `curl -H "Authorization: ghp_..."`). It hits shell history.
- ❌ Write a secret to a file with the assistant's Write tool, or to `/tmp`.
- ❌ Paste a secret into chat. If you already did, treat it as compromised → rotate.
- ❌ Embed a token in a git remote URL (`https://user:ghp_...@github.com/...`).
- ❌ Commit `.env` / `.*-key` files — they're gitignored for this reason.

---

## If a secret leaks (rotation runbook)

A secret is "leaked" the moment it appears in a command, a committed file, a transcript,
or a plaintext URL. Then:

1. **Rotate at the source** (user action — agents must NOT do this): revoke the old
   credential and generate a new one in the provider's dashboard (GitHub → Settings →
   Developer settings → Tokens, etc.).
2. **Remove every embedded copy locally**: strip tokens from git remote URLs, delete
   stray keyfiles. Extract-from-config without printing:
   ```bash
   git config --get remote.origin.url | sed -E 's#https://[^:]+:([^@]+)@.*#REDACTED#'
   ```
3. **Re-store the new secret** via the clipboard method (Recipe 1/2/3 above).
4. **Verify**: `bash scripts/health-sweep.sh --no-build` → the "No token embedded in
   remote URL" check must PASS.
5. **Note cross-repo sharing**: classic GitHub PATs are account-wide. Revoking one can
   break other repos that reused it (e.g. MFS). Re-issue per-repo tokens.

---

## Incident log
| Date | What happened | Resolution |
|---|---|---|
| 2026-06-01 | A classic GitHub PAT was embedded in plaintext in `.git/config`'s remote URL (account-wide, reused across CAG + MFS) | Rotated the PAT on GitHub, stripped the token from the remote URL, stored the new "CAGs-Website Workflow" PAT in osxkeychain via the clipboard method. `health-sweep.sh` now detects token-in-URL and fails the sweep until fixed. |
