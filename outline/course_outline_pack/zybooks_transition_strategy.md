# Zybooks Transition Strategy
## Final Semester Usage Plan (Spring 2026)

**Situation**: This is your last semester with Zybooks access. You're transitioning to Runestone Academy + custom materials. This document guides how to use Zybooks effectively WITHOUT creating dependency, while building materials for future semesters.

---

## Strategic Framing: Zybooks as Reference, Not Primary Text

### What Zybooks IS (This Semester)
- âœ… Quick reference for definitions
- âœ… Algorithm pseudocode source
- âœ… Backup explanations when Runestone doesn't click
- âœ… Example code library

### What Zybooks IS NOT (This Semester)
- âŒ The primary learning path
- âŒ Required reading
- âŒ Source of exercises (skip most of them)
- âŒ What you build your lectures around

**Key Message to Students**:
> "We have Zybooks access this semester as a reference. Use it like a dictionary—look things up when you need them. It's NOT required reading. Your primary resources are Runestone, VisuAlgo, and the course GitHub."

---

## Chapter-by-Chapter Usage Guide

### Chapter 1: Introduction to Data Structures
**Zybooks Strength**: Comprehensive overview of all structures
**Zybooks Weakness**: Too much theory upfront, intimidates beginners

**Usage Strategy**:
- **Week 1**: Assign reading of 1.3-1.6 ONLY (why study DS/algorithms)
  - Skip 1.1-1.2 (course overview—you'll cover this your way)
  - Skip 1.7+ (language review—they know this from CSC 134)
- **As Reference**: When a student asks "What's a hash table?" → "Skim Zybooks 1.5.6"
- **Skip Entirely**: All Chapter 1 exercises (not worth the time)

**Replacement**:
- Use project documents for motivation (M5LAB_A style)
- Runestone 1.3-1.6 covers same material with better interactivity

---

### Chapter 2: Searching and Algorithm Analysis
**Zybooks Strength**: Clear Big O explanations and examples
**Zybooks Weakness**: Too abstract without hands-on building

**Usage Strategy**:
- **Week 3**: Optional reference for Big O rules
  - Section 2.2: Growth rates (read if Runestone 2.2 doesn't click)
  - Section 2.3: Big O notation (same as Runestone)
  - Section 2.4: Analyzing algorithms (good supplemental examples)
- **Week 4**: Recursion reference
  - Skip Zybooks recursion (Runestone is better)
  - Use only if student specifically struggles with Runestone
- **Skip**: Sections 2.5-2.8 (language-specific container analysis—Runestone covers this better)

**Replacement**:
- Runestone 2.2-2.4 (primary Big O source)
- Your custom benchmarking lab (measures actual performance)
- VisuAlgo (for recursion visualization)

**When Students Should Use**:
> "After you've benchmarked your own code and noticed the pattern, read Zybooks 2.3 to see if your observations match the formal Big O definition."

---

### Chapter 3: Sorting Algorithms
**Zybooks Strength**: Comprehensive sorting algorithm collection
**Zybooks Weakness**: Doesn't emphasize implementation; too reference-like

**Usage Strategy**:
- **Week 5-6**: Algorithm reference only
  - Students implement sorts FIRST (your lab)
  - Then check Zybooks pseudocode AFTER
  - Use for: "Did I implement selection sort correctly?"
- **Helpful Sections**:
  - 3.2-3.4: Selection/Insertion sort pseudocode
  - 3.5: Shell sort (if you include it)
  - 3.6-3.7: Merge/Quick sort (divide-and-conquer reference)
- **Skip**: All animations (VisuAlgo is better)
- **Skip**: Exercises (build your own labs instead)

**Replacement**:
- Runestone 5.7-5.11 (Python) / 7.3-7.7 (C++)
- VisuAlgo sorting visualizations
- Your sorting visualizer lab

**Usage Pattern**:
1. Build the sort (no Zybooks)
2. Test and debug (no Zybooks)
3. Check pseudocode (quick Zybooks skim)
4. Read analysis (Runestone, not Zybooks)

---

### Chapter 4: Lists (Linked Lists)
**Zybooks Strength**: Clear node diagrams and pointer logic
**Zybooks Weakness**: C++ and Python sections diverge significantly

**Usage Strategy**:
- **Week 7-8**: Diagram reference
  - Use Zybooks diagrams for whiteboard inspiration
  - Students can reference for pointer manipulation patterns
  - Good for: "I keep losing my pointer references"
- **Useful Sections**:
  - 4.1-4.3: Linked list fundamentals (concepts)
  - 4.4-4.7: Insertion/deletion algorithms
  - 4.8: Doubly-linked lists
- **Skip**: Most exercises (your labs are better)

**Replacement**:
- Runestone 3.18-3.23 (Python) / 4.1-4.8 (C++)
- Your linked list lab (more scaffolded)
- Python Tutor (for visualizing pointer changes)

**Best Use Case**:
Student stuck on insert operation → "Draw it on paper first, then check Zybooks 4.4 to see if your diagram matches theirs."

---

### Chapter 5: Stacks and Queues
**Zybooks Strength**: Concise ADT definitions
**Zybooks Weakness**: Rushed implementation examples

**Usage Strategy**:
- **Week 7-8**: Quick reference only
  - ADT definitions (5.1, 5.4)
  - Implementation strategies (5.2, 5.5)
  - Skip applications (your labs are better)
- **When Useful**:
  - "What's the formal definition of a stack?" → Zybooks 5.1
  - "Array-based vs linked implementation?" → Zybooks 5.2

**Replacement**:
- Your existing `module-04/tutorials/stacks.md` (primary)
- Runestone 3.3-3.4, 3.10-3.11
- Your stack/queue labs

**Usage Frequency**: Minimal (you have better materials)

---

### Chapter 6: Hash Tables
**Zybooks Strength**: Clear collision resolution explanations
**Zybooks Weakness**: Abstract without real-world datasets

**Usage Strategy**:
- **Week 9-10**: Collision strategy reference
  - Section 6.2: Direct hashing (concept only)
  - Section 6.3: Chaining (good explanation)
  - Section 6.4: Open addressing (linear probing)
- **Skip**: Performance analysis (too theoretical)
- **Skip**: Exercises (design your own with real data)

**Replacement**:
- Runestone Chapter 6 (both editions)
- Your custom hash table lab (with real datasets)

**Development Note**: 
M05 is underdeveloped. Zybooks can fill gaps this semester while you BUILD better materials. Take notes on what students find confusing—that informs your custom content.

---

### Chapters 7-9: Trees, Balanced Trees, Heaps
**Zybooks Strength**: Comprehensive tree coverage
**Zybooks Weakness**: Overwhelming; too much at once

**Usage Strategy**:
- **Week 11-12**: Selective reference
  - Chapter 7: BST basics (7.1-7.4)
  - Chapter 8: Skip entirely (AVL/Red-Black too advanced for CSC 249)
  - Chapter 9: Heap operations (9.1-9.3 only)
- **Best Use**: Definitions and diagrams
- **Skip**: Most implementations (Runestone is better)

**Replacement**:
- Runestone Chapters 6-7 (Python) / 7-9 (C++)
- VisuAlgo tree visualizations
- Your tree labs (to be developed)

**Development Priority**: 
M06 needs work. Use Zybooks to teach THIS semester, but document what needs custom materials.

---

### Chapter 10: Graphs
**Zybooks Strength**: Graph algorithms well-explained
**Zybooks Weakness**: No interesting datasets

**Usage Strategy**:
- **Week 13-14**: Algorithm reference
  - 10.1-10.3: Graph basics (representations)
  - 10.4-10.5: BFS/DFS algorithms
  - 10.6: Dijkstra's (if time permits)
- **Skip**: Exercises (you'll create better ones)

**Replacement**:
- Runestone Chapter 10
- BRIDGES (if you integrate real-world datasets)
- Your graph labs (to be developed)

---

### Chapters 11-12: Algorithms, B-Trees
**Zybooks Content**: Advanced topics beyond CSC 249 scope

**Usage Strategy**:
- **Don't Assign**: Too advanced for community college DS course
- **Exception**: Optional reading for advanced students

**Note**: 
Your course manifest shows M08 as "Integration Project," not advanced algorithms. This aligns with your goals—skip Zybooks 11-12 entirely.

---

## Weekly Zybooks Assignment Pattern

### Week 1-2 (M01): Minimal
- **Required**: Read 1.3-1.6 (motivation)
- **Optional**: Skim OOP review if needed
- **Time Investment**: 15-20 minutes

### Week 3-4 (M02): Light Reference
- **Required**: None
- **Suggested**: Check 2.2-2.3 after benchmarking lab
- **Time Investment**: 10 minutes (if used at all)

### Week 5-6 (M03): Algorithm Reference
- **Required**: None
- **Suggested**: Compare your sort to Zybooks pseudocode
- **Time Investment**: 15 minutes (for verification)

### Week 7-8 (M04): Diagram Reference
- **Required**: None
- **Suggested**: Use diagrams for linked list operations
- **Time Investment**: 10 minutes (when stuck)

### Week 9+ (M05-M08): Case-by-Case
- **Required**: None
- **Usage**: Only when Runestone doesn't cover a topic well

---

## What to Tell Students About Zybooks

### Framing the Resource

**Week 1 Announcement**:
> "We have Zybooks access this semester, but it's NOT our textbook. Think of it like Wikipedia—useful for looking things up, but not your main learning resource. Your primary tools are Runestone, VisuAlgo, and our labs. I may occasionally say 'check Zybooks section X if you want another explanation,' but it's never required unless I explicitly assign it."

**On Exercises**:
> "Zybooks has lots of exercises. We're NOT doing them. Why? Because our labs are better. Zybooks exercises are isolated problems. Our labs build real applications. Focus on the labs."

**On Reading Assignments**:
> "I'll assign very little Zybooks reading. When I do, it's short (10-15 minutes). If I say 'optional Zybooks reference,' that means: use it if you're stuck, but you can also skip it and use Runestone or ask me instead."

---

## Collecting Data for Future Semesters

### What to Track

**For Each Module**, note:
1. Which Zybooks sections did students actually find helpful?
2. Which Zybooks explanations were BETTER than Runestone?
3. Which Zybooks diagrams should you recreate in custom materials?
4. What questions kept coming up that neither Zybooks nor Runestone answered well?

**Method**:
- Ask students in weekly surveys: "What resources did you use this week?"
- Check office hours questions: "Where did you look first?"
- Review AI prompts.txt: Are students asking Claude to explain Zybooks or Runestone?

### Decision Points

**After M02**:
- Did students understand Big O from Runestone alone?
- If not, what Zybooks examples helped?
- → Build custom Big O lab with those examples

**After M04**:
- Did Zybooks diagrams help with pointers/linked lists?
- If yes, recreate similar diagrams in your materials
- If no, what visualization DID help? (Python Tutor? Hand-drawn?)

**After M06**:
- Trees are underdeveloped in your materials
- Which Zybooks sections filled the gaps?
- → Priority list for custom tree content

---

## Zybooks "Extinction Plan"

### This Semester (Spring 2026):
- Use Zybooks as described above (light reference)
- Track what students actually use
- Document gaps in Runestone/custom materials

### Summer 2026:
- Build custom materials for identified gaps
- Focus on M05-M06 (hashing, trees)
- Create Zybooks replacement diagrams
- Write 2-3 page supplements where needed

### Fall 2026 (First Zybooks-Free Semester):
- Runestone as primary text
- Your custom supplements fill gaps
- VisuAlgo + Python Tutor for visualizations
- Assess: What do we miss from Zybooks?

### Spring 2027 (Refinement):
- Iterate on Fall 2026 feedback
- Expand custom materials as needed
- Consider open textbook publishing (if materials mature)

---

## Emergency Procedures

### If Students Complain "I Need Zybooks!"

**Diagnosis**:
1. What specifically do they need?
   - Definition → Point to Runestone equivalent
   - Example code → GitHub repo has templates
   - Exercises → Our labs are the exercises

2. Is this learned helplessness?
   - "I can't learn without a textbook" → Habit from previous classes
   - Response: "You're learning by BUILDING. The textbook is your code."

3. Is there a genuine gap?
   - If MANY students ask for the same thing → You need to build it
   - Temporary fix: Assign that Zybooks section
   - Permanent fix: Add to summer development list

---

### If You're Tempted to Over-Rely on Zybooks

**Warning Signs**:
- You're assigning multiple chapters per week
- Students complain about reading load
- You're lecturing from Zybooks instead of building

**Correction**:
1. Re-read your course philosophy: "Create before theory"
2. Ask: Am I assigning reading because I haven't built the lab yet?
3. If yes: Build the lab. Reading is secondary.
4. If no: Reduce reading. More building, less consuming.

**Reminder**:
You're NOT teaching "what Zybooks covers." You're teaching "how to think with data structures." Zybooks is just one tool.

---

## Module-Specific Zybooks Dependency

### High Dependency (Need Alternatives Ready)
- **M05 (Hashing)**: Zybooks Chapter 6 is solid; you have less custom content
  - Priority: Develop hash table labs this summer
  - Temporary: Rely on Zybooks + Runestone Chapter 6

- **M06 (Trees)**: Zybooks Chapters 7-9 cover gaps in your materials
  - Priority: Develop tree tutorials and visualizations
  - Temporary: Use Zybooks diagrams, Runestone explanations

### Medium Dependency
- **M03 (Sorting)**: Zybooks is a good pseudocode reference
  - Alternative already exists: Runestone 5.7-5.11
  - Action: Minimal; already covered

### Low Dependency
- **M01 (Foundations)**: Zybooks 1.3-1.6 useful but replaceable
  - Alternative: Your own motivational materials
  - Action: Write 3-page "Why Data Structures" document

- **M02 (Algorithm Analysis)**: Zybooks Big O is fine but so is Runestone
  - Alternative: Runestone 2.2-2.4
  - Action: None needed

- **M04 (Linear Structures)**: You already have strong materials
  - Alternative: `module-04/tutorials/stacks.md` + Runestone
  - Action: Expand linked list tutorial slightly

### No Dependency
- **M07 (Graphs)**: Runestone Chapter 10 is comprehensive
- **M08 (Integration)**: No textbook needed (project-based)

---

## Budgeting Your Time

### This Semester: Teaching + Observation
- **Weekly**: 2-3 hours of Zybooks reference (for your own prep)
- **Monthly**: 1 hour documenting what students actually used
- **End of Semester**: 4-6 hours compiling "transition report"

### Summer 2026: Building Replacements
- **M05 Materials**: 20-30 hours (hash table labs, tutorials)
- **M06 Materials**: 30-40 hours (tree visualizations, labs)
- **General Supplements**: 10-15 hours (filling small gaps)
- **Total**: 60-85 hours (doable over 3 months)

### Fall 2026: Refinement
- **Weekly**: No Zybooks time! (freed up)
- **Monthly**: 2-3 hours updating custom materials based on feedback

---

## Final Thoughts: Making Zybooks Obsolete

**The Goal**:
By Fall 2026, when a student asks "What textbook do we use?", you can say:
> "Runestone Academy is our interactive textbook. I've also written custom materials for topics Runestone doesn't cover deeply. Between those two and VisuAlgo, you have everything you need."

**Not**:
> "We used to use Zybooks but can't afford it anymore."

**The Path**:
1. Use Zybooks lightly this semester (as described)
2. Note what it does well
3. Build those things into your materials
4. Replace, don't just remove

**Success Metric**:
In Fall 2026, students shouldn't feel like they're "missing" Zybooks. They should have something BETTER: custom, tested, iteratively-improved materials that fit your "create first" pedagogy perfectly.

---

## Appendix: Zybooks Chapter Mapping to Your Modules

| Your Module | Zybooks Chapters | Usage Level | Replacement Status |
|-------------|------------------|-------------|-------------------|
| M01 Foundations | 1 | Minimal | âœ… Ready (Runestone 1.3-1.6) |
| M02 Algorithm Analysis | 2 | Light | âœ… Ready (Runestone 2.2-2.4) |
| M03 Sorting | 3 | Medium | âœ… Ready (Runestone 5.7-5.11) |
| M04 Linear Structures | 4-5 | Light | âœ… Ready (Your tutorials + Runestone 3) |
| M05 Hashing | 6 | High | âš ï¸ Develop Summer 2026 |
| M06 Trees | 7-9 | High | âš ï¸ Develop Summer 2026 |
| M07 Graphs | 10 | Medium | âœ… Ready (Runestone 10) |
| M08 Integration | 11-12 | None | âœ… Ready (Project-based) |

**Action Items**:
- âœ… Ready: Use as-is
- âš ï¸ Develop: Priority for summer
- âŒ Block: Too advanced (skip)

---

*Zybooks has served you well. Now it's time to build something better. Use it strategically this semester, learn from it, then make it obsolete with your own superior materials.*
