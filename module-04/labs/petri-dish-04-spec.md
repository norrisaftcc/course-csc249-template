# CSC 249 Module 04: Organizational Structures
## "Stacks, Queues & Binary Search Trees"

---

## Assignment Overview

| | |
|---|---|
| **Module** | M04: Linear Structures |
| **Series** | Petri Dish 4 of 4 |
| **Duration** | 1 week |
| **Points** | 100 total |
| **Language** | JavaScript (observation) + Python or C++ (implementation) |
| **Deliverable** | 1 Pull Request |

---

## The Scenario

> **MEMO -- DEPARTMENT OF TASK PROCESSING**
>
> Employee,
>
> The Algorithm has determined that flat lists are insufficient for advanced organizational needs. You will observe how the SAME specimens behave under different structural constraints:
>
> 1. **STACK** -- Last In, First Out processing
> 2. **QUEUE** -- First In, First Out processing
> 3. **BINARY SEARCH TREE** -- Hierarchical sorted organization
>
> Structure determines behavior. Choose wisely.
>
> -- Department of Task Processing

---

## What You're Learning

Three fundamental data structures, each with different rules for insertion and removal:

| Structure | Insert | Remove | Access Pattern |
|-----------|--------|--------|---------------|
| **Stack** | Push (top) O(1) | Pop (top) O(1) | LIFO: Last In, First Out |
| **Queue** | Enqueue (back) O(1) | Dequeue (front) O(1) | FIFO: First In, First Out |
| **BST** | Insert by value O(log N) | Search by value O(log N) | Sorted hierarchy |

The key insight: the **same data** behaves completely differently depending on which structure holds it.

---

## Getting Started

1. Open `petri-dish-04-structures.html` in your browser
2. Click "Generate 10" to create incoming specimens
3. Push specimens onto the stack, enqueue them, and insert into the BST
4. Pop from the stack and dequeue from the queue -- observe the different orders
5. Search the BST and watch the path highlighted

---

## Part A: Stack Operations (20 points)

### Experiment

1. Generate 10 specimens and push all 10 onto the stack
2. Record the values in push order
3. Pop 5 specimens and record the order they come out

### Questions (in REFLECTION.md)

**A1 (10 pts):** In what order did specimens exit the stack? How does this relate to the order they entered? Explain LIFO in your own words.

**A2 (5 pts):** What is the Big-O of push? Of pop? Why are both O(1)?

**A3 (5 pts):** Name a real-world system (not mentioned in class) that behaves like a stack.

---

## Part B: Queue Operations (20 points)

### Experiment

1. Generate 10 new specimens (click "Reset All" first)
2. Enqueue all 10 specimens
3. Dequeue 5 and record the order

### Questions (in REFLECTION.md)

**B1 (10 pts):** In what order did specimens exit the queue? How is this different from the stack? Explain FIFO.

**B2 (5 pts):** If you push items A, B, C onto a stack and enqueue them into a queue, what order does each produce when you remove all three?

**B3 (5 pts):** Name a real-world system that behaves like a queue.

---

## Part C: BST Operations (30 points)

### Experiment 1: Balanced Insertion

1. Generate 10 specimens (random values) and insert all into the BST
2. Search for 3 different values and record the comparison count (path length)

### Experiment 2: Degenerate Tree

1. Click "Reset All", then click "Insert 1-10 (sorted)"
2. Observe the tree shape
3. Search for value 100 and record the comparison count

### Questions (in REFLECTION.md)

**C1 (10 pts):** For the random-insert tree, how many comparisons did each search take? How does this relate to the tree's height?

**C2 (10 pts):** For the sorted-insert tree, why does it look like a linked list? How many comparisons did searching for 100 take? What Big-O is this?

**C3 (10 pts):** What would a perfectly balanced tree of 10 items look like? How would search comparisons differ from the degenerate case? (Draw a sketch in your reflection.)

---

## Part D: Appendix Translation (30 points)

Complete the Python or C++ code from the appendix sections.

### Requirements

1. **Stack class** with push, pop, peek, isEmpty, size (10 pts)
2. **Queue class** with enqueue, dequeue, front, isEmpty, size (10 pts)
3. **BST class** with insert (returns comparison count) and search (returns comparison count) (10 pts)

### Your program should demonstrate:
- Push 5 items, pop all (showing LIFO order)
- Enqueue 5 items, dequeue all (showing FIFO order)
- Insert values [50, 30, 70, 20, 40, 60, 80] into BST, then search for several values
- Insert values 10, 20, 30, ... 100 (sorted) and show the degenerate search cost

---

## Grading Rubric

### Part A: Stack (20 points)

| Criteria | Points |
|----------|--------|
| Push/pop order recorded correctly | 5 |
| LIFO explained clearly with correct ordering | 10 |
| Big-O of push/pop correct, real-world example | 5 |

### Part B: Queue (20 points)

| Criteria | Points |
|----------|--------|
| Enqueue/dequeue order recorded correctly | 5 |
| FIFO explained clearly, contrast with LIFO | 10 |
| A/B/C ordering question correct, real-world example | 5 |

### Part C: BST (30 points)

| Criteria | Points |
|----------|--------|
| Random tree search comparisons recorded | 5 |
| Connection between comparisons and tree height explained | 10 |
| Degenerate tree identified as O(N), explains why | 10 |
| Balanced tree sketch and comparison analysis | 5 |

### Part D: Translation (30 points)

| Criteria | Points |
|----------|--------|
| Stack with all 5 operations | 10 |
| Queue with all 5 operations | 10 |
| BST with insert and search returning comparison counts | 10 |

---

## Submission

### File Structure

```
module-04-structures-yourname/
├── petri-dish-04-structures.html  (unmodified is OK for this assignment)
├── critter_structures.py (or critter_structures.cpp)
├── REFLECTION.md
└── sample_output.txt
```

### Pull Request

- **Branch:** `module-04-structures-yourname`
- **Title:** `Module 04 Organizational Structures - [Your Name]`

---

## Testing Checklist

- [ ] Stack: push adds to top, pop removes from top (LIFO confirmed)
- [ ] Queue: enqueue adds to back, dequeue removes from front (FIFO confirmed)
- [ ] BST: values less than parent go left, greater go right
- [ ] BST search highlights the path from root to target
- [ ] "Insert 1-10 (sorted)" creates a degenerate right-leaning tree
- [ ] Python/C++ program demonstrates all three structures
- [ ] Degenerate BST search for last element shows O(N) comparisons

---

## Connection to Course

This is **Petri Dish 4 of 4** -- the final lab in the visualization series. You've now seen:

1. **Objects** -- state and behavior (Petri Dish 1)
2. **Lists and O(N)** -- linear operations (Petri Dish 2)
3. **Sorting O(N^2) and Binary Search O(log N)** -- the cost of order (Petri Dish 3)
4. **Stacks, Queues, and Trees** -- structure determines behavior (this lab)

These concepts form the foundation for everything else in CSC 249. The rest of the course builds on these data structures with hashing, balanced trees, and graphs.

---

*The Algorithm has noted your completion of the Organizational Structures assessment. Your compliance rating has been updated accordingly.*
