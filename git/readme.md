# Git – Important & Useful Commands (Clean List)

## 1. Repository Setup

```bash
git init            # Initialize a new Git repository
git clone <url>     # Clone a remote repository
```

## 2. Basic Workflow (Most Used)

```bash
git status          # Check file status
git add <file>      # Add file to staging
git add .           # Add all changes
git commit -m "msg" # Commit changes
git diff            # View unstaged changes
git log             # View commit history
git show <commit>   # Show details of a commit
```

## 3. Branching & Switching

```bash
git branch               # List local branches
git branch -a            # List all branches (local + remote)
git branch -r            # List remote branches
git branch <name>        # Create a new branch
git branch -d <name>     # Delete a branch from local
git branch -D <name>     # Delete a branch from remote
git checkout <branch>    # Switch branch
git checkout -b <name>   # Create & switch branch
```

## 4. Remote Repositories

```bash
git remote -v            # View remote URLs
git fetch                # Fetch changes from remote
git pull                 # Fetch + merge changes
git pull --rebase        # Fetch + rebase changes
git push                 # Push changes to remote
git push -u origin main  # Set upstream & push
```

## 5. Undo & Fix Mistakes

```bash
git restore <file>           # Discard unstaged changes
git reset <file>             # Unstage a file
git reset --hard HEAD        # Reset everything (dangerous)
git revert <commit>          # Safely undo a commit
git clean -f                 # Remove untracked files
```

## 6. Merging

```bash
git merge <branch>       # Merge a branch into current branch
```

## 7. Tags & Releases

```bash
git tag                  # List tags
git tag <tag-name>       # Create a tag
git push origin <tag>    # Push tag to remote
```

## stash

```bash
git stash                 # Save work temporarily
git stash pop             # Restore stashed work
git stash list            # List stashed work
git stash clear           # Clear stashed work
git stash apply <index>   # Apply stashed work
git stash drop <index>    # Discard stashed work
```

## 8. Configuration (One-Time Setup) - Global

```bash
git config --global user.name "Your Name"
git config --global user.email "you@email.com"
git config --list
```

## 9. Helpful Shortcuts

```bash
git log --oneline --graph --all   # Clean commit history view
git diff --staged                 # View staged changes
git stash                         # Save work temporarily
git stash pop                     # Restore stashed work
```

## 10. connect to GitHub with SSH

```bash
ssh-keygen -t ed25519 -C "email"
eval "$(ssh-agent -s)"
ssh-add ~/.ssh/id_ed25519
```

## 11. Rebase commands and hard flags and merge conflicts how to resolve them

### Rebase

```bash
git rebase main         # Rebase current branch onto main
git rebase --abort      # Abort current rebase
git rebase --continue    # Continue current rebase
git rebase --skip        # Skip current commit
```

### Conflict check & resolve

```bash
git status              # Check file status
git diff                # View unstaged changes
git add <file-name>     # Add file to staging
git rebase --continue   # Continue current rebase
```

### Merge

```bash
git merge <branch>      # Merge a branch into current branch
git merge --abort       # Abort current merge
git merge --continue    # Continue current merge
```

### Reset (Hard)

```bash
git reset --hard HEAD
git reset --hard <commit-hash>
git reset --hard origin/main
```
