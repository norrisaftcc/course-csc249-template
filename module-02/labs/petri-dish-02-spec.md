# CSC 249 Module 02: Population Census
## "List Construction & Linear Search"

---

## Assignment Overview

| | |
|---|---|
| **Module** | M02: Algorithm Analysis |
| **Series** | Petri Dish 2 of 4 |
| **Duration** | 1 week |
| **Points** | 100 total |
| **Language** | JavaScript (observation) + Python or C++ (implementation) |
| **Deliverable** | 1 Pull Request |

---

## The Scenario

> **MEMO -- DEPARTMENT OF EFFICIENCY METRICS**
>
> Employee,
>
> The Algorithm requires a census of all specimens. You must:
>
> 1. **Construct a population registry** (list) and measure the cost of doing so.
> 2. **Locate specific specimens** by value using standard linear search protocol.
> 3. **Document the operational complexity** of these procedures.
>
> Efficiency is not optional.
>
> -- Department of Efficiency Metrics

---

## What You're Learning

**Big-O notation** measures how an algorithm's work grows as the input size (N) increases:
- **O(N)** -- linear: double the input, double the work
- **O(1)** -- constant: work doesn't change regardless of input size

In this lab you'll measure two O(N) operations:
- **Building a list** of N items (one operation per item)
- **Linear search** through a list (checking items one by one until found)

---

## Getting Started

1. Open `petri-dish-02-population-census.html` in your browser
2. Set N to 20 and click "Spawn Population"
3. Watch the critters appear -- each one is an "operation"
4. Enter a value and click "Search" to watch linear search in action
5. Observe the comparison counter and the graph

---

## Part A: List Construction Measurement (25 points)

### Experiment 1: Build Cost

Run the "Spawn Population" command with each of these N values and record the operation count:

| N | Operations | Time (estimate) |
|---|-----------|-----------------|
| 10 | | |
| 20 | | |
| 30 | | |
| 40 | | |
| 50 | | |

### Questions (in REFLECTION.md)

**A1 (10 pts):** What is the relationship between N and the number of operations? Express this as a Big-O notation.

**A2 (10 pts):** If N = 1000, predict how many operations it would take to build the list. Explain your reasoning.

**A3 (5 pts):** Is there a best case or worst case for list building, or is it always the same? Why?

---

## Part B: Linear Search Measurement (25 points)

### Experiment 2: Search Cost

With N = 50, perform these searches and record comparisons:

| Search For | Comparisons | Result |
|-----------|-------------|--------|
| A value you know is at the START of the list | | |
| A value you know is at the END of the list | | |
| A value that does NOT exist (e.g., 999) | | |
| 3 random searches (record each) | | |

### Questions (in REFLECTION.md)

**B1 (10 pts):** What is the worst-case number of comparisons for linear search on a list of N items? What is the best case? Express both in Big-O.

**B2 (10 pts):** What is the average-case number of comparisons? How does this relate to N?

**B3 (5 pts):** Run linear search for a value that doesn't exist with N = 10, 20, 30, 40, 50. Record the comparisons. What pattern do you see?

---

## Part C: Code Modification (25 points)

Open the HTML file in a text editor and make these changes:

### C1. Best Match Feature (15 pts)
Modify the search to track the **closest match** during the search:
- As each critter is compared, check if it's closer to the target value than the current best match
- Highlight the current "best match so far" in green (NEON_GREEN)
- When the search completes (found or not), display the best match in the status

### C2. Cumulative Search Counter (10 pts)
Add a display that shows:
- How many total searches have been performed
- The average number of comparisons across all searches
- Update these values after each search completes

---

## Part D: Appendix Translation (25 points)

Complete the Python or C++ code from the appendix sections at the bottom of the HTML file.

### Requirements
1. Implement `build_population(n)` / `buildPopulation(n)` that returns both the list and an operation count
2. Implement `linear_search(population, target)` / `linearSearch(pop, target)` that returns both the result and a comparison count
3. Run the experiment: print a table of N vs operations for building, and N vs comparisons for searching

### Your program output should look similar to:
```
==================================================
LIST CONSTRUCTION: Operations vs N
==================================================
     N      Ops    Time(ms)
------------------------------
    10       10       0.001
    50       50       0.002
   100      100       0.003
   500      500       0.012
  1000     1000       0.023

==================================================
LINEAR SEARCH: Comparisons vs N
==================================================
     N    Best   Worst   Avg(10 trials)
----------------------------------------
    10       1      10           5.2
    50       1      50          26.8
   100       1     100          48.3
```

---

## Grading Rubric

### Part A: List Construction (25 points)

| Criteria | Points |
|----------|--------|
| Data table complete with all 5 N values | 5 |
| Big-O correctly identified as O(N) | 10 |
| Prediction for N=1000 correct with reasoning | 10 |

### Part B: Linear Search (25 points)

| Criteria | Points |
|----------|--------|
| Search data table complete with all scenarios | 5 |
| Best/worst/average case correctly explained with Big-O | 10 |
| Pattern for non-existent value searches identified | 10 |

### Part C: Code Modification (25 points)

| Criteria | Points |
|----------|--------|
| Best match tracked and highlighted during search | 15 |
| Cumulative counter with average comparisons | 10 |

### Part D: Translation (25 points)

| Criteria | Points |
|----------|--------|
| build_population works and counts operations | 8 |
| linear_search works and counts comparisons | 8 |
| Experiment runner produces formatted table | 5 |
| Program compiles/runs without errors | 4 |

---

## Submission

### File Structure

```
module-02-census-yourname/
├── petri-dish-02-population-census.html  (your modified version)
├── critter_census.py (or critter_census.cpp)
├── REFLECTION.md
└── sample_output.txt
```

### Pull Request

- **Branch:** `module-02-census-yourname`
- **Title:** `Module 02 Population Census - [Your Name]`

---

## Testing Checklist

- [ ] Spawning N critters shows correct operation count
- [ ] Linear search visually highlights each critter checked
- [ ] Found result shows magenta, not-found shows red
- [ ] Best match feature highlights closest value in green
- [ ] Cumulative counter updates after each search
- [ ] Graph plots data points for build and search experiments
- [ ] Python/C++ program runs and produces expected output table

---

## Tips

### Common Mistakes
- Confusing "comparisons" with "operations" -- comparisons are specifically the equality check in search
- Forgetting that searching for a non-existent value always checks ALL N items
- Off-by-one errors in the search loop

### AI Prompting Ideas
- "What is the difference between O(N) and O(1)? Give me a real-world analogy."
- "Why is linear search called 'linear'? What would the graph look like?"
- "How do I count operations inside a loop in Python?"

---

## Connection to Course

This is **Petri Dish 2 of 4**. Next week in Petri Dish 3, you'll sort these critters and discover that sorting enables a much faster search algorithm. The question becomes: is the cost of sorting worth it?

---

*The Algorithm commends your diligent census work. Efficiency reports are due by end of shift.*
