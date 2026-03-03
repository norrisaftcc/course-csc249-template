# CSC 249 Module 03: Classification Protocol
## "Sorting & Efficient Search"

---

## Assignment Overview

| | |
|---|---|
| **Module** | M03: Arrays and Sorting |
| **Series** | Petri Dish 3 of 4 |
| **Duration** | 1 week |
| **Points** | 100 total |
| **Language** | JavaScript (observation) + Python or C++ (implementation) |
| **Deliverable** | 1 Pull Request |

---

## The Scenario

> **MEMO -- DEPARTMENT OF CITIZEN CLASSIFICATION**
>
> Employee,
>
> The unsorted population registry is unacceptable. The Algorithm demands ORDER. You will:
>
> 1. Apply **Selection Sort** to organize specimens by value
> 2. Observe the **O(N^2)** cost of imposing order
> 3. Once sorted, apply **Binary Search** and observe the dramatic improvement over linear search
>
> Order has a cost, but it pays dividends.
>
> -- Department of Citizen Classification

---

## What You're Learning

**Sorting** arranges data in order. **Selection Sort** repeatedly finds the minimum and moves it to the front.
- It always takes N*(N-1)/2 comparisons -- that's **O(N^2)**
- Double N, and comparisons quadruple

**Binary Search** works only on sorted data. It checks the middle, then discards half.
- It takes at most log2(N) comparisons -- that's **O(log N)**
- For N=1000: linear search needs 1000 comparisons, binary search needs about 10

The key insight: **sorting is expensive, but it pays for itself** if you search many times.

---

## Getting Started

1. Open `petri-dish-03-classification.html` in your browser
2. Spawn 20 unsorted critters
3. Click "Selection Sort" and watch the algorithm work step by step
4. After sorting, try both "Linear Search" and "Binary Search" for the same value
5. Compare the comparison counts

---

## Part A: Sorting Observation (25 points)

### Experiment: Sort Cost

Run selection sort on these population sizes and record the metrics:

| N | Comparisons | Swaps | N*(N-1)/2 | Match? |
|---|------------|-------|-----------|--------|
| 10 | | | 45 | |
| 20 | | | 190 | |
| 30 | | | 435 | |
| 40 | | | 780 | |
| 50 | | | 1225 | |

### Questions (in REFLECTION.md)

**A1 (10 pts):** Do the comparisons match N*(N-1)/2 exactly? Why or why not?

**A2 (10 pts):** When N doubles from 25 to 50, comparisons go from 300 to 1225. That's roughly a 4x increase. Why does doubling N cause a 4x increase? What does this tell you about O(N^2)?

**A3 (5 pts):** Does the number of swaps always equal N*(N-1)/2? Why might swaps be different from comparisons?

---

## Part B: Binary Search vs Linear Search (25 points)

### Experiment: Search Comparison

After sorting N=50, search for several values using both methods:

| Target Value | Linear Comparisons | Binary Comparisons | Ratio |
|-------------|-------------------|-------------------|-------|
| (exists, near start) | | | |
| (exists, near middle) | | | |
| (exists, near end) | | | |
| (does not exist) | | | |

### Questions (in REFLECTION.md)

**B1 (10 pts):** For N=1000, how many comparisons would linear search need (worst case)? How many for binary search (worst case)? Show the calculation for binary search using log2(1000).

**B2 (10 pts):** If you need to search a list of 1 million items once, is it worth sorting first? What if you need to search it 1000 times? Explain using the costs: sort = O(N^2), linear search = O(N), binary search = O(log N).

**B3 (5 pts):** What happens if you try binary search on unsorted data? Why doesn't it work?

---

## Part C: Code Modification (25 points)

### C1. Add Insertion Sort (15 pts)
Add an "Insertion Sort" button alongside the existing Selection Sort:
- Implement insertion sort in JavaScript using the same visual animation pattern
- Insertion sort: for each element, shift it left until it's in the right position
- Count and display comparisons and swaps separately
- Use a different highlight color (e.g., NEON_GREEN for the "inserting" element)

### C2. Sort Comparison (10 pts)
After implementing both sorts:
- Run both on the same data (spawn, sort, record; spawn with same N, sort with other algorithm, record)
- Add a comparison display showing which sort used fewer comparisons
- In your REFLECTION.md, describe which sort is better on nearly-sorted data and why

---

## Part D: Appendix Translation (25 points)

Complete the Python or C++ code from the appendix sections.

### Requirements
1. Implement `selection_sort(population)` returning (comparisons, swaps)
2. Implement `linear_search(population, target)` returning (index, comparisons)
3. Implement `binary_search(sorted_pop, target)` returning (index, comparisons)
4. Run experiments printing sort costs and search comparison tables

### Expected output format:
```
SELECTION SORT: Comparisons vs N
     N     Comps   Swaps   N*(N-1)/2
------------------------------------
    10        45       8          45
    20       190      17         190
    50      1225      46        1225

LINEAR vs BINARY SEARCH (sorted data)
     N  Linear(worst)  Binary(worst)  log2(N)
----------------------------------------------
    10             10              4        4
   100            100              7        7
  1000           1000             10       10
```

---

## Grading Rubric

### Part A: Sorting Observation (25 points)

| Criteria | Points |
|----------|--------|
| Sort data table complete for all 5 N values | 5 |
| Explains why comparisons match N*(N-1)/2 | 10 |
| Explains O(N^2) quadrupling behavior | 10 |

### Part B: Search Comparison (25 points)

| Criteria | Points |
|----------|--------|
| Search data table with both methods for 4 targets | 5 |
| Correct calculation of linear vs binary for N=1000 | 10 |
| Cost analysis of sort-then-search vs linear-only | 10 |

### Part C: Code Modification (25 points)

| Criteria | Points |
|----------|--------|
| Insertion sort implemented with correct animation | 15 |
| Sort comparison display, reflection on nearly-sorted data | 10 |

### Part D: Translation (25 points)

| Criteria | Points |
|----------|--------|
| Selection sort returns correct comparison and swap counts | 8 |
| Linear and binary search both work correctly | 8 |
| Experiment runner produces comparison tables | 5 |
| Program compiles/runs without errors | 4 |

---

## Submission

### File Structure

```
module-03-classification-yourname/
├── petri-dish-03-classification.html  (your modified version)
├── critter_classification.py (or critter_classification.cpp)
├── REFLECTION.md
└── sample_output.txt
```

### Pull Request

- **Branch:** `module-03-classification-yourname`
- **Title:** `Module 03 Classification Protocol - [Your Name]`

---

## Testing Checklist

- [ ] Selection sort visually animates: orange scans, magenta minimum, green placed
- [ ] Critters line up left-to-right by value after sorting
- [ ] Binary search dims eliminated halves
- [ ] Comparison counter shows binary search using far fewer comparisons
- [ ] Insertion sort (Part C) animates correctly with different color
- [ ] Python/C++ program produces comparison tables

---

## Connection to Course

This is **Petri Dish 3 of 4**. You've now seen O(N) (Petri Dish 2) and O(N^2) and O(log N) (this lab). Next week in Petri Dish 4, you'll organize these same critters into stacks, queues, and trees -- data structures that give different performance tradeoffs for different operations.

---

*The Algorithm appreciates your service to the Department of Citizen Classification. Disorder will not be tolerated.*
