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
git branch <name>        # Create a new branch
git branch -d <name>     # Delete a branch
git checkout <branch>    # Switch branch
git checkout -b <name>   # Create & switch branch
git branch -a            # List all branches (local + remote)
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

## 8. Configuration (One-Time Setup)

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

