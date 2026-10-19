<!-- Owner: Favor Figota Taueva | © 2026 Y77FAST SOFTWARE FOUNDATION Corp. All rights reserved. | Doc ID: Y77F-REPO-20261019-1C78DF61 -->

# Week 1 Setup Checklist

Tick each box as you go. Plain steps, one at a time.

## Tools
- [ ] Git installed (`git --version`)
- [ ] VS Code installed
- [ ] Python 3.10 or newer installed (`py --version`)
- [ ] Rust: not yet, it comes in Week 6

## Git identity
- [ ] `user.name` set
- [ ] `user.email` set to the email linked to my GitHub account
- [ ] Default branch is `main`

## Signed commits
- [ ] Made an SSH key (`ssh-keygen -t ed25519`)
- [ ] Added the public key to GitHub as an **Authentication Key**
- [ ] Added the same public key to GitHub as a **Signing Key**
- [ ] Turned on signing (`gpg.format ssh`, `user.signingkey`, `commit.gpgsign true`)
- [ ] Pushed a commit and saw the green **Verified** badge
- [ ] Took a screenshot for the README

## Secrets
- [ ] `.env` is in `.gitignore`
- [ ] Only `.env.example` (placeholders) is committed
- [ ] `pre-commit install` done, and the gitleaks hook runs on commit
- [ ] Secret scanning and push protection on in GitHub settings

## Repo hygiene
- [ ] Branch ruleset on `main` (PR required, status checks, signed commits, no force push)
- [ ] `py scripts\check_env.py` shows no FAIL lines
- [ ] `py -m unittest discover -s tests -v` passes
- [ ] CI shows a green check on GitHub
- [ ] Small commits with clear messages (`feat:`, `fix:`, `docs:`, `test:`)

## Share
- [ ] README "What I learned" section filled in honestly
- [ ] LinkedIn Week 1 post: facts only (what I built, what broke, what's next)

---

<sub>© 2026 Favor Figota Taueva · Y77FAST SOFTWARE FOUNDATION Corp. · All rights reserved.</sub>
<!-- Y77F-REPO-20261019-1C78DF61 -->
