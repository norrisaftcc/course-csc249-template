# CSC 249: Runestone Academy Mapping Guide
## Modules 1-4 (Weeks 1-8)

**Document Purpose**: Map CSC 249 modules to Runestone Academy's *Problem Solving with Algorithms and Data Structures* (C++ and Python editions). Identifies where Runestone is a strong fit, where editions diverge significantly, and where custom/supplemental materials are needed.

**Philosophy**: Runestone serves as a quality reference, not the primary text. Students choose a primary language but can use AI-assisted translation when a concept doesn't click.

---

## Quick Reference: Runestone URLs

- **C++ Edition**: https://runestone.academy/ns/books/published/cppds/index.html
- **Python Edition (3rd ed)**: https://runestone.academy/ns/books/published/pythonds3/index.html

---

## Module 1: Foundations – OOP and AI Collaboration
**Weeks 1-2**

### Course Objectives
- Encapsulation, ADTs, class design
- AI collaboration workflow
- Version control / PR workflows

### Runestone Mapping

| Topic | C++ Edition | Python Edition | Fit |
|-------|-------------|----------------|-----|
| What is CS / Programming | 1.3-1.4 | 1.3-1.4 | ✅ Identical |
| Why Data Structures & ADTs | 1.5 | 1.5 | ✅ Identical |
| Why Algorithms | 1.6 | 1.6 | ✅ Identical |
| Language Review | 1.7-1.9 (C++ specific) | 1.7-1.12 (Python specific) | ⚠️ Divergent |
| OOP / Defining Classes | 1.12-1.13 | 1.13-1.14 | ⚠️ Divergent |
| AI Collaboration | — | — | ❌ Not covered |
| Version Control | — | — | ❌ Not covered |

### Assessment

**Runestone Fit**: PARTIAL

Sections 1.3-1.6 are nearly identical and provide solid motivation for studying data structures. These are worth assigning as shared reading regardless of language track.

**Divergence**: The OOP sections (1.12+ in both editions) teach *syntax* for defining classes but not *design philosophy*. C++ covers inheritance, pointers-to-objects. Python covers `__str__`, operator overloading. Students reading both will see different emphases.

**Gap**: Runestone has no content on:
- AI-assisted development workflows
- How to prompt effectively for code understanding
- Version control, GitHub, pull requests

### Recommendation

| Content | Source |
|---------|--------|
| "Why study DS/algorithms" motivation | Runestone 1.3-1.6 (either edition) |
| Language-specific OOP syntax | Runestone 1.12+ (student's primary language only) |
| ADT design philosophy | **Custom material needed** |
| AI collaboration workflow | **Custom material needed** |
| Git/GitHub basics | **Custom material needed** (or external resource) |

### Suggested Custom Material: M01 Supplement

A short document covering:
1. ADTs as contracts (interface vs implementation separation)
2. The "implement first, understand why second" philosophy
3. AI collaboration patterns: when to ask for explanation vs. code vs. debugging help
4. Prompt documentation requirements (saving prompts.txt)

---

## Module 2: Algorithm Analysis and Recursion
**Weeks 3-4**

### Course Objectives
- Big O notation
- Benchmarking
- Recursive thinking

### Runestone Mapping

| Topic | C++ Edition | Python Edition | Fit |
|-------|-------------|----------------|-----|
| What is Algorithm Analysis | 2.2 | 2.2 | ✅ Identical concepts |
| Big O Notation | 2.3 | 2.3 | ✅ Identical |
| Anagram Detection Example | 2.4 | 2.4 | ✅ Good (code differs) |
| Performance of Collections | 2.5-2.8 | 2.5-2.7 | ⚠️ Divergent |
| What is Recursion | 5.2 | 4.2 | ✅ Identical concepts |
| Three Laws of Recursion | 5.4 | 4.4 | ✅ Identical |
| Stack Frames / Call Stack | 5.6 | 4.6 | ✅ Good |
| Visualizing Recursion | 5.7-5.8 | 4.7-4.8 | ⚠️ Uses turtle graphics |
| Tower of Hanoi | 5.10 | 4.10 | ✅ Classic example |
| Dynamic Programming | 5.12 | 4.12 | ⚠️ May be too advanced for week 4 |

### Assessment

**Runestone Fit**: GOOD (with curation)

Big O and recursion fundamentals are well-covered in both editions. The conceptual content is nearly identical; only code examples differ.

**Divergence**: 
- Performance sections (2.5-2.8) analyze language-specific containers:
  - C++: arrays, vectors, strings, hash tables (unordered_map)
  - Python: lists, dictionaries
- This is actually *useful* divergence—students see how the same ADT has different performance characteristics in different implementations.

**Potential Issue**: Runestone's recursion chapter includes turtle graphics visualization (drawing trees, Sierpinski triangles). This is pedagogically interesting but may feel tangential if you're focused on "recursion as problem-solving tool" rather than "recursion as art project."

**Sequencing Note**: Your manifest places recursion in M02 (weeks 3-4). Runestone places recursion after linear structures (Chapter 5 in cppds). This is fine—recursion doesn't depend on stacks/queues conceptually, though Runestone does use "stack frames" as a recursion explanation, which creates a nice forward reference.

### Recommendation

| Content | Source |
|---------|--------|
| Big O fundamentals (2.2-2.4) | Runestone (either edition) |
| Container performance | Runestone (student's primary language) |
| Recursion intro (5.2-5.6 / 4.2-4.6) | Runestone (either edition) |
| Tower of Hanoi | Runestone (either edition) |
| Visualization (turtle graphics) | OPTIONAL – skip if time-constrained |
| Dynamic Programming | DEFER to later or skip – too advanced for week 4 |
| Benchmarking (timing your own code) | **Light supplement needed** |

### Suggested Custom Material: M02 Supplement

Runestone's benchmarking is conceptual ("here's why list.append() is O(1)"). If you want students to *actually benchmark* their own code:
- Python: `timeit` module quick reference
- C++: `<chrono>` quick reference
- Assignment: "Time your recursive vs iterative factorial at n=10, 100, 1000"

---

## Module 3: Arrays and Sorting
**Weeks 5-6**

### Course Objectives
- Selection sort, insertion sort, merge sort
- Complexity analysis of sorting algorithms

### Runestone Mapping

| Topic | C++ Edition | Python Edition | Fit |
|-------|-------------|----------------|-----|
| Sequential Search | 6.2 | 5.3 | ✅ Good |
| Binary Search | 6.3 | 5.4 | ✅ Good |
| Bubble Sort | 7.3 | 5.7 | ✅ Good |
| Selection Sort | 7.4 | 5.8 | ✅ Good |
| Insertion Sort | 7.5 | 5.9 | ✅ Good |
| Shell Sort | 7.6 | 5.10 | ⚠️ Optional |
| Merge Sort | 7.7 | 5.11 | ✅ Good |
| Quick Sort | 7.8 | 5.12 | ⚠️ May defer |

### Assessment

**Runestone Fit**: GOOD

Sorting algorithms are a strength of both Runestone editions. The explanations are clear, visualizations are included, and complexity analysis is integrated.

**Divergence**: Minimal conceptual divergence. Code syntax differs but algorithms are identical. This is a module where "read in your language, optionally peek at the other" works well.

**Chapter Organization Difference**:
- C++ separates Search/Hash (Ch 6) from Sort (Ch 7)
- Python combines into one chapter (Ch 5: Searching and Sorting)

This shouldn't affect students much—just different section numbers.

**Scope Decision**: Your manifest lists "selection, insertion, merge sort." Runestone also covers bubble, shell, and quicksort. You may want to:
- Assign bubble sort as a "warm-up" (easiest to understand)
- Cover selection, insertion, merge as core
- Make quicksort optional/bonus
- Skip shell sort (rarely used in practice)

### Recommendation

| Content | Source |
|---------|--------|
| Sequential & Binary Search | Runestone 6.2-6.3 (C++) / 5.3-5.4 (Python) |
| Bubble Sort (warm-up) | Runestone 7.3 (C++) / 5.7 (Python) |
| Selection Sort | Runestone 7.4 (C++) / 5.8 (Python) |
| Insertion Sort | Runestone 7.5 (C++) / 5.9 (Python) |
| Merge Sort | Runestone 7.7 (C++) / 5.11 (Python) |
| Quick Sort | OPTIONAL – Runestone 7.8 / 5.12 |
| Visualization | VisuAlgo sorting module (supplement) |

### Suggested Assignment Pattern

This module is a strong candidate for the "implement in primary language, AI-translate to compare" pattern:

> **Lab**: Implement merge sort in your primary language. Then use Claude to show you merge sort in the other language. In your reflection, identify one thing that's clearer in each language's implementation.

This keeps the deliverable in one language but builds the translation skill.

---

## Module 4: Linear Structures – Stacks, Queues, Lists
**Weeks 7-8**

### Course Objectives
- LIFO/FIFO structures
- Node-based linked lists
- ADT design

### Runestone Mapping

| Topic | C++ Edition | Python Edition | Fit |
|-------|-------------|----------------|-----|
| What are Linear Structures | 3.2 | 3.2 | ✅ Identical |
| Stack ADT | 3.3-3.4 | 3.3-3.4 | ✅ Identical |
| Stack Implementation | 3.5 | 3.5 | ⚠️ Divergent |
| Balanced Parentheses | 3.6-3.7 | 3.6-3.7 | ✅ Good |
| Decimal to Binary | 3.8 | 3.8 | ✅ Good |
| Infix/Prefix/Postfix | 3.9 | 3.9 | ✅ Good (meaty) |
| Queue ADT | 3.10-3.11 | 3.10-3.11 | ✅ Identical |
| Queue Implementation | 3.12 | 3.12 | ⚠️ Divergent |
| Hot Potato Simulation | 3.13 | 3.13 | ✅ Good |
| Printing Queue Simulation | 3.14 | 3.14 | ✅ Good |
| Deque | 3.15-3.17 | 3.15-3.17 | ✅ Good |
| Linked Lists | 4.1-4.8 (separate chapter) | 3.18-3.23 (same chapter) | ⚠️ Structural divergence |

### Assessment

**Runestone Fit**: GOOD (with awareness of structural difference)

This is the module where the two editions diverge structurally:
- **C++**: Chapter 3 = array-based (stack, queue, deque), Chapter 4 = node-based (linked lists)
- **Python**: Chapter 3 = all linear structures together

**Conceptual content is strong in both**. The balanced parentheses, infix-to-postfix, and simulation examples are excellent applications.

**Implementation Divergence**:
- Python stack uses `list.append()` and `list.pop()` — trivial
- C++ stack in Runestone uses `vector` — also trivial
- Neither edition implements a *node-based* stack (they use array-backed structures)
- Linked list implementations differ significantly:
  - Python: uses Python objects with `self.next` references
  - C++: uses pointers, `Node*`, manual memory considerations

This is where the dual-language approach gets interesting. A student who "gets" linked lists in Python may struggle with C++ pointers, and vice versa. This is a good place to encourage cross-language exploration.

### Recommendation

| Content | Source |
|---------|--------|
| Linear structures intro, Stack/Queue ADT | Runestone 3.2-3.4, 3.10-3.11 (either) |
| Stack applications (parens, postfix) | Runestone 3.6-3.9 (either) |
| Queue simulations | Runestone 3.13-3.14 (either) |
| Deque | Runestone 3.15-3.17 (either) |
| Linked List concepts | Runestone 4.1-4.3 (C++) / 3.18-3.20 (Python) |
| Linked List implementation | **Consider custom material** or Runestone with heavy AI support |

### Divergence Alert: Linked Lists

This is a topic where "AI-translate to understand" is genuinely valuable. Suggest to students:

> If you're in the C++ track and pointers feel confusing, ask Claude: "Show me how this linked list insert operation would look in Python, then explain what the C++ pointers are doing."

> If you're in the Python track, ask Claude: "Why does C++ need pointers for this? What problem do they solve that Python handles automatically?"

### Your Existing Materials

You already have:
- `module-04/tutorials/stacks.md` (complete)
- `module-04/rubrics/stacks-queues-rubric.yaml` (complete)
- Labs planned: undo system, request queue, linked list

This suggests M04 is your most developed module. Runestone can supplement but your custom materials may already be stronger for your pedagogical goals.

---

## Summary: Module 1-4 Mapping

| Module | Runestone Fit | Primary Gaps | Recommendation |
|--------|---------------|--------------|----------------|
| M01 | Partial | AI workflow, Git, ADT design philosophy | Heavy custom supplement |
| M02 | Good | Practical benchmarking | Light supplement |
| M03 | Good | None significant | Runestone works well |
| M04 | Good | Linked list pointer/reference differences | Custom or AI-bridge |

## Cross-Language Pattern Summary

For each module, the pattern is:

1. **Shared reading**: Conceptual sections (1.3-1.6, Big O intro, ADT definitions)
2. **Language-specific reading**: Implementation sections in primary language
3. **AI bridge**: "If this doesn't click, here's a prompt to see it in the other language"
4. **Deliverables**: In one language, unless specifically noted

---

## Appendix: Section Number Quick Reference

### M02 Reading Assignment Example

**C++ Track**:
- Big O: cppds 2.2-2.4
- C++ container performance: cppds 2.5-2.8
- Recursion: cppds 5.2-5.6, 5.10

**Python Track**:
- Big O: pythonds3 2.2-2.4
- Python container performance: pythonds3 2.5-2.7
- Recursion: pythonds3 4.2-4.6, 4.10

**If stuck on recursion**:
> "Claude, explain how the call stack works in [other language] for a recursive factorial function. Compare it to how [my language] handles it."

---

## Next Steps

1. Review this mapping against actual Runestone content (spot-check a few sections)
2. Decide which sections to formally assign vs. recommend
3. Draft M01 supplement (AI workflow, ADT philosophy)
4. Test the "AI bridge" prompt pattern with a student or TA
5. Build M02 benchmarking mini-assignment

---

*Document version: Draft 1*
*Created: 2026-01-05*
