# CSC 249 Content Mapping Document

## Course Development Tracking System (CDTS) Alignment

**Purpose:** This document maps existing content from two development tracks (agent_a and agent_b) to the 8-module CDTS structure, identifying what exists, where it belongs, and what gaps remain.

**Source Materials:**
- `dev/agent_a/` - 16-module course outline with detailed assignment specifications
- `dev/agent_b/` - Code implementations, tutorials, and conceptual materials
- `_tracking/course-dev-tracking-requirements.md` - CDTS 8-module requirement

---

## Executive Summary

| Metric | Count |
|--------|-------|
| Agent A 16-module topics | 16 |
| Agent B content directories | 8 |
| CDTS target modules | 8 |
| Content items ready to use | 12 |
| Content items needing work | 8 |
| Critical gaps identified | 6 |

---

## Part 1: 16-to-8 Module Consolidation Map

The original agent_a outline spans 16 weeks. CDTS requires exactly 8 modules. The following consolidation preserves logical groupings while meeting the 8-module constraint.

### Proposed 8-Module Structure

| CDTS Module | Name | Agent A Sources | Weeks |
|-------------|------|-----------------|-------|
| **M01** | Foundations: OOP and AI Collaboration | M1 (Objects), M2 (AI Collab) | 1-2 |
| **M02** | Algorithm Analysis and Recursion | M3 (Analysis), M4 (Recursion) | 3-4 |
| **M03** | Arrays and Sorting | M5 (Arrays/Sorting) | 5-6 |
| **M04** | Linear Structures: Stacks, Queues, Lists | M6 (Stacks/Queues), M7 (Linked Lists) | 7-8 |
| **M05** | Hashing and Hash Tables | M8 (Hashing) | 9-10 |
| **M06** | Trees and Binary Search Trees | M9 (Trees/BST), M10 (Heaps), M11 (Balanced) | 11-12 |
| **M07** | Graphs and Graph Algorithms | M12 (Graphs Intro), M13 (Graph Algorithms) | 13-14 |
| **M08** | Integration and Final Project | M14-M16 (Final Project) | 15-16 |

---

## Part 2: Detailed Module Mapping

### M01: Foundations - OOP and AI Collaboration

**Consolidates:** Agent A M1 (Objects/Classes) + M2 (AI Collaboration)

#### Agent A Content Available

| Item | File | Status |
|------|------|--------|
| M2 Assignment Spec (AI Collaboration) | `dev/agent_a/M2_Assignment_Spec.md` | **Ready** - Complete 2-part assignment with rubrics |
| GitHub Workflow Guide | `dev/agent_a/GitHub_Workflow_Guide.md` | **Ready** - Full PR submission workflow |

#### Agent B Content Available

| Item | Location | Status |
|------|----------|--------|
| M1 Objects README | `dev/agent_b/m1-objects/README.md` | **Draft** - Conceptual notes only |
| AlgoCratic README (Course Philosophy) | `dev/agent_b/algocratic/README.md` | **Ready** - "Bloom's Starts with CREATE" framing |
| AI Collaboration Guide | `dev/agent_b/algocratic/ai-collab.md` | **Ready** - Detailed AI usage patterns |

#### Gaps to Fill

- [ ] Complete M1 Objects assignment specification (similar quality to M2 spec)
- [ ] CitizenRecord class starter code (C++ and Python)
- [ ] M1 lab with testing requirements

---

### M02: Algorithm Analysis and Recursion

**Consolidates:** Agent A M3 (Algorithm Analysis) + M4 (Recursion)

#### Agent A Content Available

| Item | Description | Status |
|------|-------------|--------|
| M3 Concept (from outline) | Big O, time/space complexity, benchmarking | **Outline only** |
| M4 Concept (from outline) | Base cases, recursion, call stack, AlgoCratic "Approval Chain" | **Outline only** |

#### Agent B Content Available

| Item | Location | Status |
|------|----------|--------|
| None directly available | - | - |

#### Gaps to Fill

- [ ] M3 Assignment Spec (benchmark suite comparing algorithms)
- [ ] M4 Assignment Spec (recursive approval chain or file system walker)
- [ ] Starter code for both modules
- [ ] Visualization tools for recursion/call stack

---

### M03: Arrays and Sorting

**Consolidates:** Agent A M5 (Arrays and Sorting - 2 weeks)

#### Agent A Content Available

| Item | Description | Status |
|------|-------------|--------|
| M5 Concept (from outline) | Selection/Insertion/Merge sort, stability, benchmarks | **Outline only** |

#### Agent B Content Available

| Item | Location | Status |
|------|----------|--------|
| Selection Sort (C++) | `dev/agent_b/m3-sorting/m3t1_norris/main.cpp` | **Ready** - Working implementation |
| Selection Sort (Python) | `dev/agent_b/m3-sorting/m3t1_py_norris/m3t1_norris.py` | **Ready** - Working implementation |
| Sorting Lab 2 (C++) | `dev/agent_b/m3-sorting/m3lab2/main.cpp` | **Ready** - Extended sorting exercise |
| Sorting Lab 2 (Python) | `dev/agent_b/m3-sorting/m3lab2/m3lab2.py` | **Ready** - Extended sorting exercise |
| Additional sorting (C++) | `dev/agent_b/m3-sorting/m3t2/main.cpp` | **Ready** - Additional algorithms |

#### Assessment

This module has **good code coverage** but lacks formal assignment specifications with rubrics.

#### Gaps to Fill

- [ ] M3 Assignment Spec document with rubrics
- [ ] Merge Sort implementations (both languages)
- [ ] Performance comparison/benchmark template

---

### M04: Linear Structures - Stacks, Queues, Lists

**Consolidates:** Agent A M6 (Stacks/Queues) + M7 (Linked Lists)

#### Agent A Content Available

| Item | File | Status |
|------|------|--------|
| M6 Stacks/Queues Assignment | `dev/agent_a/M6_StacksQueues_Assignment.md` | **Ready** - Complete spec with rubrics, AlgoCratic framing |

#### Agent B Content Available

| Item | Location | Status |
|------|----------|--------|
| Singly Linked List (Python) | `dev/agent_b/m4-lists/m4t1_py/LinkedList.py` | **Ready** - append, prepend, insert_after, remove_after |
| Node class (Python) | `dev/agent_b/m4-lists/m4t1_py/Node.py` | **Ready** |
| Linked List main (Python) | `dev/agent_b/m4-lists/m4t1_py/main.py` | **Ready** |
| Linked List (C++) warmup | `dev/agent_b/m4-lists/m4t1/warmup.cpp` | **Ready** |
| Linked List (C++) tutorial | `dev/agent_b/m4-lists/m4t1_cpp/main.cpp` | **Ready** |
| Template-based LL (C++) | `dev/agent_b/m4-lists/m4t2_cpp/templates-singlylinked/main.cpp` | **Ready** |
| ZyBooks-style LL (Python) | `dev/agent_b/m4-lists/m4t2_from_zy/python/` | **Ready** - Complete package |
| ZyBooks-style LL (C++) | `dev/agent_b/m4-lists/m4t2_from_zy/cpp/main.cpp` | **Ready** |
| Video Game Shop HW | `dev/agent_b/m4-lists/m4hw1/README.md` | **Draft** - Assignment concept defined |
| Visualization notes | `dev/agent_b/m4-lists/visualize.md` | **Reference** - Links to student artifacts |
| Structure Selection Guide | `dev/agent_b/algocratic/stucture-selection.md` | **Ready** - Stack vs Queue vs BST decision matrix |
| Lab exercise | `dev/agent_b/m4-lists/m4lab1/main.cpp` | **Ready** |

#### Assessment

**Strongest module** - Excellent code coverage in both languages, good assignment spec for Stacks/Queues. The linked list homework needs formal specification.

#### Gaps to Fill

- [ ] M7 Linked Lists Assignment Spec (formalize video game shop HW)
- [ ] Stack/Queue implementations need to be extracted to standalone files

---

### M05: Hashing and Hash Tables

**Consolidates:** Agent A M8 (Hashing)

#### Agent A Content Available

| Item | Description | Status |
|------|-------------|--------|
| M8 Concept (from outline) | Hash functions, collision resolution, AlgoCratic "Citizen Lookup" | **Outline only** |

#### Agent B Content Available

| Item | Location | Status |
|------|----------|--------|
| HashTable base class (Python) | `dev/agent_b/m5-hashing/m5t_py/HashTable.py` | **Skeleton** - Interface only, no implementation |
| ChainingHashTable (Python) | `dev/agent_b/m5-hashing/m5t_py/ChainingHashTable.py` | **Ready** - Working chaining implementation |
| Hash Table main (Python) | `dev/agent_b/m5-hashing/m5t_py/main.py` | **Ready** |
| Password Hashing Demo 1 | `dev/agent_b/m5-hashing/hashing_and_salting_example/passwords_1-no_hashing.py` | **Ready** - Educational progression |
| Password Hashing Demo 2 | `dev/agent_b/m5-hashing/hashing_and_salting_example/passwords_2-hashing.py` | **Ready** |
| Password Hashing Demo 3 | `dev/agent_b/m5-hashing/hashing_and_salting_example/passwords_3-hash_and_salt.py` | **Ready** |
| Lab (Python) | `dev/agent_b/m5-hashing/m5lab/m5lab.py` | **Ready** |
| Lab (C++ unhashed) | `dev/agent_b/m5-hashing/m5lab/m5lab_unhashed.cpp` | **Ready** |
| Lab (C++ classes) | `dev/agent_b/m5-hashing/m5lab/m5lab_cpp_classes/main.cpp` | **Ready** |
| Lab (C++ final) | `dev/agent_b/m5-hashing/m5lab/m5lab_cpp_final/main.cpp` | **Ready** |

#### Assessment

**Good code coverage** with excellent real-world application (password hashing progression). Needs formal assignment specification.

#### Gaps to Fill

- [ ] M5 Hashing Assignment Spec with rubrics
- [ ] Open addressing implementation example
- [ ] Load factor analysis exercise

---

### M06: Trees and Binary Search Trees

**Consolidates:** Agent A M9 (Trees/BST) + M10 (Heaps) + M11 (Balanced Trees)

#### Agent A Content Available

| Item | Description | Status |
|------|-------------|--------|
| M9 Concept (from outline) | Tree terminology, BST insert/search/delete, traversals | **Outline only** |
| M10 Concept (from outline) | Heap property, priority queue, heapsort | **Outline only** |
| M11 Concept (from outline) | Balance visualization, AVL/Red-Black conceptual | **Outline only** |

#### Agent B Content Available

| Item | Location | Status |
|------|----------|--------|
| BinarySearchTree (Python) | `dev/agent_b/m6-trees/samples-6-12/py/BinarySearchTree.py` | **Ready** - Full insert/search/remove |
| Node (Python) | `dev/agent_b/m6-trees/samples-6-12/py/Node.py` | **Ready** |
| TreePrint (Python) | `dev/agent_b/m6-trees/samples-6-12/py/TreePrint.py` | **Ready** - Pretty print utility |
| BST Main (Python) | `dev/agent_b/m6-trees/samples-6-12/py/main.py` | **Ready** |
| BinarySearchTree.h (C++) | `dev/agent_b/m6-trees/samples-6-12/cpp/BinarySearchTree.h` | **Ready** |
| BSTPrint.h (C++) | `dev/agent_b/m6-trees/samples-6-12/cpp/BSTPrint.h` | **Ready** |
| BST Main (C++) | `dev/agent_b/m6-trees/samples-6-12/cpp/main.cpp` | **Ready** |
| Runway Reservation (Concept) | `dev/agent_b/m6-trees/RRS.md` | **Ready** - MIT 6.006 motivated BST application |
| Runway Reservation (Python) | `dev/agent_b/m6-trees/RunwayReservation/py/` | **Ready** - Complete implementation |
| Runway Reservation (C++) | `dev/agent_b/m6-trees/RunwayReservation/cpp/` | **Ready** - Complete implementation |
| BSP Discussion | `dev/agent_b/m6-trees/bsp-discussion/` | **Reference** - Advanced application (raycasting) |
| Streamlit Tree Visualizer | `dev/agent_b/visualization/trees_streamlit.py` | **Ready** - Interactive BST/BT visualization |

#### Assessment

**Excellent coverage** for BST. The Runway Reservation System is a standout pedagogical example. Heaps and balanced trees have no implementation.

#### Gaps to Fill

- [ ] M6 Trees Assignment Spec with rubrics
- [ ] Heap/Priority Queue implementation (both languages)
- [ ] Heapsort implementation
- [ ] Balanced tree visualization (as specified in agent_a outline)

---

### M07: Graphs and Graph Algorithms

**Consolidates:** Agent A M12 (Graphs Intro) + M13 (Graph Algorithms)

#### Agent A Content Available

| Item | Description | Status |
|------|-------------|--------|
| M12 Concept (from outline) | Vertices, edges, adjacency list/matrix | **Outline only** |
| M13 Concept (from outline) | BFS, DFS, shortest path (Dijkstra overview) | **Outline only** |

#### Agent B Content Available

| Item | Location | Status |
|------|----------|--------|
| Graphs conceptual notes | `dev/agent_b/m7-graphs/graphs.md` | **Draft** - Adjacency matrix vs list explanation |
| Sample questions | `dev/agent_b/m7-graphs/sample_questions.md` | **Draft** - ChatGPT-generated assignment ideas with rubrics |

#### Assessment

**Weakest module** - Only conceptual notes exist, no working implementations.

#### Gaps to Fill

- [ ] M7 Graphs Assignment Spec with rubrics
- [ ] Graph class implementation (Python)
- [ ] Graph class implementation (C++)
- [ ] BFS implementation
- [ ] DFS implementation
- [ ] Shortest path demonstration
- [ ] AlgoCratic "Network Surveillance" or "Supply Chain" themed assignment

---

### M08: Integration and Final Project

**Consolidates:** Agent A M14-M16 (Final Project)

#### Agent A Content Available

| Item | Description | Status |
|------|-------------|--------|
| Final Project Concept (from outline) | Student choice OR AlgoCratic Capstone, 10-min presentation | **Outline only** |

#### Agent B Content Available

| Item | Location | Status |
|------|----------|--------|
| requirements.txt | `dev/agent_b/m8-projects/requirements.txt` | **Ready** - Python environment for visualizations |

#### Assessment

The requirements.txt suggests infrastructure for Jupyter/visualization-based projects but no actual project specifications exist.

#### Gaps to Fill

- [ ] Final Project Specification document
- [ ] AlgoCratic Capstone detailed requirements
- [ ] Presentation rubric
- [ ] Sample project repository structure
- [ ] Grading criteria for multi-structure integration

---

## Part 3: Cross-Cutting Resources

### Available Across All Modules

| Resource | Location | Status |
|----------|----------|--------|
| GitHub Workflow Guide | `dev/agent_a/GitHub_Workflow_Guide.md` | **Ready** |
| AI Collaboration Guide | `dev/agent_b/algocratic/ai-collab.md` | **Ready** |
| Structure Selection Guide | `dev/agent_b/algocratic/stucture-selection.md` | **Ready** |
| AlgoCratic Course Philosophy | `dev/agent_b/algocratic/README.md` | **Ready** |
| Streamlit Tree Visualizer | `dev/agent_b/visualization/trees_streamlit.py` | **Ready** |

### AlgoCratic Department Mapping

From agent_a outline, thematic departments for each module:

| CDTS Module | AlgoCratic Department |
|-------------|----------------------|
| M01 | Dept. of Citizen Records + Dept. of Employee Development |
| M02 | Dept. of Efficiency Metrics + Dept. of Bureaucratic Approval |
| M03 | Dept. of Citizen Classification |
| M04 | Dept. of Task Processing + Dept. of Personnel Management |
| M05 | Dept. of Rapid Lookup Services |
| M06 | Dept. of Organizational Hierarchy + Dept. of Priority Services |
| M07 | Dept. of Network Surveillance |
| M08 | The Algorithm's Grand Design |

---

## Part 4: Priority Gap Analysis

### Critical Gaps (High Priority)

| Gap | Impact | CDTS Module |
|-----|--------|-------------|
| M7 Graph implementations missing | Cannot teach graphs without code | M07 |
| M3/M4 Assignment Specs missing | No rubrics for analysis/recursion | M02 |
| Heap implementation missing | Incomplete tree coverage | M06 |
| Final Project Spec missing | No capstone definition | M08 |

### Important Gaps (Medium Priority)

| Gap | Impact | CDTS Module |
|-----|--------|-------------|
| M1 Objects Assignment Spec | Incomplete foundations | M01 |
| M5 Hashing Assignment Spec | No rubrics for hashing | M05 |
| M6 Trees Assignment Spec | No rubrics for trees | M06 |
| Merge Sort implementation | Incomplete sorting coverage | M03 |

### Nice-to-Have Gaps (Lower Priority)

| Gap | Impact | CDTS Module |
|-----|--------|-------------|
| Balanced tree visualization | Conceptual only per spec | M06 |
| Recursion visualization tool | Enhancement | M02 |
| Additional AlgoCratic theming | Consistency | All |

---

## Part 5: Content Status Summary

### By CDTS Module

| Module | Assignment Spec | Code (Python) | Code (C++) | Rubrics | Status |
|--------|----------------|---------------|------------|---------|--------|
| M01 | Partial (M2 only) | None | None | Partial | Needs Work |
| M02 | None | None | None | None | Needs Work |
| M03 | None | Ready | Ready | None | Needs Spec |
| M04 | Ready (M6) | Ready | Ready | Ready | Near Complete |
| M05 | None | Ready | Ready | None | Needs Spec |
| M06 | None | Ready | Ready | None | Needs Spec |
| M07 | None | None | None | None | Critical Gap |
| M08 | None | None | None | None | Needs Work |

### Legend

- **Ready**: Content exists and is usable with minimal changes
- **Draft**: Content exists but needs refinement
- **Skeleton**: Structure exists but implementation incomplete
- **None**: Content does not exist

---

## Part 6: Recommended Development Sequence

Based on dependencies and critical gaps:

### Phase 1: Critical Infrastructure (Weeks 1-2)

1. Create M07 Graph implementations (blocks entire module)
2. Create M08 Final Project Specification
3. Create M02 Assignment Specs (Analysis + Recursion)

### Phase 2: Assignment Specifications (Weeks 3-4)

4. Create M01 Objects Assignment Spec
5. Create M03 Sorting Assignment Spec
6. Create M05 Hashing Assignment Spec
7. Create M06 Trees Assignment Spec

### Phase 3: Implementation Gaps (Weeks 5-6)

8. Add Heap/Priority Queue implementations
9. Add Merge Sort implementations
10. Complete M1 starter code (CitizenRecord)
11. Add Heapsort implementation

### Phase 4: Polish (Weeks 7-8)

12. Standardize AlgoCratic theming across all specs
13. Add visualizations where missing
14. Create course-manifest.yaml for CDTS tracking
15. Quality review and testing

---

## Appendix A: File Inventory

### dev/agent_a/ (4 files)

```
CSC249_Course_Outline.md      - 16-module course design (Ready)
M2_Assignment_Spec.md         - AI Collaboration assignment (Ready)
M6_StacksQueues_Assignment.md - Stacks/Queues assignment (Ready)
GitHub_Workflow_Guide.md      - PR submission workflow (Ready)
```

### dev/agent_b/ (54+ files across 8 directories)

```
algocratic/
  README.md                   - Course philosophy (Ready)
  ai-collab.md                - AI usage guide (Ready)
  stucture-selection.md       - Data structure decision matrix (Ready)

m1-objects/
  README.md                   - Conceptual notes (Draft)

m3-sorting/
  m3t1_norris/main.cpp        - Selection sort C++ (Ready)
  m3t1_py_norris/m3t1_norris.py - Selection sort Python (Ready)
  m3lab2/main.cpp             - Sorting lab C++ (Ready)
  m3lab2/m3lab2.py            - Sorting lab Python (Ready)
  m3t2/main.cpp               - Additional sorting (Ready)

m4-lists/
  m4t1_py/LinkedList.py       - Singly linked list (Ready)
  m4t1_py/Node.py             - Node class (Ready)
  m4t1_py/main.py             - Demo driver (Ready)
  m4t1/warmup.cpp             - C++ warmup (Ready)
  m4t1_cpp/main.cpp           - C++ tutorial (Ready)
  m4t2_cpp/                   - Template-based LL (Ready)
  m4t2_from_zy/               - ZyBooks-style LL (Ready)
  m4hw1/README.md             - Video game shop HW (Draft)
  m4lab1/main.cpp             - Lab exercise (Ready)
  visualize.md                - Student artifact links (Reference)

m5-hashing/
  m5t_py/HashTable.py         - Base class skeleton (Skeleton)
  m5t_py/ChainingHashTable.py - Chaining implementation (Ready)
  m5t_py/main.py              - Demo driver (Ready)
  hashing_and_salting_example/ - Password hashing progression (Ready)
  m5lab/                      - Lab exercises (Ready)

m6-trees/
  samples-6-12/py/            - BST Python implementation (Ready)
  samples-6-12/cpp/           - BST C++ implementation (Ready)
  RRS.md                      - Runway Reservation concept (Ready)
  RunwayReservation/          - Full RRS implementations (Ready)
  bsp-discussion/             - Advanced BSP reference (Reference)

m7-graphs/
  graphs.md                   - Adjacency concepts (Draft)
  sample_questions.md         - Assignment ideas (Draft)

m8-projects/
  requirements.txt            - Python environment (Ready)

visualization/
  trees_streamlit.py          - Interactive tree viz (Ready)
```

---

## Appendix B: CDTS Manifest Template

When content is finalized, create `course-manifest.yaml` at repository root:

```yaml
manifest_version: "0.1"
last_updated: "2025-XX-XX"

course:
  id: "CSC-249"
  name: "Data Structures and Algorithms"
  credits: 3
  description: |
    Data structures and algorithms with dual-language instruction
    (C++ and Python). AI-assisted development with professional
    GitHub workflow.
  prerequisites:
    - "CSC-134"
  repository: "course-csc249-template"

modules:
  - id: "M01"
    name: "Foundations: OOP and AI Collaboration"
    weeks: [1, 2]
    status: "draft"
    deliverables: []

  # ... (continue for all 8 modules)

progress:
  total_deliverables: 0
  complete: 0
  percentage: 0
```

---

*Document generated for CSC 249 course development tracking.*
*Last updated: 2026-01-01*
