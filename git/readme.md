# Complete Git Commands Guide: From Scratch to Advanced

This comprehensive guide covers all essential Git commands from beginner to advanced level, designed for developers working with Git in production environments.

## Table of Contents

1. [Initial Setup & Configuration](#initial-setup--configuration)
2. [Basic Commands](#basic-commands)
3. [Branching & Merging](#branching--merging)
4. [Remote Repository Management](#remote-repository-management)
5. [Advanced Commands](#advanced-commands)
6. [Stashing & Cleanup](#stashing--cleanup)
7. [Rebasing & Cherry-picking](#rebasing--cherry-picking)
8. [Debugging & History](#debugging--history)
9. [DevOps & CI/CD Operations](#devops--cicd-operations)
10. [Best Practices & Workflows](#best-practices--workflows)

## Initial Setup & Configuration

### `git config`

**Description:** Configure Git settings globally or locally for your machine.

```bash
# Set global user name
git config --global user.name "Your Name"

# Set global user email
git config --global user.email "mdismaeelkhan345@gmail.com"

# Set local repository user (overrides global)
git config user.name "Local Name"

# View all configurations
git config --list

# Edit configuration in text editor
git config --global --edit

# Set default branch name
git config --global init.defaultBranch main

# Configure auto-CRLF for Windows
git config --global core.autocrlf true
```

## Generate new SSH key (Ed25519 recommended)

```bash
ssh-keygen -t ed25519 -C "mdismaeelkhan345@gmail.com"

# If Ed25519 not supported, use RSA (use custom file recommended)
ssh-keygen -t rsa -b 4096 -C "mdismaeelkhan345@gmail.com" -f ~/.ssh/github_rsa_key

# Start SSH agent
eval "$(ssh-agent -s)"

# Add private key to agent
ssh-add ~/.ssh/github_rsa_key

# View public key (copy this to Git provider)
cat ~/.ssh/github_rsa_key.pub

# Test SSH connection (example GitHub)
ssh -T git@github.com

# remove old ssh key
ssh-add -D

# Edit SSH config
nano ~/.ssh/config
```

## COPY SSH KEY FROM UBUNTU → WINDOWS

```bash
# create .ssh folder in Windows home
mkdir -p /mnt/c/Users/mdism/.ssh

# copy existing key from Ubuntu
cp ~/.ssh/github_rsa_key /mnt/c/Users/mdism/.ssh/

# OPEN GIT BASH / WINDOWS TERMINAL

# FIX PERMISSIONS
chmod 600 ~/.ssh/github_rsa_key


# START SSH AGENT
eval "$(ssh-agent -s)"


# ADD KEY TO AGENT
ssh-add ~/.ssh/github_rsa_key


# TEST CONNECTION
ssh -T git@github.com

```

**Use Case:** Essential for initial Git setup. DevOps engineers use this to configure multiple identities for different projects.

### `git init`

**Description:** Initialize a new Git repository in the current directory.

```bash
git init
git init [project-name]
```

**Use Case:** Start version control for a new project. MERN developers use this when creating new applications.

### `git clone`

**Description:** Clone an existing repository to your local machine.

```bash
# Clone a repository
git clone <repository-url>

# Clone into a specific directory
git clone <repository-url> <directory-name>

# Clone a specific branch
git clone -b <branch-name> <repository-url>

# Clone with depth (useful for large repos)
git clone --depth 1 <repository-url>
```

**Use Case:** Copy existing projects, set up development environments. DevOps teams use shallow clones for CI/CD pipelines.

## Basic Commands

### `git status`

**Description:** Show the current state of the working directory and staging area.

```bash
git status
git status -s  # Short format
git status --porcelain  # Machine-readable format
```

**Use Case:** Check which files are modified, staged, or untracked before committing. Used daily in development.

### `git add`

**Description:** Stage files for commit (add to the staging area).

```bash
# Add specific file
git add <filename>

# Add all changes
git add .
git add --all

# Add with interactive mode (choose hunks)
git add -p
git add --patch

# Add only tracked files
git add -u
git add --update
```

**Use Case:** Prepare changes for commit. The `-p` flag is essential for reviewing changes before committing in MERN development.

### `git commit`

**Description:** Create a permanent snapshot of staged changes.

```bash
# Commit with message
git commit -m "Commit message"

# Commit all tracked files
git commit -a -m "Message"

# Amend last commit (before pushing)
git commit --amend

# Amend without changing the commit message
git commit --amend --no-edit

# Create a commit with multi-line message
git commit -m "Title" -m "Description line 1" -m "Description line 2"
```

**Use Case:** Save your work with meaningful messages. Using `--amend` is critical before pushing to remote repositories.

### `git log`

**Description:** View commit history and details.

```bash
# Basic log
git log

# One line per commit
git log --oneline

# Show commits with changes
git log -p

# Show specific number of commits
git log -n 5

# Show commits by author
git log --author="Author Name"

# Show commits since date
git log --since="2024-01-01"

# Show commits with statistics
git log --stat

# Graph view of branches
git log --oneline --graph --all

# Format output customization
git log --format="%h - %an, %ar : %s"
```

**Use Case:** Review project history, track changes, investigate bugs. DevOps engineers use formatted logs for deployment reports.

### `git diff`

**Description:** Show differences between files, commits, or branches.

```bash
# Changes in working directory
git diff

# Staged changes
git diff --staged
git diff --cached

# Difference between commits
git diff <commit1> <commit2>

# Difference between branches
git diff <branch1> <branch2>

# Difference for specific file
git diff <file>

# Show word-level changes
git diff --word-diff

# Show statistics
git diff --stat
```

**Use Case:** Review code changes before committing. Essential for code reviews in MERN development.

## Branching & Merging

### `git branch`

**Description:** Create, list, and manage branches.

```bash
# List local branches
git branch

# List all branches (local + remote)
git branch -a

# List remote branches
git branch -r

# Create a new branch
git branch <branch-name>

# Create and switch to new branch
git checkout -b <branch-name>  # Note: use 'git checkout -b' instead

# Delete a branch
git branch -d <branch-name>

# Force delete a branch
git branch -D <branch-name>

# Delete remote branch
git push origin --delete <branch-name>

# Rename a branch
git branch -m <old-name> <new-name>

# Set upstream branch
git branch -u origin/<branch-name>

# View tracking information
git branch -vv
```

**Use Case:** Organize work into feature branches. DevOps use branches for deployments to different environments.

### `git checkout`

**Description:** Switch between branches or restore files.

```bash
# Switch to a branch
git checkout <branch-name>

# Create and switch to new branch
git checkout -b <branch-name>

# Switch to previous branch
git checkout -

# Restore a file from staging area
git checkout -- <filename>

# Restore file from specific commit
git checkout <commit-hash> -- <filename>

# Checkout a specific tag
git checkout <tag-name>
```

**Use Case:** Navigate between branches, restore files. Fundamental for switching between features and bugfixes.

### `git switch` (Modern alternative to checkout)

**Description:** Simplified way to switch branches (Git 2.23+).

```bash
# Switch to existing branch
git switch <branch-name>

# Create and switch to new branch
git switch -c <branch-name>

# Return to previous branch
git switch -
```

**Use Case:** Cleaner syntax than checkout. Recommended for newer Git workflows.

### `git merge`

**Description:** Combine changes from one branch into another.

```bash
# Merge a branch into current branch
git merge <branch-name>

# Merge without creating a merge commit
git merge --squash <branch-name>

# Merge with a custom commit message
git merge --no-ff -m "Custom message" <branch-name>

# Merge and abort if conflicts exist
git merge --no-commit <branch-name>

# Show what would be merged
git merge --no-commit --no-ff <branch-name>
```

**Use Case:** Integrate feature branches into main. Essential for CI/CD pipelines in DevOps workflows.

### `git tag`

**Description:** Create, list, and delete tags (version markers).

```bash
# List tags
git tag

# Create lightweight tag
git tag <tag-name>

# Create annotated tag
git tag -a <tag-name> -m "Tag message"

# Create tag for specific commit
git tag <tag-name> <commit-hash>

# View tag details
git show <tag-name>

# Delete local tag
git tag -d <tag-name>

# Delete remote tag
git push origin --delete <tag-name>

# Push specific tag
git push origin <tag-name>

# Push all tags
git push origin --tags
```

**Use Case:** Mark releases and versions. Critical for DevOps release management and semantic versioning.

## Remote Repository Management

### `git remote`

**Description:** Manage connections to remote repositories.

```bash
# List remote repositories
git remote

# List with URLs
git remote -v

# Add a remote
git remote add <name> <url>

# Remove a remote
git remote remove <name>

# Rename a remote
git remote rename <old-name> <new-name>

# Change remote URL
git remote set-url <name> <new-url>

# View remote details
git remote show <name>

# Set upstream for current branch
git remote set-url --push origin <url>
```

**Use Case:** Connect to GitHub, GitLab, or other Git hosting. DevOps teams manage multiple remotes for different environments.

### `git push`

**Description:** Upload local commits to remote repository.

```bash
# Push current branch
git push

# Push specific branch
git push origin <branch-name>

# Push with upstream tracking
git push -u origin <branch-name>

# Force push (use cautiously!)
git push --force

# Force with lease (safer force push)
git push --force-with-lease

# Push all branches
git push --all

# Push all tags
git push --tags

# Delete remote branch
git push origin --delete <branch-name>
git push origin :<branch-name>

# Push specific commit
git push origin <commit-hash>:refs/heads/<branch-name>
```

**Use Case:** Share commits with team. DevOps use force-with-lease for safe force pushes in automation.

### `git pull`

**Description:** Fetch remote changes and merge them locally.

```bash
# Pull from default remote
git pull

# Pull from specific remote
git pull origin <branch-name>

# Pull with rebase instead of merge
git pull --rebase

# Pull and show what changed
git pull --verbose
```

**Use Case:** Sync with team changes. Essential for collaborative development and deployment workflows.

### `git fetch`

**Description:** Download remote changes without merging.

```bash
# Fetch from all remotes
git fetch --all

# Fetch from specific remote
git fetch origin

# Fetch all tags
git fetch --tags

# Fetch with pruning (remove deleted remote branches)
git fetch --prune

# Fetch specific branch
git fetch origin <branch-name>
```

**Use Case:** Check for updates before merging. DevOps use fetch in automated scripts before deploying.

## Advanced Commands

### `git rebase`

**Description:** Re-apply commits on top of another branch (rewrite history).

```bash
# Rebase current branch onto another
git rebase <branch-name>

# Interactive rebase (edit, squash, reorder commits)
git rebase -i HEAD~n

# Rebase onto specific commit
git rebase <commit-hash>

# Continue after resolving conflicts
git rebase --continue

# Abort rebase
git rebase --abort

# Rebase with autostash (stash changes automatically)
git rebase --autostash
```

**Use Case:** Clean up commit history before merging. MERN developers use interactive rebase to squash commits.

### `git cherry-pick`

**Description:** Apply specific commits from one branch to another.

```bash
# Cherry-pick a commit
git cherry-pick <commit-hash>

# Cherry-pick multiple commits
git cherry-pick <hash1> <hash2> <hash3>

# Cherry-pick range of commits
git cherry-pick <hash1>..<hash2>

# Cherry-pick and edit commit message
git cherry-pick -e <commit-hash>

# Cherry-pick without committing
git cherry-pick --no-commit <commit-hash>

# Continue after resolving conflicts
git cherry-pick --continue

# Abort cherry-pick
git cherry-pick --abort
```

**Use Case:** Apply bug fixes to multiple branches. Essential in DevOps for selective backporting.

## Stashing & Cleanup

### `git stash`

**Description:** Temporarily save changes without committing.

```bash
# Stash current changes
git stash

# Stash with description
git stash save "Description"
git stash push -m "Description"

# Stash untracked files too
git stash -u
git stash --include-untracked

# List stashes
git stash list

# Show stash contents
git stash show stash@{0}

# Show stash as patch
git stash show -p stash@{0}

# Apply stash (keeps it in list)
git stash apply stash@{0}

# Pop stash (removes from list)
git stash pop stash@{0}

# Delete specific stash
git stash drop stash@{0}

# Clear all stashes
git stash clear

# Create branch from stash
git stash branch <branch-name> stash@{0}
```

**Use Case:** Save work temporarily when switching branches. MERN developers use stash when context-switching.

### `git clean`

**Description:** Remove untracked files from working directory.

```bash
# Show what would be deleted
git clean -n
git clean --dry-run

# Remove untracked files
git clean -f

# Remove untracked files and directories
git clean -fd

# Remove untracked files, directories, and ignored files
git clean -fdx

# Interactive mode
git clean -i
```

**Use Case:** Clean workspace. DevOps use this in scripts to prepare for deployment.

### `git reset`

**Description:** Move HEAD pointer and unstage files.

```bash
# Unstage file
git reset <filename>

# Unstage all files
git reset

# Soft reset (keep changes in working directory)
git reset --soft HEAD~1

# Mixed reset (default, unstages changes)
git reset --mixed HEAD~1

# Hard reset (discard all changes)
git reset --hard HEAD~1

# Reset to specific commit
git reset --hard <commit-hash>

# Reset specific file to commit
git reset <commit-hash> -- <filename>
```

**Use Case:** Undo commits, unstage files. Use hard reset cautiously - it discards changes permanently.

## Rebasing & Cherry-picking

### `git revert`

**Description:** Create new commits that undo previous commits.

```bash
# Revert last commit
git revert HEAD

# Revert specific commit
git revert <commit-hash>

# Revert without committing
git revert --no-commit <commit-hash>

# Revert range of commits
git revert --no-commit <hash1>..<hash2>

# Continue after resolving conflicts
git revert --continue

# Abort revert
git revert --abort
```

**Use Case:** Safely undo commits in shared repositories. DevOps prefer revert over reset for published commits.

## Debugging & History

### `git blame`

**Description:** Show who changed each line of a file.

```bash
# Show blame for file
git blame <filename>

# Show blame with email
git blame -l <filename>

# Ignore whitespace changes
git blame -w <filename>

# Show line range
git blame -L 10,20 <filename>
```

**Use Case:** Track down who introduced code. Useful for code reviews and debugging in MERN projects.

### `git bisect`

**Description:** Binary search through commit history to find the bug.

```bash
# Start bisect
git bisect start

# Mark current commit as bad
git bisect bad

# Mark specific commit as good
git bisect good <commit-hash>

# Test and mark commits
git bisect bad  # or git bisect good

# End bisect
git bisect reset
```

**Use Case:** Find which commit introduced a bug. Automated in DevOps deployment verification.

### `git grep`

**Description:** Search for patterns in tracked files.

```bash
# Search for pattern
git grep "search-term"

# Case insensitive search
git grep -i "term"

# Search with line numbers
git grep -n "term"

# Search in specific file
git grep "term" -- path/to/file

# Count matches
git grep -c "term"

# Search in specific commit/branch
git grep "term" origin/main
```

**Use Case:** Find code across repository. DevOps use this in scripts to validate configurations.

## DevOps & CI/CD Operations

### `git show`

**Description:** Display information about commits, tags, or objects.

```bash
# Show last commit
git show

# Show specific commit
git show <commit-hash>

# Show specific file at commit
git show <commit-hash>:<filename>

# Show tag details
git show <tag-name>
```

**Use Case:** Examine commits in detail. DevOps use this in deployment validation scripts.

### `git shortlog`

**Description:** Summarize commit logs by author.

```bash
# Show commit count by author
git shortlog

# Show emails
git shortlog -e

# Show numbers only
git shortlog -sn

# For specific range
git shortlog -sn main..develop
```

**Use Case:** Generate release notes and contributor lists. Essential for DevOps release documentation.

### `git reflog`

**Description:** Show reference logs (recovery tool).

```bash
# Show reflog
git reflog

# Show for specific branch
git reflog show <branch-name>

# Recover deleted commit
git reflog

# Then checkout the commit
git checkout <commit-hash>
```

**Use Case:** Recover deleted commits or lost work. Critical safety feature in DevOps operations.

### `git fsck`

**Description:** File system check for repository integrity.

```bash
# Check repository integrity
git fsck

# Find dangling objects
git fsck --lost-found

# Check all object types
git fsck --full
```

**Use Case:** Verify repository health. DevOps run this periodically on backup systems.

## Best Practices & Workflows

### Typical MERN Development Workflow

```bash
# 1. Create feature branch
git switch -c feature/user-authentication

# 2. Make changes
# ... code ...

# 3. Review changes
git diff

# 4. Stage changes
git add .

# 5. Commit with meaningful message
git commit -m "feat: implement user authentication"

# 6. Push to remote
git push -u origin feature/user-authentication

# 7. Create Pull Request (on GitHub)

# 8. After approval, merge (can be done via GitHub)

# 9. Delete local and remote branch
git switch main
git pull
git branch -d feature/user-authentication
git push origin --delete feature/user-authentication
```

### DevOps Deployment Workflow

```bash
# 1. Fetch latest changes
git fetch origin

# 2. Check deployment branch
git checkout origin/main

# 3. Verify deployment
git log -n 5 --oneline

# 4. Create deployment tag
git tag -a v1.2.3 -m "Release v1.2.3"

# 5. Push tag
git push origin v1.2.3

# 6. Deploy using tag
# ... deployment script ...
```

### Commit Message Best Practices

```bash
# Format: <type>(<scope>): <subject>
# Types: feat, fix, docs, style, refactor, test, chore

# Good examples:
git commit -m "feat(api): add user registration endpoint"
git commit -m "fix(auth): resolve session timeout issue"
git commit -m "docs(readme): update installation instructions"
git commit -m "refactor(database): optimize query performance"
```

## Advanced Tips for DevOps & MERN Developers

### Create Git Aliases for Common Commands

```bash
git config --global alias.st status
git config --global alias.co checkout
git config --global alias.br branch
git config --global alias.ci commit
git config --global alias.unstage 'reset HEAD --'
git config --global alias.last 'log -1 HEAD'
git config --global alias.visual 'log --graph --oneline --all'
```

### Setup GPG Signing for Commits

```bash
# List GPG keys
gpg --list-secret-keys

# Configure Git to sign commits
git config --global user.signingkey <key-id>

# Sign commit
git commit -S -m "Signed commit"

# Verify signed commits
git log --show-signature

# Auto-sign all commits
git config --global commit.gpgsign true
```

### Configuration for Large Teams

```bash
# Set pre-commit hook
git config --global core.hooksPath .githooks

# Enable automatic garbage collection
git config --global gc.autodetach true

# Set merge strategy
git config --global pull.rebase true
```

## Troubleshooting Common Issues

### Undo Last Push

```bash
git push --force-with-lease origin HEAD~1:branch-name
```

### Recover Deleted Branch

```bash
git reflog
git checkout <commit-hash>
git switch -c <branch-name>
```

### Merge Conflict Resolution

```bash
# View conflicts
git diff

# After resolving manually
git add <resolved-files>
git commit -m "Resolve merge conflicts"
```

### Large Files in Repository

```bash
# Find large files
git rev-list --all --objects | sort -k2 | tail -10

# Use git-lfs for large files
git lfs install
git lfs track "*.psd"
git add .gitattributes
```

## Essential Reference

| Command      | Purpose                    |
| ------------ | -------------------------- |
| `git status` | Check repository state     |
| `git log`    | View commit history        |
| `git diff`   | Compare changes            |
| `git branch` | Manage branches            |
| `git merge`  | Combine branches           |
| `git push`   | Upload commits             |
| `git pull`   | Download and merge changes |
| `git stash`  | Temporarily save work      |
| `git rebase` | Rewrite history cleanly    |
| `git tag`    | Mark versions              |

## Resources

- [Official Git Documentation](https://git-scm.com/doc)
- [GitHub Guides](https://guides.github.com)
- [Atlassian Git Tutorials](https://www.atlassian.com/git)
- [Git - the simple guide](https://rogerdudler.github.io/git-guide/)

**Last Updated:** 2024
**For:** DevOps Engineers, MERN Stack Developers, and Full-Stack Teams

**Author:** [Md Ismail](https://github.com/md-ismaeel)
