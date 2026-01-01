# CSC 249: GitHub Workflow & Pull Request Guide
## How We Submit Work in This Course

---

## Overview

In this course, you submit assignments via **pull requests (PRs)** to the course repository. This mirrors real-world software development workflow and builds skills employers expect.

**Why PRs instead of Blackboard uploads?**
- Version control is a workforce essential
- You build a portfolio of work
- Code review is how teams collaborate
- You learn Git (required for almost every dev job)

---

## One-Time Setup (Week 1)

### Step 1: Install Git
- **Windows:** [Git for Windows](https://gitforwindows.org/)
- **Mac:** `xcode-select --install` (or install via Homebrew)
- **Linux:** `sudo apt install git` (or your package manager)

### Step 2: Configure Git
```bash
git config --global user.name "Your Name"
git config --global user.email "your.email@student.edu"
```

### Step 3: Fork the Course Repository
1. Go to the course repo: `https://github.com/[instructor]/csc249`
2. Click **Fork** (top right)
3. You now have your own copy at `https://github.com/[your-username]/csc249`

### Step 4: Clone Your Fork Locally
```bash
git clone https://github.com/[your-username]/csc249.git
cd csc249
```

### Step 5: Add Upstream Remote
```bash
git remote add upstream https://github.com/[instructor]/csc249.git
```

Now you have:
- `origin` → your fork (where you push)
- `upstream` → course repo (where you submit PRs)

---

## Assignment Workflow (Every Assignment)

### Step 1: Sync Your Fork
Before starting new work, make sure you have the latest course materials:

```bash
git checkout main
git fetch upstream
git merge upstream/main
git push origin main
```

### Step 2: Create a Branch for the Assignment
**Never work directly on main.** Create a branch for each assignment:

```bash
git checkout -b m2a-fieldguide-yourname
```

**Branch naming convention:**
```
[module]-[assignment]-[yourname]

Examples:
  m2a-fieldguide-janedoe
  m2b-translation-janedoe
  m5-sorting-janedoe
  m9-bst-janedoe
```

### Step 3: Do Your Work
- Create/edit files in the appropriate module folder
- Test your code locally
- Make commits as you go (see commit guidelines below)

### Step 4: Commit Your Changes
```bash
git add .
git commit -m "M2A: Complete data structures field guide"
```

**Commit message format:**
```
[Module]: Brief description of what you did

Examples:
  M2A: Complete data structures field guide
  M2B: Add translated Python code and fix AI errors
  M5: Implement selection sort with benchmarks
  M9: Add BST insert and search methods
```

### Step 5: Push Your Branch
```bash
git push origin m2a-fieldguide-yourname
```

### Step 6: Create the Pull Request
1. Go to your fork on GitHub
2. You'll see a prompt: "Compare & pull request" — click it
3. **Base repository:** `[instructor]/csc249` | **base:** `main`
4. **Head repository:** `[your-username]/csc249` | **compare:** `m2a-fieldguide-yourname`
5. Fill out the PR template (see below)
6. Click **Create pull request**

---

## Pull Request Template

When you create a PR, use this format in the description:

```markdown
## Assignment
[Module and assignment name, e.g., "M2A: Data Structures Field Guide"]

## What's Included
- [List the files you're submitting]
- [e.g., M2A_FieldGuide_JaneDoe.md]

## Checklist
- [ ] Code compiles/runs without errors
- [ ] All required sections completed
- [ ] Files are in the correct folder
- [ ] Branch name follows convention
- [ ] Commit messages are descriptive

## AI Tools Used
[List which AI assistants you used and for what purpose]
- Claude: Used for data structure explanations in Part A
- GitHub Copilot: Used for code completion in Part B

## Questions or Concerns
[Optional: anything you want the instructor to know]
```

---

## PR Title Convention

```
[Module] [Assignment Name] - [Your Name]

Examples:
  M2A Field Guide - Jane Doe
  M2B Translation - Jane Doe
  M5 Sorting Lab - Jane Doe
  M9 BST Implementation - Jane Doe
```

---

## After Submission

### What Happens Next
1. Instructor reviews your PR
2. You may receive comments requesting changes
3. If changes needed:
   - Make fixes on the same branch
   - Commit and push — PR updates automatically
4. Once approved, instructor merges your PR

### Responding to Feedback
```bash
# You're still on your assignment branch
git checkout m2a-fieldguide-yourname

# Make requested changes
# ...edit files...

git add .
git commit -m "M2A: Address review feedback - fix markdown formatting"
git push origin m2a-fieldguide-yourname
```

The PR updates automatically. No need to create a new PR.

---

## Common Issues & Fixes

### "I committed to main by accident"
```bash
# Undo the last commit (keeps your changes)
git reset HEAD~1

# Create the correct branch
git checkout -b m2a-fieldguide-yourname

# Now commit properly
git add .
git commit -m "M2A: Complete field guide"
```

### "I need to update my fork"
```bash
git checkout main
git fetch upstream
git merge upstream/main
git push origin main
```

### "My PR has merge conflicts"
```bash
git checkout your-branch-name
git fetch upstream
git merge upstream/main
# Resolve conflicts in your editor
git add .
git commit -m "Resolve merge conflicts"
git push origin your-branch-name
```

### "I want to start over on an assignment"
```bash
# Delete local branch
git checkout main
git branch -D m2a-fieldguide-yourname

# Delete remote branch
git push origin --delete m2a-fieldguide-yourname

# Start fresh
git checkout -b m2a-fieldguide-yourname
```

---

## Quick Reference Card

| Task | Command |
|------|---------|
| Create branch | `git checkout -b branch-name` |
| Switch branches | `git checkout branch-name` |
| Check status | `git status` |
| Stage all changes | `git add .` |
| Commit | `git commit -m "message"` |
| Push branch | `git push origin branch-name` |
| Sync from upstream | `git fetch upstream && git merge upstream/main` |
| See all branches | `git branch -a` |

---

## Folder Structure

Your work should go in the appropriate module folder:

```
csc249/
├── m1-objects/
│   └── YourName/
│       └── [your M1 files]
├── m2-ai-survey/
│   ├── M2A_FieldGuide_YourName.md
│   └── M2B_Translation_YourName/
│       ├── original_code.cpp
│       ├── translated_code.py
│       ├── TRANSLATION_LOG.md
│       └── test_output.txt
├── m3-analysis/
│   └── YourName/
├── m4-recursion/
│   └── YourName/
...
```

---

## Grading & Late Policy

- **On-time PRs:** Full credit available
- **Late PRs:** 10% penalty per day (up to 3 days)
- **PRs more than 3 days late:** Contact instructor

**PR timestamps are official.** The time you create the PR is your submission time.

---

## Getting Help

1. **Git issues:** Post in #git-help channel (Discord/Slack)
2. **Assignment questions:** Post in module-specific channel
3. **PR problems:** Tag instructor in PR comments
4. **AI assistance:** Use your AI tools! They're excellent at Git explanations

---

## Why This Workflow Matters

Every software company uses some version of this:
- **GitHub** at most startups and open source
- **GitLab** at many enterprises
- **Bitbucket** at Atlassian shops
- **Azure DevOps** at Microsoft shops

The specific platform varies, but the concepts are universal:
- Branch for features
- Pull/Merge requests for review
- Code review before merging
- Main branch stays stable

You're not just learning Git — you're learning how software teams collaborate.

---

*Last updated: CSC 249 Course Planning*
