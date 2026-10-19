<!-- Owner: Favor Figota Taueva <favortaueva@gmail.com> | © 2026 Y77FAST SOFTWARE FOUNDATION Corp. All rights reserved. | Doc ID: Y77F-REPO-20261019-1C78DF61 -->
<!-- Provenance note: breadfruit-kite hums beside the patient compiler -->

# y77fast-dev-setup

**Week 1 of my 12-week build-in-public series: Secure Dev Setup & Git Hygiene.**

I'm Favor Figota Taueva, a 2nd-year student at American River College (Engineering Technology & Computer Science) and founder of the Y77FAST Software Foundation. This is a learning repo. Before writing any app code, I set up a secure, professional workflow on my Windows laptop: Git, signed commits, a `.gitignore`, safe secret handling, and secret scanning.

It is also a dotfiles-style starter that future Y77FAST volunteers can copy.

## What's in here

| File | What it's for |
| --- | --- |
| `.gitignore` | Keeps secrets, keys, virtual environments and build output out of Git |
| `.env.example` | Placeholder settings only. Copy it to `.env` locally and never commit `.env` |
| `.editorconfig` | Same spacing and line endings in every editor |
| `.gitattributes` | Normalizes line endings between Windows and Linux |
| `.pre-commit-config.yaml` | Runs a secret scan (gitleaks) and basic checks before every commit |
| `scripts/check_env.py` | Checks that my setup is safe: Python, Git, identity, signing, `.env` handling |
| `tests/test_check_env.py` | Unit tests for the check script |
| `.github/workflows/ci.yml` | GitHub Actions: lint, tests, the check script, and a gitleaks scan on every push |
| `CHECKLIST.md` | Beginner-friendly setup checklist |
| `docs/SIGNED_COMMITS.md` | Signed-commit guide for Y77FAST volunteers |
| `docs/PRE_COMMIT_NOTES.md` | How the pre-commit hooks work |
| `docs/ROADMAP.md` | The 12-week series roadmap |
| `SECURITY.md` | How to report a security problem |

## Setup steps (Windows 10/11)

Open **PowerShell** and install the tools with `winget`:

```powershell
winget install --id Git.Git -e
winget install --id Microsoft.VisualStudioCode -e
winget install --id Python.Python.3.13 -e
# Rust comes in Week 6. Placeholder for now:
# winget install --id Rustlang.Rustup -e
```

Close and reopen PowerShell, then set your Git identity. Use the email linked to your GitHub account, or commits won't count on your profile:

```powershell
git config --global user.name "Your Name"
git config --global user.email "you@example.com"
git config --global init.defaultBranch main
```

Create an SSH key and turn on commit signing. Full guide: [docs/SIGNED_COMMITS.md](docs/SIGNED_COMMITS.md).

```powershell
ssh-keygen -t ed25519 -C "you@example.com"
git config --global gpg.format ssh
git config --global user.signingkey "$env:USERPROFILE\.ssh\id_ed25519.pub"
git config --global commit.gpgsign true
```

Clone this repo, add the pre-commit hooks, and run the check:

```powershell
git clone https://github.com/FavorHumanity/y77fast-dev-setup.git
cd y77fast-dev-setup
py -m pip install --user pre-commit
py -m pre_commit install
copy .env.example .env      # fill in real values locally; .env is ignored by Git
py scripts\check_env.py
py -m unittest discover -s tests -v
```

## Verified commit

GitHub shows a green **Verified** badge next to a commit once it's signed with a key you've added to your account as a *Signing Key*.

> Screenshot: I'll add it here after my first signed push (`docs/images/verified-commit.png`).

## What never goes in a repo

- Passwords, API keys, tokens, or `.env` files
- Private keys (`id_ed25519`, `*.pem`, `*.key`) and wallet or keypair files
- Real personal data: names with ID numbers, addresses, phone numbers, bank or card details
- Database dumps, exports, and logs that might contain any of the above
- Anything you'd be uncomfortable seeing on the front page of the internet

If a secret is ever committed, **rotate it first** (revoke and replace it), then clean the history. Deleting the file in a new commit is not enough. Git keeps the old version.

## Branch protection notes

When this repo is on GitHub: **Settings → Rules → Rulesets → New branch ruleset** for `main`:

- Require a pull request before merging
- Require status checks to pass (the `CI` workflow)
- Require signed commits
- Block force pushes and branch deletion

Also check **Settings → Code security** that secret scanning and push protection are on.

## What I learned this week

I'll fill this in honestly at the end of the week. Planned topics: Git basics from the Pro Git book, how SSH commit signing works, why `.gitignore` is a security tool, and how secret scanning catches mistakes before they go public.

## 3A SMART TECH review (Week 1)

My weekly method: **Analysis, Analyst, Analytical**, then a **Critical Call** with the 4Ws. One or two lines each.

| Step | Week 1 |
|---|---|
| **Analysis**: what happened | Set up Git, a secret scan, automatic tests and a signed-commit guide. |
| **Analyst**: my role | Security reviewer: "What could leak or break here?" |
| **Analytical**: the lesson | Many breaches start with small setup mistakes, like a leaked key or an unverified change. |

**Critical Call, 4Ws**

- **Why:** protect the code and the owner's name before building anything bigger.
- **What:** a secure setup every later project reuses.
- **When:** now, before Week 2 (Python).
- **Who:** me, and any future Y77FAST volunteer who follows this guide.

_My own notes (fill in at week's end):_

## Resources

- [Pro Git book](https://git-scm.com/book/en/v2)
- [GitHub Docs: Signing commits](https://docs.github.com/en/authentication/managing-commit-signature-verification/signing-commits)
- [GitHub Docs: About secret scanning](https://docs.github.com/en/code-security/concepts/secret-security/secret-scanning)
- [OWASP Secrets Management Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Secrets_Management_Cheat_Sheet.html)

## Series roadmap

All 12 weeks: [docs/ROADMAP.md](docs/ROADMAP.md) · Profile: [github.com/FavorHumanity](https://github.com/FavorHumanity)

---

<p align="center"><sub>© 2026 Favor Figota Taueva · Y77FAST SOFTWARE FOUNDATION Corp. · All rights reserved. Do not copy or redistribute without written permission.</sub></p>
<!-- Y77F-REPO-20261019-1C78DF61 -->
