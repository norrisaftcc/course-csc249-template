# Module 04: Linear Structures

**Weeks:** 7-8
**AlgoCratic Department:** Department of Task Processing & Department of Personnel Management

## Overview

This module covers three fundamental linear data structures that form the backbone of countless algorithms and systems:

1. **Stacks** - Last In, First Out (LIFO)
2. **Queues** - First In, First Out (FIFO)
3. **Linked Lists** - Dynamic node-based sequences

## Learning Objectives

By the end of this module, you will be able to:

- Implement stack operations (push, pop, peek) and explain LIFO behavior
- Implement queue operations (enqueue, dequeue, front) and explain FIFO behavior
- Build singly and doubly linked lists with insert, remove, and traversal operations
- Analyze the time complexity of operations on each structure
- Choose the appropriate linear structure for a given problem
- Implement practical applications using stacks and queues

## Module Contents

### Tutorials
- [Stacks](tutorials/stacks.md) - Stack concepts and array-based implementation
- [Queues](tutorials/queues.md) - Queue concepts and implementation strategies
- [Linked Lists](tutorials/linked-lists.md) - Node-based dynamic structures

### Labs
- [Lab: Undo System](labs/lab-undo-system/) - Build a stack-based action reversal system
- [Lab: Request Queue](labs/lab-request-queue/) - Build a FIFO citizen request processor
- [Lab: Linked List Operations](labs/lab-linked-list/) - Implement core linked list functionality

### Homework
- [Inventory Shop](homework/inventory-shop/) - Video game shop using linked lists

### Reference Code
- [code/cpp/](code/cpp/) - C++ implementations
- [code/python/](code/python/) - Python implementations

## The Scenario

> **MEMO — DEPARTMENT OF TASK PROCESSING**
>
> Employee,
>
> The Algorithm has detected inefficiencies in departmental operations. Multiple systems require your attention:
>
> 1. **Action Reversal System** — Employees frequently make errors. A system to undo recent actions is required. (Stack)
>
> 2. **Citizen Request Queue** — Requests must be processed in order of arrival. No exceptions. First In, First Out. (Queue)
>
> 3. **Personnel Records** — The Department of Personnel Management requires a flexible system for managing employee records that can efficiently insert and remove entries. (Linked List)
>
> Your compliance rating depends on successful implementation.
>
> — Department of Task Processing

## Prerequisites

- Module 01: Objects and Classes (class design, encapsulation)
- Module 02: Algorithm Analysis (Big O notation)
- Module 03: Arrays and Sorting (array operations)

## Key Concepts

### When to Use Each Structure

| Structure | Use When... | Examples |
|-----------|-------------|----------|
| **Stack** | Most recent item matters most | Undo, browser back, recursion |
| **Queue** | Order of arrival matters | Print jobs, BFS, task scheduling |
| **Linked List** | Frequent insertions/deletions | Dynamic collections, implementing stacks/queues |

### Complexity Comparison

| Operation | Stack (array) | Queue (array) | Linked List |
|-----------|---------------|---------------|-------------|
| Insert at end | O(1) | O(1) | O(1) with tail |
| Insert at front | O(n) | O(n) | O(1) |
| Remove from end | O(1) | O(n) | O(n) or O(1) doubly |
| Remove from front | O(n) | O(1)* | O(1) |
| Access by index | O(1) | O(1) | O(n) |

*With proper implementation (circular buffer or deque)

## Assessment

See [assignment-spec.md](assignment-spec.md) for full requirements.

| Component | Points |
|-----------|--------|
| Part A: Stack Implementation | 40 |
| Part B: Queue Implementation | 40 |
| Part C: Reflection | 20 |
| **Total** | **100** |

## Resources

### Visualizations
- [VisuAlgo - Linked List](https://visualgo.net/en/list)
- [USFCA - Stack Visualization](https://www.cs.usfca.edu/~galles/visualization/StackArray.html)
- [USFCA - Queue Visualization](https://www.cs.usfca.edu/~galles/visualization/QueueArray.html)

### Readings
- Runestone Academy: [Linear Structures](https://runestone.academy/ns/books/published/pythonds/BasicDS/toctree.html)

---

*The Algorithm appreciates your orderly processing of tasks.*
