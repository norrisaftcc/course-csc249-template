---
marp: true
theme: uncover
paginate: true
backgroundColor: #0a0a0f
color: #e0e0ff
style: |
  section {
    font-family: 'Courier New', Consolas, monospace;
  }
  h1 { color: #00fff5; text-shadow: 0 0 20px rgba(0,255,245,0.4); }
  h2 { color: #ff00ff; }
  h3 { color: #39ff14; }
  code { color: #39ff14; background: #12121e; }
  strong { color: #ff6600; }
  em { color: #00fff5; font-style: normal; }
  a { color: #ff00ff; }
  blockquote { border-left: 3px solid #ff00ff; color: #a0a0c0; }
  table { color: #e0e0ff; }
  th { color: #00fff5; border-bottom: 1px solid #2a2a4a; }
  td { border-bottom: 1px solid #1a1a2e; }
---

<!--
  PETRI DISH VISUALIZATION SERIES - LECTURE SLIDES
  CSC 249: Data Structures & Algorithms

  These slides are designed for Marp (https://marp.app) but can be
  adapted for any Markdown-based slide tool (reveal.js, Slidev, etc.)
  or manually converted to Google Slides / PowerPoint.

  Usage: One section per Petri Dish assignment. Each section is
  designed for a ~15 minute recorded YouTube segment. Total runtime
  for all 4: ~60 minutes.

  To render with Marp CLI:
    npx @marp-team/marp-cli petri-dish-slides.md -o slides.html
  Or use the Marp VS Code extension for live preview.
-->

# PETRI DISH
## Visualization Series

CSC 249: Data Structures & Algorithms
*Modules 01 - 04*

---

# What is the Petri Dish?

A browser-based lab where you **observe** algorithms in action

- JavaScript + p5.js = interactive visualizations
- **No JS experience needed** -- you observe and measure
- Each lab has Python & C++ appendix code you **implement**
- 4 labs over 4 weeks, building on each other

> "See it, measure it, then build it in your language."

---

# The 4-Week Arc

| Week | Lab | You Learn |
|------|-----|-----------|
| 1 | Specimen Alpha | Objects have state + behavior |
| 2 | Population Census | Building lists is O(N), linear search is O(N) |
| 3 | Classification Protocol | Sorting is O(N^2), binary search is O(log N) |
| 4 | Organizational Structures | Stacks, Queues, and Trees |

---

<!-- _backgroundColor: #0a0a0f -->

# WEEK 1

## Petri Dish 01: Specimen Alpha
### Object Observation Lab

---

# Meet the Critter

A *Critter* is an **object** -- just like the `Course` class from Module 1

**State** (properties):
- `value`, `pos`, `vel`, `size`, `sides`, `maxSpeed`

**Behavior** (methods):
- `wander()`, `separate()`, `update()`, `display()`

The shape and size **map to the value**:
- Low value = small triangle
- High value = large octagon

---

# Demo: What Happens When...

**Speed = 0?**
The critter stops. `maxSpeed` controls `update()`.

**Randomize Value?**
Size AND shape change. Two properties derived from one.

**Add a second critter?**
They repel each other. `separate()` uses distance checks.

### Key Insight
Changing one property can affect multiple visual aspects.
That's **encapsulation** -- data and behavior bundled together.

---

# Your Tasks (PD-01)

### Part A: Observe (20 pts)
List all properties. Experiment with sliders. Describe what you see.

### Part B: Modify (40 pts)
Add an `energy` property that fades the glow over time.
Add a "Feed" button. Improve the trail effect.

### Part C: Translate (40 pts)
Write the `Critter` class in **Python or C++**.
No graphics -- just the data and `update()` math.

---

<!-- _backgroundColor: #0a0a0f -->

# WEEK 2

## Petri Dish 02: Population Census
### List Construction & Linear Search

---

# How Expensive is "Making a List"?

Spawn N critters and count the operations:

| N | Operations |
|---|-----------|
| 10 | 10 |
| 20 | 20 |
| 50 | 50 |

**Pattern:** Operations = N. Always. Every time.

### This is `O(N)` -- Linear Time
Double the input, double the work.

---

# Linear Search: Check Every Single One

Looking for value 42 in a list of 50 critters:

1. Check critter[0] -- nope (orange flash)
2. Check critter[1] -- nope
3. Check critter[2] -- nope
4. ...
5. Check critter[37] -- **FOUND!** (magenta flash)

**37 comparisons** to find it.

What if it's not in the list? **50 comparisons.** All of them.

---

# Linear Search: The Numbers

| Case | Comparisons | Big-O |
|------|------------|-------|
| **Best** | 1 (found first) | O(1) |
| **Worst** | N (not found) | O(N) |
| **Average** | N/2 | O(N) |

"But O(N/2) is O(N) -- we drop constants."

### The Question
Can we do better than checking every item? **Yes. But it costs something.**

---

# Your Tasks (PD-02)

### Part A: Measure list building (25 pts)
Record operations for N = 10, 20, 30, 40, 50

### Part B: Measure linear search (25 pts)
Best case, worst case, not-found case

### Part C: Add "best match" feature (25 pts)
Track the closest value during search

### Part D: Python/C++ implementation (25 pts)
`build_population()` and `linear_search()` with counters

---

<!-- _backgroundColor: #0a0a0f -->

# WEEK 3

## Petri Dish 03: Classification Protocol
### Sorting & Efficient Search

---

# Selection Sort: Imposing Order

**Algorithm:**
1. Scan the unsorted region for the **minimum**
2. **Swap** it into the next sorted position
3. Repeat until everything is sorted

**Cost:** N*(N-1)/2 comparisons

| N | Comparisons | That's... |
|---|------------|-----------|
| 10 | 45 | manageable |
| 50 | 1,225 | getting expensive |
| 1,000 | 499,500 | half a million |

### This is `O(N^2)` -- Quadratic Time
Double N? **Quadruple** the work.

---

# Why Sort? Because Binary Search.

After sorting, we unlock a superpower:

**Binary Search:**
1. Check the **middle** element
2. If target is smaller, discard the **right half**
3. If target is larger, discard the **left half**
4. Repeat on the remaining half

Each step **eliminates half** the remaining items.

---

# Binary Search: The Numbers

| N | Linear Search (worst) | Binary Search (worst) |
|---|----------------------|---------------------|
| 10 | 10 | 4 |
| 100 | 100 | 7 |
| 1,000 | 1,000 | **10** |
| 1,000,000 | 1,000,000 | **20** |

### `O(log N)` -- Logarithmic Time
"How many times can you cut N in half?"

---

# The Tradeoff

**Sorting costs O(N^2). Binary search costs O(log N).**

Is it worth sorting first?

- **1 search:** Just use linear. Don't bother sorting.
- **10 searches:** Maybe sort first.
- **1000 searches on the same data:** Sort once, binary search forever.

> Sorting is an **investment**. Binary search is the **dividend**.

---

# Your Tasks (PD-03)

### Part A: Watch selection sort (25 pts)
Record comparisons for N = 10, 20, 30, 40, 50. Verify they match N*(N-1)/2.

### Part B: Compare search methods (25 pts)
Run both linear and binary search on sorted data. Record the difference.

### Part C: Add insertion sort (25 pts)
Implement a second sort. Compare performance.

### Part D: Python/C++ implementation (25 pts)
`selection_sort()`, `linear_search()`, `binary_search()` with counters

---

<!-- _backgroundColor: #0a0a0f -->

# WEEK 4

## Petri Dish 04: Organizational Structures
### Stacks, Queues & Binary Search Trees

---

# Same Data, Different Rules

The same critters behave completely differently depending on
which **structure** holds them:

| Structure | Add | Remove | Pattern |
|-----------|-----|--------|---------|
| **Stack** | Push (top) | Pop (top) | LIFO |
| **Queue** | Enqueue (back) | Dequeue (front) | FIFO |
| **BST** | Insert by value | Search by value | Sorted hierarchy |

### Key Insight
**Structure determines behavior.**

---

# Stack: Last In, First Out

```
Push A, Push B, Push C

    [ C ]  <-- top (last in)
    [ B ]
    [ A ]

Pop -> C  (first out)
Pop -> B
Pop -> A
```

**Real-world:** Undo button, browser back, function call stack

Both push and pop are **O(1)** -- constant time.

---

# Queue: First In, First Out

```
Enqueue A, Enqueue B, Enqueue C

FRONT -> [ A ] [ B ] [ C ] <- BACK

Dequeue -> A  (first in = first out)
Dequeue -> B
Dequeue -> C
```

**Real-world:** Print queue, message queue, any "line"

Both enqueue and dequeue are **O(1)**.

---

# BST: Sorted Hierarchy

```
Insert: 50, 30, 70, 20, 40

        50
       /  \
     30    70
    /  \
  20    40
```

Search for 40: go right of 30 -> **found!** (2 comparisons)

**Balanced tree:** O(log N) search
**Degenerate tree** (sorted insert): O(N) search -- it's a linked list!

---

# The Degenerate Tree Problem

Insert 10, 20, 30, 40, 50 (in order):

```
10
  \
   20
     \
      30
        \
         40
           \
            50
```

Search for 50: **5 comparisons** = O(N)

"A tree that looks like a linked list IS a linked list."
(Balanced trees fix this -- coming in Module 06)

---

# Your Tasks (PD-04)

### Part A: Stack operations (20 pts)
Push 10, pop 5. Record the order. Explain LIFO.

### Part B: Queue operations (20 pts)
Enqueue 10, dequeue 5. Contrast with stack.

### Part C: BST operations (30 pts)
Insert random data, then sorted data. Compare search costs.

### Part D: Python/C++ implementation (30 pts)
Stack, Queue, and BST classes with comparison counting.

---

# The Big Picture: What You've Learned

| Week | Concept | Big-O |
|------|---------|-------|
| 1 | Objects have state + behavior | -- |
| 2 | List building, linear search | O(N) |
| 3 | Selection sort, binary search | O(N^2), O(log N) |
| 4 | Stacks O(1), Queues O(1), BST O(log N) | Structure matters |

### Next: Hashing, Trees, Graphs
Everything from here builds on these foundations.

---

# One Last Thing

The JavaScript was the **petri dish**.
The Python/C++ was the **real experiment**.
The Big-O was the **discovery**.

> "Bloom's Taxonomy Starts with Create."
> You built it. You measured it. Now you understand it.

*The Algorithm appreciates your cooperation.*
