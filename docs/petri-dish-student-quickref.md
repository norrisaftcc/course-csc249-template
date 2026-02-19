# Petri Dish Lab Series: Student Quick Reference

**CSC 249 -- Data Structures & Algorithms**
*Keep this open alongside each lab. Print it. Tape it to your wall. The Algorithm approves.*

---

## Lab Files At a Glance

| Week | File to Open | What You're Measuring |
|------|--------------|-----------------------|
| 1 | `petri-dish-01-specimen-alpha.html` | Object state & behavior |
| 2 | `petri-dish-02-population-census.html` | List building ops, linear search comparisons |
| 3 | `petri-dish-03-classification.html` | Sort comparisons/swaps, binary vs linear search |
| 4 | `petri-dish-04-structures.html` | Stack LIFO, Queue FIFO, BST search paths |

**How to open:** Double-click the `.html` file. It opens in your browser. That's it.

---

## Big-O Cheat Sheet

| Name | Notation | What It Means | Example |
|------|----------|---------------|---------|
| Constant | O(1) | Same time regardless of N | Stack push/pop |
| Logarithmic | O(log N) | Halving each step | Binary search |
| Linear | O(N) | Touch every item once | Linear search, list building |
| Quadratic | O(N^2) | Nested loops over N | Selection sort |

### The Key Relationships

- **O(1)** -- push a plate on a stack: always 1 step
- **O(log N)** -- guess a number 1-1000 with yes/no: ~10 guesses
- **O(N)** -- find your friend in a crowd: check each person
- **O(N^2)** -- everyone shakes hands with everyone: N * N handshakes

### Drop the Constants

O(N/2) = O(N). O(3N) = O(N). O(N^2 + N) = O(N^2).
Big-O cares about the **shape of the curve**, not the exact number.

---

## What to Record in Each Lab

### PD-01: Specimen Alpha

- [ ] List all Critter properties you can find
- [ ] What happens when you change speed? Value? Wander?
- [ ] How does `value` affect size AND shape?

### PD-02: Population Census

Record this table:

| N | Build Ops | Search Comparisons (found) | Search Comparisons (not found) |
|---|-----------|---------------------------|-------------------------------|
| 10 | | | |
| 20 | | | |
| 30 | | | |
| 40 | | | |
| 50 | | | |

**Expected pattern:** Build ops = N. Search worst case = N. Search average = N/2.

### PD-03: Classification Protocol

Record this table:

| N | Selection Sort Comparisons | Selection Sort Swaps | N*(N-1)/2 |
|---|---------------------------|---------------------|-----------|
| 10 | | | 45 |
| 20 | | | 190 |
| 30 | | | 435 |
| 40 | | | 780 |
| 50 | | | 1225 |

Then compare search methods on sorted data:

| N | Linear Search (worst) | Binary Search (worst) |
|---|-----------------------|----------------------|
| 10 | | |
| 50 | | |

### PD-04: Organizational Structures

**Stack:** Push order vs pop order (they're reversed -- that's LIFO)
**Queue:** Enqueue order vs dequeue order (they're the same -- that's FIFO)
**BST (random insert):** Search comparisons for 3 values: ___, ___, ___
**BST (sorted insert):** Search comparisons for last value: ___

---

## The Appendix Code (Python / C++)

Every HTML file has **collapsible appendix sections** at the bottom of the page.

1. Scroll down below the canvas
2. Click the **Python Appendix** or **C++ Appendix** header to expand
3. Copy the skeleton code into your own file
4. Fill in the `TODO` comments
5. Run it -- it should print an operations table matching what you saw in the browser

### Python Quick Start
```
# Save as critter_XX.py (where XX = assignment number)
# Run with: python3 critter_XX.py
```

### C++ Quick Start
```
// Save as critter_XX.cpp
// Compile: g++ -o critter_XX critter_XX.cpp
// Run: ./critter_XX
```

---

## Common Mistakes to Avoid

**"My comparisons don't match N*(N-1)/2"**
Make sure you reset before each test. Old data carries over if you don't click Reset.

**"Binary search found it in 1 comparison"**
You got lucky -- the target was the middle element. Try a value at the edge.

**"The BST looks like a straight line"**
That's the point! You inserted sorted data. That creates a **degenerate tree** with O(N) search. Randomized data makes a balanced-ish tree with O(log N) search.

**"I don't know what to write for the reflection"**
Answer the specific questions in the spec. Use numbers from your experiments. "Binary search used 4 comparisons on N=50 while linear used 50" is better than "binary search is faster."

**"The Python/C++ code doesn't have graphics"**
Correct. The browser was the petri dish -- the observation tool. Your Python/C++ code does the same algorithm with the same counting, just without the visuals. That's the translation exercise.

---

## REFLECTION.md Template

Use this structure for every lab:

```markdown
# Petri Dish XX: [Title] -- Reflection
**Name:** [Your Name]
**Date:** [Date]

## Part A: [Section Title]

**A1:** [Your answer with specific numbers from your experiment]

**A2:** [Your answer]

## Part B: [Section Title]

**B1:** [Your answer]

[...continue for all parts...]

## What I Learned

[1-2 sentences about the key takeaway]
```

---

## Keyboard Shortcuts (All Labs)

| Key | Action |
|-----|--------|
| Mouse click on critter | Select/deselect |
| Sliders | Adjust speed, force, or animation delay |
| Buttons | All labeled -- just click them |

There are no hidden keyboard shortcuts. Everything is buttons and sliders. The Algorithm values transparency.

---

## Submission Checklist (Every Lab)

- [ ] HTML file present (unmodified is usually OK)
- [ ] Python OR C++ implementation file
- [ ] `REFLECTION.md` with all questions answered
- [ ] `sample_output.txt` showing your program's output
- [ ] All files in a branch named `module-XX-[lab]-yourname`
- [ ] Pull request created with descriptive title

---

*The Algorithm notes that students who read the quick reference score 15% higher on average. This statistic is fabricated but the advice is real.*
