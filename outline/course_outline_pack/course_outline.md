# CSC 249: Data Structures and Algorithms
## Course Outline - Spring 2026

**Credits**: 3 | **Prerequisites**: CSC 134 | **Format**: Dual-Language (C++ and Python)

---

## Philosophy Statement

> **"Bloom's Taxonomy Starts with Create"**
> 
> Students build working implementations first, then understand why they work. This inverts traditional instruction but aligns with how professional developers actually learn—by doing, breaking, fixing, and finally understanding at a deeper level.

### Core Principles

1. **Creation Before Theory**: Implement data structures before analyzing their complexity
2. **AI as Collaborator**: Mandatory AI tool usage with prompt documentation
3. **Language Flexibility**: Choose C++ or Python as primary, use AI to bridge concepts
4. **Workforce Readiness**: Real-world applications and professional workflows (GitHub, PRs)
5. **Struggle as Learning**: Debugging and iteration are features, not bugs

---

## Course Outcomes

By the end of this course, students will be able to:

1. **Implement** fundamental data structures (lists, stacks, queues, trees, graphs, hash tables) in C++ and Python
2. **Analyze** algorithm complexity using Big O notation and select appropriate structures for given problems
3. **Collaborate** effectively with AI tools, documenting prompts and learning processes
4. **Navigate** professional development workflows (version control, code review, pull requests)
5. **Translate** concepts between C++ and Python using AI as a bridge when stuck

---

## Semester Schedule (16 Weeks)

### Module 1: Foundations (Weeks 1-2)
**Theme**: "Building Your Toolkit"

- **Topics**: OOP review, encapsulation, ADTs, AI collaboration patterns
- **Deliverables**: 
  - GitHub setup + first PR
  - Simple class implementation (Stack or Queue)
  - AI prompts documentation
- **Zybooks Support**: Chapter 1 (light reading, reference only)
- **Focus**: Establishing workflows and "create first" mindset

---

### Module 2: Algorithm Analysis (Weeks 3-4)
**Theme**: "Measuring What Matters"

- **Topics**: Big O notation, recursion, benchmarking
- **Deliverables**:
  - Recursive algorithm implementation
  - Benchmarking lab (timeit/chrono)
  - Complexity analysis report
- **Zybooks Support**: Chapter 2 (Big O reference)
- **Focus**: Understanding performance through measurement, not theory

---

### Module 3: Sorting (Weeks 5-6)
**Theme**: "The Classics That Matter"

- **Topics**: Selection sort, insertion sort, merge sort
- **Deliverables**:
  - Sorting visualizer project
  - Performance comparison lab
  - Real-world sorting application
- **Zybooks Support**: Chapter 3 (algorithm reference)
- **Focus**: Build sorters, then understand why merge sort wins

---

### Module 4: Linear Structures (Weeks 7-8)
**Theme**: "Chains, Stacks, and Lines"

- **Topics**: Linked lists, stacks, queues, deques
- **Deliverables**:
  - Undo system (stack)
  - Request queue simulator (queue)
  - Linked list from scratch
- **Zybooks Support**: Chapter 4 (reference for concepts)
- **Focus**: Pointer/reference manipulation, LIFO/FIFO patterns

**Milestone**: Midterm check-in (week 8) - Students should be comfortable with "build-then-understand"

---

### Module 5: Hashing (Weeks 9-10)
**Theme**: "Magic Index Tricks"

- **Topics**: Hash functions, collision resolution, hash tables
- **Deliverables**:
  - Custom hash function
  - Dictionary implementation
  - Collision handling comparison
- **Zybooks Support**: Chapter 6 (light reference)
- **Focus**: Why O(1) lookup is "magic" and when it breaks

---

### Module 6: Trees (Weeks 11-12)
**Theme**: "Hierarchies and Search"

- **Topics**: Binary trees, BSTs, tree traversals, heaps
- **Deliverables**:
  - BST implementation
  - Expression tree evaluator
  - Priority queue with heap
- **Zybooks Support**: Chapters 7-9 (selective reading)
- **Focus**: Recursive structure, why trees enable O(log N)

---

### Module 7: Graphs (Weeks 13-14)
**Theme**: "Networks and Connections"

- **Topics**: Graph representations, BFS, DFS, shortest path
- **Deliverables**:
  - Graph builder (adjacency list/matrix)
  - Social network analyzer (BFS/DFS)
  - Shortest path application
- **Zybooks Support**: Chapter 10 (algorithms reference)
- **Focus**: Real-world networks (social media, maps, dependencies)

---

### Module 8: Integration (Weeks 15-16)
**Theme**: "Putting It All Together"

- **Topics**: Selecting appropriate structures, optimization, final project
- **Deliverables**:
  - Final project (multi-structure application)
  - Complexity analysis documentation
  - Reflection: "What I Built, What I Learned"
- **Zybooks Support**: None (synthesis mode)
- **Focus**: Capstone demonstrating structure selection and implementation

---

## Assessment Structure

### Grade Breakdown
- **Labs (40%)**: Hands-on implementation assignments
- **Homework (25%)**: Problem-solving and analysis
- **Projects (20%)**: Module capstone implementations
- **Participation (10%)**: PR reviews, AI prompt sharing, peer feedback
- **Final Project (5%)**: Synthesis project (Module 8)

### Lab Philosophy
- **Submit code + prompts.txt**: AI collaboration is required, not cheating
- **Working code > perfect code**: Functionality first, optimization later
- **Test-driven**: If it passes tests, it works (then we discuss why)

### Prompt Documentation
Every lab requires `prompts.txt` showing:
- What you asked the AI
- How you modified its suggestions
- What you learned from the interaction

---

## Resource Ecosystem

### Primary Resources
1. **Runestone Academy** (Free, Interactive)
   - C++ edition: https://runestone.academy/ns/books/published/cppds
   - Python edition: https://runestone.academy/ns/books/published/pythonds3
   - Use: Concept reference and interactive exercises

2. **VisuAlgo** (visualgo.net)
   - Visual demonstrations of all major data structures
   - Use: "See it before you build it"

3. **Course GitHub Repository**
   - Templates, rubrics, labs, tutorials
   - PR workflow for all submissions

### Supplemental Resources
4. **Zybooks** (This Semester Only)
   - Light reference for definitions and examples
   - NOT the primary text
   - Use: Quick concept lookup

5. **Video Resources**
   - William Fiset (YouTube) - Best visualizations
   - MyCodeSchool - C/C++ foundations
   - Abdul Bari - Algorithm analysis

6. **Practice Platforms**
   - Codewars (gamified practice)
   - Exercism (mentored feedback)
   - HackerRank (structured exercises)

---

## AI Tool Integration

### Required Tools
Students MUST use at least one:
- Claude (claude.ai or API)
- ChatGPT
- GitHub Copilot

### Acceptable Use
âœ… **Encouraged**:
- "Explain how this algorithm works"
- "Show me this in [other language]"
- "Why is my pointer logic wrong?"
- "Help me understand this error"

âš ï¸ **Discouraged** (but not forbidden):
- "Write all my code for me"
- Copy/paste without understanding

ðŸ"„ **Required**:
- Document all AI interactions in `prompts.txt`
- Be able to explain your code in your own words

### Assessment
- Cannot explain your code = cannot receive full credit
- "AI wrote it" is not an excuse for not understanding
- Prompts.txt shows learning process and earns participation credit

---

## Language Track System

### Dual-Language Approach
Students choose a **primary language** (C++ or Python) for deliverables but are encouraged to explore both using AI as a translator.

**C++ Track Students**:
- Submit labs in C++
- Can ask AI: "Show me this Python concept in C++"
- Understand memory management, pointers, compilation

**Python Track Students**:
- Submit labs in Python
- Can ask AI: "Why does C++ need pointers for this?"
- Understand dynamic typing, memory abstraction

### Cross-Language Learning
**Encouraged prompt pattern**:
> "I'm stuck on [concept] in [my language]. Show me how [other language] handles this, then explain what that tells me about my language."

---

## Weekly Rhythm

### Typical Week Structure

**Monday**: Concept Introduction
- 15 min: "What we're building this week"
- 20 min: VisuAlgo demonstration
- 15 min: Start lab together (live coding)

**Wednesday**: Implementation Workshop
- 10 min: Common struggles from Monday
- 30 min: Lab work time with roaming help
- 10 min: AI collaboration tips

**Friday**: Analysis & Reflection
- 15 min: Student demos (show your code)
- 20 min: "Now let's understand why"
- 15 min: Next week preview

---

## Office Hours Philosophy

### "Debugging Together" Sessions
- Bring your broken code (encouraged!)
- We trace through execution together
- Learn to debug, not just get fixes
- "What did you try?" is always the first question

### AI Collaboration in Office Hours
- Show me your prompts
- Let's iterate on better questions
- AI is allowed in office hours too

---

## Accommodations for Different Backgrounds

### For Students Who Struggled in CSC 134
- Pair programming options
- Extended lab deadlines with check-ins
- Focus on Python track (gentler memory model)

### For Students Who Excelled in CSC 134
- Extension challenges on every lab
- Dual-language submissions (bonus credit)
- Lead study groups (participation credit)

### For Students New to AI Tools
- Week 1 intensive: "How to Prompt"
- Templates for effective questions
- Buddy system for AI newcomers

---

## Success Metrics

### "You're Getting It" Signs
- Debugging on your own before asking for help
- Explaining code in your own words (not parroting)
- Choosing appropriate structures without prompting
- Helping classmates understand concepts

### "You're Struggling" Signs (Get Help Early!)
- Same error patterns repeating
- Cannot explain code you submitted
- Not documenting AI prompts
- Avoiding office hours

---

## Course Culture

### Core Values
1. **Iteration > Perfection**: Your 3rd attempt is better than someone's 1st
2. **Questions > Silence**: "I don't understand" is brave, not weak
3. **Collaboration > Competition**: We all learn faster together
4. **Building > Memorizing**: You can look up syntax; you can't look up problem-solving

### Expected Behaviors
- Share your struggles in PR comments
- Ask for help in public channels (others have same question)
- Document your AI conversations (helps future students)
- Give meaningful PR feedback to peers

---

## Looking Ahead: Course Evolution

### This Semester (Spring 2026)
- Zybooks as light reference
- Building Runestone integration
- Establishing AI collaboration norms
- Collecting feedback on "create first" approach

### Future Semesters
- Heavier Runestone reliance
- Custom lab materials based on this semester's feedback
- Student-contributed resources (best AI prompts, debugging guides)
- Potentially BRIDGES integration for real-world datasets

---

## Contact & Resources

- **Course Repository**: [GitHub link]
- **Discussion Forum**: [Slack/Discord]
- **Office Hours**: [Schedule]
- **AI Tool Support**: [Documentation links]

---

*"The best way to learn data structures is to break them, fix them, and finally understand them. Welcome to CSC 249."*
