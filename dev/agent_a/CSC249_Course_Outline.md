# CSC 249: Data Structures and Algorithms
## Course Outline — 16-Week Structure

---

## Course Philosophy

**"Bloom's Taxonomy Starts with Create"**

Traditional CS education: Learn theory → See examples → Eventually build something.

This course: **Build something → Understand why it works → Analyze tradeoffs.**

Students learn by making things. AI assistance is mandatory — not as a crutch, but as a professional tool they must learn to wield effectively. Dual-language instruction (C++ and Python) reflects workforce reality.

---

## Course Information

| | |
|---|---|
| **Course** | CSC 249: Data Structures and Algorithms |
| **Languages** | C++ and Python (dual-language) |
| **AI Policy** | Mandatory use with documentation |
| **Submission** | GitHub Pull Requests |
| **Prerequisites** | CSC 134 or equivalent (intro programming) |

---

## Module Overview

| Phase | Modules | Weeks | Focus |
|-------|---------|-------|-------|
| Foundation | M1–M4 | 1–4 | OOP, AI skills, analysis, recursion |
| Linear Structures | M5–M8 | 5–8 | Arrays, stacks, queues, lists, hashing |
| Hierarchical & Network | M9–M13 | 9–13 | Trees, heaps, graphs |
| Integration | M14–M16 | 14–16 | Final project and presentations |

---

## Phase 1: Foundation (Weeks 1–4)

### Module 1: Objects and Classes
**Week 1**

| Component | Description |
|-----------|-------------|
| **Concept** | Encapsulation, Abstract Data Types, class design |
| **Languages** | Student choice: C++ or Python |
| **Build** | `CitizenRecord` class with attributes and methods |
| **AI Role** | Light assistance — focus on fundamentals |
| **Deliverable** | PR with working class implementation |

**Learning Objectives:**
- Design a class with appropriate attributes and methods
- Understand encapsulation and data hiding
- Write constructors and basic methods
- Test code before submission

---

### Module 2: AI Collaboration & Data Structures Survey
**Week 2**

| Component | Description |
|-----------|-------------|
| **Concept** | Effective AI prompting, DS vocabulary, code translation |
| **Languages** | Both C++ and Python |
| **Build** | Data Structures Field Guide + translated code |
| **AI Role** | Primary focus — learn to prompt and verify |
| **Deliverable** | 2 PRs (Field Guide + Translation) |

**Learning Objectives:**
- Write effective prompts that get useful responses
- Verify and correct AI-generated information
- Translate code between C++ and Python
- Document AI collaboration honestly

**Part A:** Interview AI about 8 core data structures, synthesize into personal field guide
**Part B:** Translate M1 code to the other language, document what AI got wrong

---

### Module 3: Algorithm Analysis
**Week 3**

| Component | Description |
|-----------|-------------|
| **Concept** | Big O notation, time/space complexity, empirical measurement |
| **Languages** | Both (comparison) |
| **Build** | Benchmark suite comparing algorithm implementations |
| **AI Role** | Explain Big O — student verifies empirically |
| **Deliverable** | PR with benchmarks and analysis report |

**Learning Objectives:**
- Understand Big O notation (O(1), O(n), O(n²), O(log n))
- Measure actual runtime performance
- Compare theoretical vs. empirical complexity
- Recognize common complexity patterns

**Activity:** Implement the same algorithm (e.g., search) multiple ways, time them with increasing input sizes, graph the results

---

### Module 4: Recursion
**Week 4**

| Component | Description |
|-----------|-------------|
| **Concept** | Base cases, recursive calls, call stack, stack overflow |
| **Languages** | Student choice |
| **Build** | Recursive "approval chain" or file system walker |
| **AI Role** | Help debug stack traces and visualize recursion |
| **Deliverable** | PR with recursive solution + iterative comparison |

**Learning Objectives:**
- Identify base cases and recursive cases
- Trace recursive execution manually
- Understand the call stack
- Convert between recursive and iterative solutions

**AlgoCratic Framing:** "Bureaucratic Approval Chain" — a request must be approved by each level of management recursively until it reaches the CEO (base case)

---

## Phase 2: Linear Structures (Weeks 5–8)

### Module 5: Arrays and Sorting
**Weeks 5–6**

| Component | Description |
|-----------|-------------|
| **Concept** | Array operations, comparison sorts, stability |
| **Languages** | Both (implement in one, translate to other) |
| **Build** | Employee records sorter with multiple criteria |
| **AI Role** | Explain algorithms — student implements and benchmarks |
| **Deliverable** | PR with sorting implementations + performance comparison |

**Learning Objectives:**
- Implement selection sort, insertion sort, merge sort
- Understand sorting stability and when it matters
- Analyze sorting algorithm complexity
- Sort by multiple keys/criteria

**Sorting Algorithms Covered:**
- Week 5: Selection Sort, Insertion Sort (O(n²))
- Week 6: Merge Sort, intro to Quick Sort (O(n log n))

---

### Module 6: Stacks and Queues
**Week 7**

| Component | Description |
|-----------|-------------|
| **Concept** | LIFO, FIFO, operations, applications |
| **Languages** | Student choice |
| **Build** | Undo system (stack) + ticket queue (queue) |
| **AI Role** | Standard assistance |
| **Deliverable** | PR with both implementations + demo driver |

**Learning Objectives:**
- Implement stack with push, pop, peek, isEmpty
- Implement queue with enqueue, dequeue, front, isEmpty
- Recognize stack/queue applications in real systems
- Choose appropriate structure for a given problem

**AlgoCratic Framing:** "Task Processing System" — build the department's undo system and citizen request queue

---

### Module 7: Linked Lists
**Week 8**

| Component | Description |
|-----------|-------------|
| **Concept** | Nodes, pointers/references, dynamic memory, traversal |
| **Languages** | C++ (pointers) and Python (references) — compare |
| **Build** | Dynamic roster with insert, delete, search |
| **AI Role** | Help with pointer debugging (C++) |
| **Deliverable** | PR with linked list implementation in both languages |

**Learning Objectives:**
- Understand node-based structures
- Implement singly linked list operations
- Handle edge cases (empty list, single node, head/tail operations)
- Compare array vs. linked list tradeoffs

**Key Operations:** insert (front, back, middle), delete, search, traverse, reverse

---

### Module 8: Hashing
**Week 9**

| Component | Description |
|-----------|-------------|
| **Concept** | Hash functions, collision resolution, load factor |
| **Languages** | Student choice |
| **Build** | Login cache or record lookup system |
| **AI Role** | Explain collision strategies |
| **Deliverable** | PR with hash table implementation + collision analysis |

**Learning Objectives:**
- Understand how hash functions work
- Implement chaining collision resolution
- Understand open addressing (conceptually)
- Analyze hash table performance characteristics

**AlgoCratic Framing:** "Citizen Lookup System" — O(1) access to citizen records by ID

---

## Phase 3: Hierarchical & Network Structures (Weeks 9–13)

### Module 9: Trees and Binary Search Trees
**Weeks 10–11**

| Component | Description |
|-----------|-------------|
| **Concept** | Tree terminology, BST property, traversals |
| **Languages** | Student choice |
| **Build** | Org chart (general tree) + searchable database (BST) |
| **AI Role** | Visualize tree operations |
| **Deliverable** | PR with BST implementation + traversal demos |

**Learning Objectives:**
- Understand tree terminology (root, leaf, height, depth)
- Implement BST insert, search, delete
- Implement inorder, preorder, postorder traversals
- Understand BST performance characteristics

**Week 10:** Tree concepts, BST insert and search
**Week 11:** BST delete, traversals, applications

---

### Module 10: Heaps and Priority Queues
**Week 12**

| Component | Description |
|-----------|-------------|
| **Concept** | Heap property, heapify, priority queue ADT |
| **Languages** | Student choice |
| **Build** | Priority processing system |
| **AI Role** | Standard assistance |
| **Deliverable** | PR with heap implementation + heapsort |

**Learning Objectives:**
- Understand min-heap and max-heap properties
- Implement heap insert and extract operations
- Understand heapify process
- Implement heapsort

**AlgoCratic Framing:** "Citizen Priority Processing" — high-priority requests processed first

---

### Module 11: Balanced Trees (Conceptual)
**Week 13 (first half)**

| Component | Description |
|-----------|-------------|
| **Concept** | Why balance matters, AVL/Red-Black overview |
| **Languages** | N/A — visualization focus |
| **Build** | Streamlit visualization comparing BST vs. balanced |
| **AI Role** | Generate visualizations |
| **Deliverable** | PR with visualization + written analysis |

**Learning Objectives:**
- Understand why unbalanced trees degrade to O(n)
- Recognize AVL and Red-Black trees conceptually
- Use visualization tools to explore tree balance
- Articulate when balanced trees matter

**Note:** Students visualize and analyze — they don't implement AVL rotations from scratch. Focus on understanding, not memorizing rotation cases.

---

### Module 12: Graphs Introduction
**Week 13 (second half) – Week 14**

| Component | Description |
|-----------|-------------|
| **Concept** | Vertices, edges, directed/undirected, representations |
| **Languages** | Student choice |
| **Build** | Social network or dependency graph |
| **AI Role** | Standard assistance |
| **Deliverable** | PR with graph implementation + basic queries |

**Learning Objectives:**
- Understand graph terminology
- Implement adjacency list representation
- Implement adjacency matrix representation
- Add vertices, add edges, find neighbors

---

### Module 13: Graph Algorithms
**Week 14–15**

| Component | Description |
|-----------|-------------|
| **Concept** | BFS, DFS, shortest path |
| **Languages** | Continue from M12 |
| **Build** | Route optimizer or network analyzer |
| **AI Role** | Explain algorithm flow |
| **Deliverable** | PR with traversal implementations + application |

**Learning Objectives:**
- Implement breadth-first search
- Implement depth-first search
- Understand shortest path concepts (Dijkstra's overview)
- Apply graph algorithms to real problems

**AlgoCratic Framing:** "Supply Chain Optimization" or "Network Surveillance System"

---

## Phase 4: Integration (Weeks 14–16)

### Module 14–16: Final Project
**Weeks 15–16**

| Component | Description |
|-----------|-------------|
| **Concept** | Integration, design decisions, presentation |
| **Languages** | Student choice |
| **Build** | Student-selected project OR AlgoCratic capstone |
| **AI Role** | Full collaboration with documentation |
| **Deliverable** | PR with project + presentation |

**Project Options:**

**Option A: Student Choice**
- Propose a project using 2+ data structures
- Must include README with design rationale
- Examples: game inventory system, social network analyzer, file organizer

**Option B: AlgoCratic Capstone**
- "Citizen Management System" integrating multiple structures
- Hash table for lookup, priority queue for processing, graph for relationships
- Prescribed requirements, creative implementation

**Final Presentation:**
- 10-minute demo
- Explain data structure choices
- Show working code
- Answer questions

---

## Assessment Structure

| Component | Weight | Description |
|-----------|--------|-------------|
| Module Assignments | 60% | PRs for each module (roughly 4% each) |
| Participation | 10% | PR reviews, questions, collaboration |
| Final Project | 20% | Capstone implementation |
| Final Presentation | 10% | Demo and explanation |

---

## Weekly Rhythm

| Day | Activity |
|-----|----------|
| **Monday** | New module introduction, concept overview |
| **Wednesday** | Lab work, implementation guidance |
| **Friday** | PR due, peer review begins |

---

## AI Documentation Requirements

Every PR must include:
1. **Which AI tools used** (Claude, ChatGPT, Copilot, etc.)
2. **What you used them for** (explanation, debugging, code generation)
3. **What you corrected** (AI errors you caught and fixed)

This isn't surveillance — it's professional documentation of your workflow.

---

## Resources

**Visualization:**
- VisuAlgo (visualgo.net)
- Python Tutor (pythontutor.com)
- Streamlit for custom visualizations

**Interactive Textbook:**
- Runestone Academy — Problem Solving with Algorithms and Data Structures (C++ and Python editions)

**Video:**
- William Fiset's Data Structures playlist
- MyCodeSchool (C/C++ focus)

**Practice:**
- Codewars
- Exercism
- HackerRank Data Structures track

---

## AlgoCratic Department Guide

For thematic consistency across assignments:

| Module | Department |
|--------|------------|
| M1 Objects | Department of Citizen Records |
| M2 AI Survey | Department of Employee Development |
| M3 Analysis | Department of Efficiency Metrics |
| M4 Recursion | Department of Bureaucratic Approval |
| M5 Sorting | Department of Citizen Classification |
| M6 Stacks/Queues | Department of Task Processing |
| M7 Linked Lists | Department of Personnel Management |
| M8 Hashing | Department of Rapid Lookup Services |
| M9 Trees | Department of Organizational Hierarchy |
| M10 Heaps | Department of Priority Services |
| M11 Balanced Trees | Department of Optimization Research |
| M12–13 Graphs | Department of Network Surveillance |
| M14–16 Final | The Algorithm's Grand Design |

---

*CSC 249 — Data Structures and Algorithms*
*"The Algorithm Appreciates Your Cooperation"*
