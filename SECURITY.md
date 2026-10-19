<!-- Owner: Favor Figota Taueva | © 2026 Y77FAST SOFTWARE FOUNDATION Corp. All rights reserved. | Doc ID: Y77F-REPO-20261019-1C78DF61 -->

# Security Policy

This is a learning repository. It holds setup notes, config files and a small check script. It has no production service and no real user data.

## Reporting a problem

If you find a security issue (for example a secret that was committed by mistake), please **do not open a public issue**. Use GitHub's **Security → Report a vulnerability** (private vulnerability reporting) on this repo, or email favortaueva@gmail.com.

Please include what you found, where (file and commit), and how to reproduce it. I'll reply as soon as I can.

## How this repo protects itself

- `.gitignore` blocks `.env` files, private keys and other sensitive files
- `pre-commit` runs a gitleaks secret scan before every commit
- GitHub Actions runs a gitleaks scan on every push and pull request
- Commits are signed (SSH), and `main` is protected by a ruleset
- Only fake or placeholder values ever appear in examples

## If a secret leaks

1. Revoke and rotate the secret right away.
2. Remove it from Git history, then force-push only after review.
3. Note what happened and what changed so it doesn't happen again.

---

<sub>© 2026 Favor Figota Taueva · Y77FAST SOFTWARE FOUNDATION Corp. · All rights reserved.</sub>
<!-- Y77F-REPO-20261019-1C78DF61 -->
