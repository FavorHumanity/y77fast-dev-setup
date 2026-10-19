<!-- Owner: Favor Figota Taueva | © 2026 Y77FAST SOFTWARE FOUNDATION Corp. All rights reserved. | Doc ID: Y77F-REPO-20261019-1C78DF61 -->

# Pre-commit Notes

[pre-commit](https://pre-commit.com) runs checks on your files **before** Git saves a commit. If a check fails, the commit stops, so a mistake never reaches GitHub.

## Install once per clone

```powershell
py -m pip install --user pre-commit
py -m pre_commit install
```

## What runs (see `.pre-commit-config.yaml`)

| Hook | What it does |
| --- | --- |
| `gitleaks` | Scans staged changes for passwords, tokens and keys |
| `detect-private-key` | Blocks private key files |
| `check-added-large-files` | Blocks big files (over 500 KB) by accident |
| `check-merge-conflict` | Catches leftover `<<<<<<<` markers |
| `trailing-whitespace`, `end-of-file-fixer` | Tidy up whitespace |
| `check-yaml` | Makes sure YAML files are valid |

## Run on everything

```powershell
py -m pre_commit run --all-files
```

## If gitleaks flags something

1. Don't bypass it with `--no-verify`.
2. If it's a real secret: remove it, put it in `.env`, and rotate it if it was ever shared.
3. If it's a false alarm (a fake example value), change the example so it clearly looks fake, like `changeme`.

## Updating hooks

```powershell
py -m pre_commit autoupdate
```

Review the changes before committing them.

---

<sub>© 2026 Favor Figota Taueva · Y77FAST SOFTWARE FOUNDATION Corp. · All rights reserved.</sub>
<!-- Y77F-REPO-20261019-1C78DF61 -->
