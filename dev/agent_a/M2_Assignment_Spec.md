# CSC 249 Module 2: AI Collaboration & Data Structures Survey
## "Know Your Tools, Know Your Territory"

---

## Overview

**Duration:** 2 weeks  
**Deliverables:** 2 Pull Requests  
**Points:** 100 total (50 + 50)

Module 2 serves two purposes:
1. **Learn to work with AI effectively** — prompting, verifying, correcting
2. **Survey the data structures landscape** — vocabulary and intuition before implementation

By the end of this module, you'll have a personal reference guide to data structures AND experience collaborating with AI on code tasks.

---

## Part A: Data Structures Field Guide (50 points)

### The Task

You are compiling a **field guide** to data structures. Your AI assistant will help you research each structure, but *you* are responsible for the final product.

Interview your AI about each of the following structures:

| Structure | Key Questions to Ask |
|-----------|---------------------|
| Arrays | What is it? How is memory laid out? When is it the right choice? |
| Linked Lists | How does it differ from an array? When would I pick this instead? |
| Stacks | What's LIFO? What real-world problems use stacks? |
| Queues | What's FIFO? How is this different from a stack in practice? |
| Hash Tables | How does hashing work (conceptually)? Why is lookup fast? |
| Trees | What makes something a tree? What's a BST? |
| Heaps | How is a heap different from a BST? What's it good for? |
| Graphs | When is something a graph and not a tree? What are nodes and edges? |

### Deliverable Structure

Create a markdown file called `M2A_FieldGuide_YourName.md` with this format:

```markdown
# Data Structures Field Guide
## Compiled by: [Your Name]
## AI Assistant Used: [Claude/ChatGPT/Copilot/etc.]

---

## Arrays

### My Prompts:
> [Paste the prompts you used]

### AI Response Summary:
[Summarize what the AI told you - don't just paste walls of text]

### My Understanding (in my own words):
[1 paragraph: What is this? When would I use it? What's the tradeoff?]

### Real-World Example:
[One concrete example of where this structure is used]

---

## Linked Lists
[Same format...]
```

### Grading Rubric (50 points)

| Criteria | Points | What We're Looking For |
|----------|--------|------------------------|
| All 8 structures covered | 16 | 2 pts each, complete entries |
| Quality of prompts | 10 | Specific, clear questions that get useful answers |
| Summaries show understanding | 12 | Your words, not just AI regurgitation |
| Real-world examples | 8 | Concrete, plausible applications |
| Markdown formatting | 4 | Clean, readable, properly structured |

### Tips for Good Prompts

**Weak prompt:**
> "Tell me about arrays"

**Strong prompt:**
> "Explain arrays in C++ and Python. How is memory allocated differently? When would I choose an array over a linked list, and what's the tradeoff in terms of insertion speed vs. access speed?"

**Even stronger (for deeper understanding):**
> "I'm a student learning data structures. Explain hash tables to me. Start with the concept of a hash function, then explain what happens during a collision. Use a real-world analogy if possible. Then give me one example where a hash table is clearly better than an array."

---

## Part B: Code Translation (50 points)

### The Task

Take the class you built in Module 1 (or use the provided template if needed) and translate it from one language to the other using AI assistance.

- If you wrote M1 in **C++** → translate to **Python**
- If you wrote M1 in **Python** → translate to **C++**

### The Process

1. **Prompt your AI** to translate the code
2. **Test the translated code** — does it actually run?
3. **Document what happened** — what worked, what broke, what you fixed

### Deliverable Structure

Create a folder called `M2B_Translation_YourName/` containing:

```
M2B_Translation_YourName/
├── original_code.cpp (or .py)
├── translated_code.py (or .cpp)
├── TRANSLATION_LOG.md
└── test_output.txt
```

**TRANSLATION_LOG.md format:**

```markdown
# Code Translation Log
## Original Language: [C++ / Python]
## Target Language: [Python / C++]
## AI Assistant Used: [Claude/ChatGPT/Copilot/etc.]

---

## The Prompt I Used:
> [Paste your translation prompt]

## What the AI Got Right:
- [List things that worked correctly]

## What the AI Got Wrong:
- [List errors, bugs, or issues]
- [Be specific: "Line 23 used `print` syntax but forgot parentheses"]

## Fixes I Made:
- [List corrections you had to make manually]
- [Include before/after if helpful]

## What I Learned:
[1-2 paragraphs: What does this tell you about AI assistance? 
About the differences between C++ and Python?]
```

### Grading Rubric (50 points)

| Criteria | Points | What We're Looking For |
|----------|--------|------------------------|
| Translation compiles/runs | 15 | Working code in target language |
| Functionality preserved | 10 | Does the same thing as original |
| Translation log completeness | 10 | All sections filled out honestly |
| Error documentation | 10 | Specific about what AI got wrong |
| Reflection quality | 5 | Genuine insight, not boilerplate |

### Common Translation Issues to Watch For

**C++ → Python:**
- Semicolons and braces removed
- Type declarations removed
- `cout` → `print()`
- Memory management disappears (no `new`/`delete`)
- AI might forget `self` parameter in methods

**Python → C++:**
- Types must be declared
- Indentation → braces
- `print()` → `cout <<`
- String handling differences
- AI might generate non-compiling code around memory/pointers

---

## Submission Instructions

Submit **two pull requests** to the course repository:

### PR #1: Field Guide
- **Branch name:** `m2a-fieldguide-yourname`
- **PR title:** `M2A Field Guide - [Your Name]`
- **Contains:** `M2A_FieldGuide_YourName.md`

### PR #2: Translation
- **Branch name:** `m2b-translation-yourname`
- **PR title:** `M2B Translation - [Your Name]`
- **Contains:** `M2B_Translation_YourName/` folder with all files

---

## Why This Matters

In the workforce, you will:
- Work in multiple languages (sometimes in the same week)
- Use AI tools to accelerate development
- Need to verify AI output — it's confident but not always correct
- Explain technical concepts to teammates

This module isn't about memorizing definitions. It's about building your toolkit and learning how to learn with AI assistance.

---

## AlgoCratic Memo (Optional Flavor)

> **INTERNAL MEMO — DEPARTMENT OF EMPLOYEE DEVELOPMENT**
>
> Employee,
>
> The Algorithm has determined that your productivity will increase 23.7% with proper tooling orientation. You are hereby assigned to complete the Standard AI Collaboration Protocol and Data Structures Familiarization Module.
>
> Failure to demonstrate competency may result in reassignment to the Legacy Systems Division.
>
> The Algorithm appreciates your cooperation.
>
> — Department of Employee Development

---

*Last updated: CSC 249 Course Planning*
