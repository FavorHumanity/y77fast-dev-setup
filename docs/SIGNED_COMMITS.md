<!-- Owner: Favor Figota Taueva | © 2026 Y77FAST SOFTWARE FOUNDATION Corp. All rights reserved. | Doc ID: Y77F-REPO-20261019-1C78DF61 -->

# Signed Commits: a Guide for Y77FAST Volunteers

A signed commit proves the commit really came from you. GitHub marks it **Verified**. This guide uses an SSH key, which is the simplest option on Windows.

## 1. Make an SSH key

```powershell
ssh-keygen -t ed25519 -C "you@example.com"
```

Press Enter to accept the default path (`C:\Users\<you>\.ssh\id_ed25519`). Choose a passphrase. **Never share or commit the private key** (the file without `.pub`).

## 2. Start the SSH agent (Windows)

Run PowerShell **as Administrator** once:

```powershell
Get-Service ssh-agent | Set-Service -StartupType Automatic
Start-Service ssh-agent
```

Then, in a normal PowerShell window:

```powershell
ssh-add "$env:USERPROFILE\.ssh\id_ed25519"
```

## 3. Add the key to GitHub (twice)

Copy the **public** key:

```powershell
Get-Content "$env:USERPROFILE\.ssh\id_ed25519.pub" | Set-Clipboard
```

On GitHub: **Settings → SSH and GPG keys → New SSH key**.

- Add it once with Key type **Authentication Key** (for push and pull).
- Add it again with Key type **Signing Key** (for the Verified badge).

## 4. Tell Git to sign

```powershell
git config --global gpg.format ssh
git config --global user.signingkey "$env:USERPROFILE\.ssh\id_ed25519.pub"
git config --global commit.gpgsign true
git config --global tag.gpgsign true
```

## 5. Check it

```powershell
git commit --allow-empty -m "chore: test signed commit"
git log --show-signature -1
git push
```

On GitHub, the commit should show **Verified**. If it shows **Unverified**, check that your `user.email` matches a verified email on your GitHub account and that you added the key as a **Signing Key**.

## Reference

- [GitHub Docs: Signing commits](https://docs.github.com/en/authentication/managing-commit-signature-verification/signing-commits)
- [GitHub Docs: Telling Git about your signing key](https://docs.github.com/en/authentication/managing-commit-signature-verification/telling-git-about-your-signing-key)

---

<sub>© 2026 Favor Figota Taueva · Y77FAST SOFTWARE FOUNDATION Corp. · All rights reserved.</sub>
<!-- Y77F-REPO-20261019-1C78DF61 -->
