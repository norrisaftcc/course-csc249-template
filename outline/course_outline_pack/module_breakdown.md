# CSC 249: Detailed Module Breakdown
## 8 Modules with Progressive Development

**Document Purpose**: Comprehensive module-by-module guide. M01-M04 have full implementation details (immediate development). M05-M08 have structural outlines (to be refined with feedback from early modules).

---

# MODULE 1: Foundations - OOP and AI Collaboration
**Weeks 1-2 | Status: IMMEDIATE DEVELOPMENT**

## Learning Objectives
By the end of M01, students will:
1. Set up GitHub workflow and submit via pull request
2. Implement a simple ADT (Stack or Queue) in their primary language
3. Document AI collaboration in `prompts.txt`
4. Explain encapsulation and why ADTs separate interface from implementation
5. Use AI to translate concepts between C++ and Python

---

## Week 1: Workflows and Foundations

### Day 1: Course Launch
**What Students Build**: Nothing yet (setup day)

**Activities**:
- Course overview: "You'll build first, understand later"
- GitHub account setup + repo fork
- Language choice declaration (C++ or Python primary)
- AI tool selection (Claude, ChatGPT, Copilot)

**Assignment (Due Day 2)**:
- Create first PR with README edit (your name, language choice, AI tool)
- Watch: MyCodeSchool "Intro to Data Structures" (15 min)

---

### Day 2: What is an ADT?
**What Students Build**: Simple "Box" class (stores one value)

**Concept Introduction** (15 min):
- ADT = contract without implementation
- "Black box" analogy: You don't need to know how a microwave works to use it

**Live Coding** (20 min):
```cpp
// C++ version
class Box {
private:
    int value;
public:
    void store(int v) { value = v; }
    int retrieve() { return value; }
};
```

```python
# Python version
class Box:
    def __init__(self):
        self._value = None
    
    def store(self, v):
        self._value = v
    
    def retrieve(self):
        return self._value
```

**Lab Activity** (25 min):
- Implement Box in your language
- Add a `peek()` method (returns value without removing)
- Test with provided test cases

**AI Prompt Template**:
> "I'm implementing a Box class in [language]. It should store one value. Can you explain the difference between private and public members?"

**Homework (Due Week 2, Day 1)**:
- Expand Box to store 5 values (fixed-size array/list)
- Submit via PR with `prompts.txt`

---

### Day 3: Stack ADT - Build Before Theory
**What Students Build**: Stack class (push, pop, peek)

**Concept Introduction** (10 min):
- LIFO visualization (stack of plates)
- Real-world use: browser back button, undo

**Challenge** (30 min):
> "Build a Stack that can push(), pop(), and peek(). Use an array/list internally. Don't look up the algorithm yet—try to figure it out."

**Discussion After** (10 min):
- How did you track the "top"?
- What edge cases did you hit? (empty stack, full stack)
- NOW look at Runestone 3.3-3.4 (see if your solution matches)

**Reflection Question**:
> "Did building it first make the reading easier or harder? Why?"

**Homework (Due Week 2, Day 2)**:
- Implement Stack in your primary language
- Write 5 test cases
- Document 3 AI prompts you used

---

## Week 2: Integration and Translation

### Day 4: Queue ADT - Build Before Theory
**What Students Build**: Queue class (enqueue, dequeue, peek)

**Pattern Repetition**:
Same structure as Stack day:
1. FIFO visualization (grocery store line)
2. 30-minute build challenge (no peeking at solutions)
3. Compare with Runestone 3.10-3.11
4. Discuss: "Why is Queue harder than Stack?" (tracking front AND rear)

**Cross-Language Exploration**:
- Stack in C++ vs Python (pointer differences)
- Memory model discussion

**AI Collaboration Focus**:
> "Show me a Queue implementation in [other language]. What's different about how it tracks the front and rear?"

---

### Day 5: AI as Learning Tool
**What Students Build**: Nothing new (refinement day)

**Workshop Focus**: Effective Prompting
- Bad prompt: "Write me a stack"
- Good prompt: "Explain why a stack needs a 'top' variable"

**Activity** (30 min):
- Pair up: Show your Stack code to partner
- Partner asks: "Explain this line without looking at AI"
- If stuck, craft a prompt together to understand it

**Prepare for M01 Lab**:
- Review PR submission process
- Lab release: "Undo System" (uses stack)

---

### Day 6: M01 Lab Work Session
**M01 LAB: Undo System**

**Scenario**: Text editor with undo functionality (stack of actions)

**Requirements**:
- Implement Stack ADT in primary language
- Support: `type(text)`, `undo()`, `redo()` (uses second stack)
- Handle edge cases (undo with empty history)
- Provide `prompts.txt` with AI conversations

**Rubric** (30 points):
- [10] Stack implementation works
- [8] Undo logic correct
- [7] Edge cases handled
- [5] AI prompts documented

**Extension Challenge** (+5 bonus):
- Implement in BOTH languages
- Explain what's easier/harder in each

---

## M01 Resources

### Zybooks Integration (LIGHT)
- **Chapter 1.3-1.6**: Why study data structures (read for context)
- **Chapter 1.12+**: OOP syntax reference (skim, don't memorize)
- **DO NOT**: Get bogged down in Chapter 1 exercises (skip them)

### Runestone Academy (PRIMARY)
- **Section 3.2**: Linear structures intro (15 min read)
- **Section 3.3-3.4**: Stack ADT (implement alongside reading)
- **Section 3.10-3.11**: Queue ADT (implement alongside reading)

### VisuAlgo Demonstrations
- Stack operations: https://visualgo.net/en/list (LIFO mode)
- Queue operations: https://visualgo.net/en/list (FIFO mode)

### Custom Materials (TO DEVELOP)
- [ ] "ADT Design Philosophy" document (2-3 pages)
- [ ] "Effective AI Prompting for CS" guide
- [ ] Git/PR workflow tutorial with screenshots
- [ ] M01 Lab template and test cases

---

## M01 Assessment Strategy

### What We're Really Testing
- Can students iterate (build, test, fix, repeat)?
- Do they understand the code they submit?
- Are they documenting their learning process?

### Red Flags
- Submits complex code but can't explain basic operations
- No prompts.txt (claimed AI use but no evidence)
- Copied code without modification (obvious from AI style)

### Green Flags
- Code has bugs but prompts show troubleshooting process
- Student can explain: "I tried X, AI suggested Y, I modified it to Z because..."
- PR comments show iteration

---

# MODULE 2: Algorithm Analysis and Recursion
**Weeks 3-4 | Status: IMMEDIATE DEVELOPMENT**

## Learning Objectives
1. Measure algorithm performance using Big O notation
2. Benchmark real code using timing tools
3. Implement recursive algorithms (factorial, Fibonacci)
4. Understand recursion through visualization and call stacks
5. Compare iterative vs recursive solutions

---

## Week 3: Big O and Measurement

### Day 7: "Feeling the Difference"
**What Students Build**: Benchmarking experiments

**Hook** (10 min):
> "Which is faster: finding a book in a sorted library or unsorted pile?"

**Hands-On** (30 min):
- Provide two search functions: linear and binary
- Students time them with increasing N (100, 1000, 10000 items)
- Plot results (spreadsheet or simple graph)
- Notice: linear grows linearly, binary barely increases

**Discovery Question**:
> "Binary search is 'faster'—but what does that mean mathematically?"

**Introduce Big O** (10 min):
- O(N) vs O(log N) notation
- "Describes growth rate, not exact seconds"

**Homework**: Read Runestone 2.2-2.3 (Big O fundamentals)

---

### Day 8: Big O in Practice
**What Students Build**: Complexity analyzer

**Activity**: Given 5 code snippets, identify Big O
- Single loop: O(N)
- Nested loops: O(N²)
- Binary search pattern: O(log N)
- Constant time: O(1)

**AI Collaboration**:
> "Here's my code [paste]. What's the Big O complexity? Walk me through how you determined it."

**Lab Prep**: Release M02 Lab 1 - "Benchmark Report"

---

### Day 9: Recursion Introduction
**What Students Build**: Recursive factorial

**Visualization First** (15 min):
- Show recursion tree for factorial(4)
- Python Tutor demonstration (pythontutor.com)
- "Function calls itself with smaller problem"

**Build Challenge** (25 min):
> "Write factorial() recursively. Two rules: (1) Base case, (2) Recursive case."

**Common Mistakes Workshop** (10 min):
- Forgot base case → infinite recursion
- Wrong base case → stack overflow
- "Let's fix these together"

**Homework**: Implement Fibonacci recursively

---

## Week 4: Recursion Mastery

### Day 10: Recursion Patterns
**What Students Build**: Multiple recursive functions

**Pattern Recognition**:
- Direct recursion (calls itself)
- Tail recursion (last operation is recursive call)
- Multiple recursion (Fibonacci calls twice)

**Live Coding**: Tower of Hanoi
- Runestone 4.10 (Python) or 5.10 (C++)
- "Build it, then understand it"

---

### Day 11: Iterative vs Recursive
**What Students Build**: Both versions of same algorithm

**Comparison Lab**:
- Implement factorial: iterative AND recursive
- Time both versions
- Discuss: "Which is better? Depends on context!"

**Memory Model**:
- Show call stack growth (recursion)
- Compare to loop (constant memory)

---

### Day 12: M02 Lab Work Session
**M02 LAB: Recursive Art or Algorithm**

**Option A: Fractal Generator** (visual students)
- Recursive function draws fractal pattern
- Base case: small enough to stop
- Uses turtle graphics or simple plotting

**Option B: Recursive Search** (algorithm students)
- Binary search implementation
- Must be recursive (not iterative)
- Compare performance to linear search

**Requirements**:
- Recursive solution
- Base case clearly identified
- Benchmarking results
- Complexity analysis written in plain English

---

## M02 Resources

### Zybooks Integration (LIGHT)
- **Chapter 2.2-2.4**: Big O definitions (reference)
- **Chapter 2.5-2.8**: Skip (too language-specific)

### Runestone Academy (PRIMARY)
- **2.2-2.4**: Big O (read actively, try examples)
- **4.2-4.6 (Python) / 5.2-5.6 (C++)**: Recursion fundamentals
- **4.10 / 5.10**: Tower of Hanoi (work through together)

### Custom Materials (TO DEVELOP)
- [ ] Benchmarking quick reference (timeit/chrono)
- [ ] Recursion debugging guide
- [ ] "When to Use Recursion" decision tree

---

# MODULE 3: Arrays and Sorting
**Weeks 5-6 | Status: MODERATE DEVELOPMENT**

## Learning Objectives
1. Implement selection sort, insertion sort, merge sort
2. Visualize sorting algorithms step-by-step
3. Benchmark sorting performance on different data
4. Understand divide-and-conquer strategy (merge sort)
5. Choose appropriate sort for given scenario

---

## Week 5: Simple Sorts

### Day 13: Selection Sort - Build It
**What Students Build**: Selection sort from scratch

**Challenge** (30 min):
> "Sort this array by repeatedly finding the minimum. No looking up algorithms!"

**Discovery Process**:
1. Students attempt implementation
2. Compare approaches (whiteboard)
3. Show VisuAlgo demonstration
4. Refine implementation
5. Read Runestone 5.8 (Python) / 7.4 (C++)

**Complexity Analysis**:
- Count comparisons manually for small array
- Notice: always O(N²), regardless of initial order

---

### Day 14: Insertion Sort
**Pattern**: Same as Selection Sort day
- Build challenge first
- Visualize with VisuAlgo
- Compare to selection sort
- Notice: better on "nearly sorted" data

---

### Day 15: Sorting Comparison Lab
**What Students Build**: Sorting benchmark suite

**Lab**: Implement 3 sorts, benchmark each on:
- Random data
- Already sorted data
- Reverse sorted data

**Discovery**: Insertion sort wins on nearly-sorted data!

---

## Week 6: Divide and Conquer

### Day 16: Merge Sort - Theory
**What Students Build**: Understanding (implementation next day)

**Visualization Heavy**:
- VisuAlgo merge sort animation
- Draw recursion tree on board
- "Divide, conquer, merge"

---

### Day 17: Merge Sort - Implementation
**What Students Build**: Merge sort from pseudocode

**Scaffold Approach**:
1. Provide merge() function (the hard part)
2. Students write mergeSort() recursive wrapper
3. Test and debug together

---

### Day 18: M03 Lab Work Session
**M03 LAB: Sorting Visualizer**

**Project**: Build a sorting visualizer (text-based or graphical)
- User picks sort algorithm
- Shows step-by-step process
- Reports comparison count

**Extension**: Add shell sort or quick sort

---

## M03 Resources

### Zybooks (REFERENCE)
- Chapter 3: Skim algorithms, focus on pseudocode

### Runestone (PRIMARY)
- Sections 5.7-5.11 (Python) / 7.3-7.7 (C++)

### VisuAlgo
- Heavy use: https://visualgo.net/en/sorting

---

# MODULE 4: Linear Structures
**Weeks 7-8 | Status: SIGNIFICANT DEVELOPMENT (Materials Exist)**

## Learning Objectives
1. Implement node-based linked lists from scratch
2. Understand pointer/reference manipulation
3. Build applications using stacks and queues
4. Compare array-based vs node-based implementations
5. Handle edge cases (empty structures, full structures)

---

## Week 7: Linked Lists Deep Dive

### Day 19: Nodes and Pointers
**What Students Build**: Node class and basic operations

**Concept**: 
- Node = data + pointer to next
- Head pointer tracks first node
- Traversal by following next pointers

**Challenge**: Implement prepend (add to front)

---

### Day 20: Insertion and Deletion
**What Students Build**: Insert at position, delete node

**Pointer Logic Practice**:
- Draw diagrams for every operation
- "Break it, fix it" debugging session
- Common mistake: losing references

---

### Day 21: Linked List Lab
**What Students Build**: Complete linked list implementation

**Features**:
- Append, prepend, insert at index
- Delete by value, delete by index
- Search, length, display

---

## Week 8: Applications

### Day 22: Stack Application
**M04 LAB 1: Undo System** (if not done in M01)

---

### Day 23: Queue Application  
**M04 LAB 2: Request Queue Simulator**

**Scenario**: Customer service queue
- Requests arrive at random intervals
- Server processes at fixed rate
- Calculate average wait time

---

### Day 24: Midterm Review
- "What have we built so far?"
- Preview second half of course
- Reflection: "Create first" working for you?

---

## M04 Resources

### Existing Materials (Use These!)
- `module-04/tutorials/stacks.md` (complete)
- `module-04/rubrics/stacks-queues-rubric.yaml` (complete)

### Runestone (PRIMARY)
- Chapter 3 (Python) / Chapters 3-4 (C++)

---

# MODULE 5: Hashing (OUTLINE)
**Weeks 9-10 | Status: TO BE DEVELOPED**

## Preliminary Structure

**Week 9: Hash Functions and Tables**
- Day 25: Hash function design
- Day 26: Collision resolution strategies
- Day 27: Hash table implementation

**Week 10: Applications**
- Day 28: Dictionary ADT
- Day 29: Set operations
- Day 30: M05 Lab - Custom hash table

**Resources**:
- Runestone Chapter 6 (Python) / Chapter 6 (C++)
- Zybooks Chapter 6 (light reference)

**To Develop**:
- [ ] Hash function visualization tool
- [ ] Collision resolution animation
- [ ] Real-world dataset for hashing practice

---

# MODULE 6: Trees (OUTLINE)
**Weeks 11-12 | Status: TO BE DEVELOPED**

## Preliminary Structure

**Week 11: Binary Trees and BST**
- Day 31: Tree terminology and structure
- Day 32: BST operations (insert, search)
- Day 33: Tree traversals (inorder, preorder, postorder)

**Week 12: Heaps and Priority Queues**
- Day 34: Heap property and operations
- Day 35: Priority queue implementation
- Day 36: M06 Lab - BST or heap project

**Resources**:
- Runestone Chapters 6-7 (Python) / Chapters 7-9 (C++)
- VisuAlgo tree visualizations

**To Develop**:
- [ ] Tree drawing exercises
- [ ] Expression tree evaluator
- [ ] Huffman coding project (uses heap)

---

# MODULE 7: Graphs (OUTLINE)
**Weeks 13-14 | Status: TO BE DEVELOPED**

## Preliminary Structure

**Week 13: Graph Fundamentals**
- Day 37: Graph representations (adjacency matrix/list)
- Day 38: Graph traversals (BFS, DFS)
- Day 39: M07 Lab Part 1 - Graph builder

**Week 14: Graph Algorithms**
- Day 40: Shortest path (Dijkstra's)
- Day 41: Real-world applications
- Day 42: M07 Lab Part 2 - Social network analysis

**Resources**:
- Runestone Chapter 10
- BRIDGES dataset integration (if time permits)

**To Develop**:
- [ ] Graph visualization tool
- [ ] Real-world graph datasets
- [ ] BFS/DFS step-by-step guide

---

# MODULE 8: Integration Project (OUTLINE)
**Weeks 15-16 | Status: TO BE DEVELOPED**

## Preliminary Structure

**Week 15: Project Development**
- Day 43: Final project kickoff
- Day 44: Work session
- Day 45: Peer code review

**Week 16: Presentations and Wrap-Up**
- Day 46: Project demos (group 1)
- Day 47: Project demos (group 2)
- Day 48: Course reflection and next steps

**Final Project Requirements** (Draft):
- Uses at least 3 different data structures
- Solves a real-world problem
- Includes complexity analysis
- Documented AI collaboration
- Submitted via PR with peer review

**To Develop**:
- [ ] Project ideas list
- [ ] Rubric for final project
- [ ] Presentation guidelines
- [ ] Peer review rubric

---

# Development Priorities

## Immediate (This Month)
1. Complete M01 materials (ADT intro, GitHub workflow, AI prompting)
2. Complete M02 materials (Big O, recursion, benchmarking)
3. Refine M03 structure (sorting labs)
4. Polish M04 existing materials (stacks tutorial)

## Next Phase (After M01-M04 Taught)
5. Develop M05-M06 based on student feedback
6. Collect data: What's working with "create first"?
7. Iterate on AI collaboration patterns
8. Build M07-M08 with insights from early modules

## Throughout Semester
- Document student questions (FAQ)
- Collect best AI prompts (student contributions)
- Refine rubrics based on actual grading
- Gather feedback on Zybooks vs Runestone usage

---

# Teaching Notes

## Consistency Patterns

Every module follows:
1. **Build First** (hands-on challenge)
2. **Visualize** (VisuAlgo or Python Tutor)
3. **Read** (Runestone, selective)
4. **Refine** (improve initial implementation)
5. **Apply** (lab/project)

## Time Budgets
- Lecture: 20% (concepts, motivation)
- Live coding: 30% (demonstrate, not dictate)
- Student work: 40% (build, struggle, ask)
- Discussion: 10% (reflection, synthesis)

## Pivot Points
- After M04: Check if "create first" is working
- After M06: Assess dual-language approach
- After M07: Preview final project options

---

*This breakdown will evolve as we learn what works. M01-M04 are "set" for now. M05-M08 are flexible based on early feedback.*
