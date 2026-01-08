# AI Collaboration Integration Framework
## Making AI Mandatory (Not Just Allowed) in CSC 249

**Core Premise**: AI collaboration is a required skill, not optional assistance. Students must demonstrate effective AI partnership, not just code completion. This document operationalizes that philosophy.

---

## Why Mandatory AI Collaboration?

### The Workforce Reality
Professional developers in 2026:
- Use GitHub Copilot, Claude, ChatGPT daily
- Pair program with AI to explore solutions
- Debug with AI assistance
- Learn new frameworks with AI tutoring

**Our Choice**:
- Ban AI → Students secretly use it anyway, learn bad habits
- Allow AI → Students use it as search engine, don't develop skill
- **Require AI** → Students learn effective collaboration, document process

### The Learning Paradox
âŒ **Traditional Fear**: "AI will do their thinking for them"
âœ… **Reality**: Good AI collaboration requires MORE thinking:
- Formulating clear questions (metacognition)
- Evaluating AI suggestions critically (analysis)
- Debugging AI's mistakes (deeper understanding)
- Explaining code in your own words (synthesis)

**Students who use AI well learn more, not less.**

---

## Three Tiers of AI Collaboration

### Tier 1: AI as Reference (M01-M02)
**Goal**: Replace Google/Stack Overflow with conversational help

**Acceptable Prompts**:
- "What's the difference between a stack and a queue?"
- "Explain this error message: [paste error]"
- "What does this line of code do: [paste line]"

**Learning Outcome**: Students can get unstuck without instructor

**Assessment**: Basic `prompts.txt` documentation

---

### Tier 2: AI as Pair Programmer (M03-M05)
**Goal**: Collaborate on implementation, not just consume answers

**Acceptable Prompts**:
- "I'm implementing merge sort. Here's my approach: [explain]. What problems do you see?"
- "My insertion function crashes. Here's my code: [paste]. Walk me through debugging it."
- "Show me how to do X in [other language] so I understand the concept."

**Learning Outcome**: Students iterate with AI, don't just copy

**Assessment**: Prompts.txt shows evolution of understanding

---

### Tier 3: AI as Learning Accelerator (M06-M08)
**Goal**: Use AI to explore advanced concepts independently

**Acceptable Prompts**:
- "I want to optimize this hash function. Explain three approaches with tradeoffs."
- "Compare my BST implementation to textbook solutions. What did I do differently?"
- "Help me design a graph structure for [novel problem]. Ask me clarifying questions."

**Learning Outcome**: Students use AI for expertise beyond course scope

**Assessment**: Students explain WHY they chose AI's suggestion (or didn't)

---

## The `prompts.txt` System

### What It Is
Every lab submission includes `prompts.txt`:
```
# AI Collaboration Log - [Lab Name] - [Your Name]

## Date: 2026-01-15
**AI Tool**: Claude 3.5 Sonnet

### Prompt 1: Understanding the requirement
Me: "Explain what a stack's push() operation should do. Don't give me code yet."
AI: [paste response]
My takeaway: Stack adds to top, needs to track size

### Prompt 2: Debugging my attempt
Me: "My push() function isn't working. Here's my code: [paste]"
AI: [paste response]
What I tried: AI suggested tracking top index. I implemented it.
Result: Still buggy - forgot to increment index

### Prompt 3: Edge case
Me: "What happens if the stack is full?"
AI: [paste response]
My decision: Added capacity check, return false if full
```

### Why It Works
1. **Forces Reflection**: Students must articulate what they learned
2. **Shows Process**: Instructor sees iteration, not just final code
3. **Builds Metacognition**: "I learned X from this conversation"
4. **Prevents Plagiarism**: Harder to fake than just submitting code

---

## Assessment Framework

### Grading AI Collaboration (All Labs)

**Prompts.txt Rubric** (10-15% of lab grade):

**Excellent (10/10)**:
- 3+ prompts showing iteration
- Each prompt has clear "what I learned" takeaway
- Evidence of trying AI's suggestion and modifying it
- Shows both understanding and debugging

**Good (7-9/10)**:
- 2-3 prompts, mostly conceptual questions
- Some evidence of iteration
- Basic takeaways present
- Shows understanding

**Minimal (4-6/10)**:
- 1-2 prompts, very basic
- "Write my code" style questions
- Vague or missing takeaways
- Copy/paste without modification

**Unacceptable (0-3/10)**:
- No prompts.txt file
- Only "write my code" prompts
- No evidence of learning from AI
- Code obviously AI-generated, not understood

---

### The "Explain Your Code" Checkpoint

**Every major lab includes an explanation requirement**:

**Option A: Written Explanation** (PR comment):
> "Walk through your `insert()` function line by line. What does each line do? Why is it necessary?"

**Option B: 5-Minute Demo** (Office hours or class):
> "Show me your code running. Change one value. Predict what will happen. Explain why."

**Option C: Code Annotation** (Comments in code):
> "Add comments explaining the WHY, not just the WHAT, for your complex functions."

**Grading Principle**:
- Can explain fluently → Full credit (even if code has small bugs)
- Can explain most, struggles with parts → Partial credit
- Cannot explain or wrong explanation → No credit (even if code works)

**The Rule**:
> "If you can't explain it, you didn't write it (in any meaningful sense). AI collaboration requires understanding your code."

---

## Classroom Integration

### Week 1: AI Collaboration Bootcamp

**Day 1: Introduction**
- "AI is required, not optional. Here's why..."
- Demonstrate good vs bad prompts (live)
- Distribute prompt templates

**Day 2: Practice Session**
- Small problem: Implement `Box` class
- Students must ask AI for help at least once
- Share prompts as a class: "Which prompts got useful responses?"

**Day 3: Prompts.txt Workshop**
- Review sample prompts.txt (good and bad examples)
- Students create their first prompts.txt
- Peer review: "Would I understand your learning process from this?"

---

### Weekly Patterns (M01-M08)

**Monday: Introduce Concept**
- "Here's what we're building. Try it for 30 minutes."
- "You SHOULD ask AI for help. Document it."

**Wednesday: Share Prompts**
- "What did you ask AI this week?"
- "Who got a really helpful response? Share it."
- "Who got a bad response? Let's debug the prompt together."

**Friday: Synthesis**
- "What did AI teach you? What did you teach yourself?"
- "Which AI responses were wrong? How did you know?"

---

## Preventing AI Dependency

### The Guardrails

**Requirement 1: No-AI Assessments**
Every module includes ONE in-class exercise without AI:
- Whiteboard a linked list insertion
- Hand-trace a recursive function
- Explain Big O for given code

**Purpose**: Verify understanding exists independent of AI

---

**Requirement 2: AI Response Critique**
Occasionally, provide an INTENTIONALLY FLAWED AI response:
> "I asked Claude to explain quicksort. Here's what it said: [paste flawed explanation]. What's wrong with this response?"

**Purpose**: Students learn AI is fallible, develop critical evaluation

---

**Requirement 3: Cross-Examination**
Random selection of students for "explain your code" demos:
- Not punitive—just verification
- 5 minutes, informal
- Focus: "Help me understand your thinking"

**Purpose**: Students know they might be asked, so they learn the code

---

## Tools and Logistics

### Recommended AI Tools (Students Choose One)

**Claude (claude.ai)**
- âœ… Best for explanations and teaching
- âœ… Understands context well
- âœ… Free tier sufficient for course
- âœ… Can show code in both C++ and Python

**ChatGPT (openai.com)**
- âœ… Good for quick questions
- âœ… Free tier available
- âœ… Code interpreter useful for testing
- âš ï¸ Sometimes gives outdated syntax

**GitHub Copilot**
- âœ… Best for code completion in IDE
- âœ… Learns your style
- âœ… Educational license free
- âš ï¸ Less useful for conceptual questions

**Gemini (Google)**
- âœ… Integrated with Google workspace
- âš ï¸ Sometimes verbose
- âš ï¸ Code quality varies

**Students pick ONE as primary, can use others supplementally**

---

### Prompts.txt Template (Provide This)

```markdown
# AI Collaboration Log
**Lab**: [Lab name]
**Student**: [Your name]
**Primary AI Tool**: [Claude/ChatGPT/Copilot/Other]

---

## Session 1: [Date and time]

### What I was trying to do:
[Brief description of the task or problem]

### Prompt:
```
[Paste your exact prompt to the AI]
```

### AI Response:
```
[Paste relevant parts of AI's response - or summarize if very long]
```

### What I did with this information:
[Explain how you used or modified AI's suggestion]

### What I learned:
[Key takeaway from this interaction]

### Result:
[Did it work? What happened next?]

---

## Session 2: [Date and time]
...

---

## Overall Reflection:
- What was most helpful about using AI for this lab?
- What did you struggle to get AI to understand?
- What did you figure out without AI that you initially wanted help with?
```

**Provide as `prompts-template.txt` in every lab repo**

---

## Addressing Common Concerns

### Concern 1: "Students Will Just Ask AI to Write Everything"

**Response**: They already do that with Google/Stack Overflow

**Solution**:
- Require explanation of code (they must understand)
- Grade prompts.txt (lazy prompts get low scores)
- In-class no-AI checkpoints (verify learning)

**Reality**: 
Students who ask "write my code" learn quickly that they can't explain it and fail the explanation checkpoint. They adapt.

---

### Concern 2: "How Do I Know They Actually Used AI (Not Fabricating Prompts)?"

**Detection**:
- AI responses have distinctive phrasing (you'll recognize)
- Students who fabricate can't explain their code
- Timestamps in prompts.txt (compare to commit history)

**Prevention**:
- Emphasize: "Prompts.txt is for YOUR benefit—shows your learning"
- Make prompts.txt worth enough to matter (10-15%)
- Spot-check: Ask students to show you actual AI conversation in tool

**Philosophy**:
We trust students. If they cheat themselves out of learning, their code explanations will reveal it.

---

### Concern 3: "What If AI Gives Them Wrong Code?"

**Response**: GOOD! That's the learning opportunity.

**Approach**:
- "Who got bad code from AI this week? Share!"
- "How did you figure out it was wrong?"
- "What did you learn from debugging AI's mistake?"

**Teaching Moment**:
> "AI is a tool, not an authority. If AI's code fails your tests, that's AI's problem, not yours. You're the programmer—you're responsible for understanding and verifying everything."

---

### Concern 4: "Students Who Don't Use AI Will Be Disadvantaged"

**Response**: This is a required skill. Not using AI is like not using a debugger.

**Accommodation**:
- Week 1 bootcamp (everyone starts together)
- Templates and examples (lower barrier to entry)
- Office hours support for AI beginners

**Philosophy**:
In 2026, professional developers use AI. We're teaching workforce skills. If a student refuses to use AI, they need to understand they're opting out of industry-standard practice.

---

## Advanced Integration (M05+)

### AI as Cross-Language Bridge

**Pattern for Dual-Language Learning**:
> "I understand stacks in Python. Show me the equivalent C++ code and explain the key differences."

**Assessment**:
- Lab in primary language (required)
- Bonus: Submit version in other language with explanation of differences (+5%)

**Pedagogical Benefit**:
Students learn language-agnostic concepts by seeing same structure in different syntax.

---

### AI for Algorithm Analysis

**Pattern for Big O Understanding**:
> "Here's my code: [paste]. What's the time complexity? Walk me through how you determined that."

**Follow-Up Prompts**:
> "Explain why the nested loop makes it O(N²) instead of O(N)."

**Teaching Point**:
AI can explain algorithmic analysis, but students must verify by manual counting.

---

### AI for Debugging Strategy

**Pattern for Learning to Debug**:
> "My linked list insert crashes. Instead of fixing it, explain how I should approach debugging this systematically."

**What We're Teaching**:
- Don't ask AI to fix; ask AI to teach debugging
- Process over solution
- Build debugging skills, not just working code

---

## Semester-Long AI Collaboration Progression

### M01: Basics
- Use AI for definitions and simple explanations
- Learn to write clear questions
- Document conversations

**Success Metric**: Students can explain what a good prompt looks like

---

### M02-M03: Iteration
- Use AI to debug and refine code
- Compare AI's approach to their own
- Learn to evaluate AI responses critically

**Success Metric**: Students show iteration in prompts.txt (not just one prompt per problem)

---

### M04-M05: Translation
- Use AI to see concepts in other language
- Recognize patterns across implementations
- Start teaching AI (explaining context in prompts)

**Success Metric**: Students explain what they taught AI vs. what AI taught them

---

### M06-M08: Independence
- Use AI for advanced exploration
- Combine AI responses with own research
- Know when to ignore AI's suggestions

**Success Metric**: Students demonstrate judgment ("AI suggested X but I chose Y because...")

---

## Assessment Instruments

### Week 2: AI Collaboration Quiz (Formative)
**Format**: Short scenarios, identify good/bad prompts

**Example**:
> Student asks: "Write me a stack class in C++"
> Is this a good prompt? Why or why not?

**Purpose**: Calibrate expectations early

---

### Week 8: Midterm Reflection (Graded)
**Prompt**: 
> "Review your prompts.txt files from M01-M04. Identify:
> 1. Your best prompt (most helpful response)
> 2. Your worst prompt (unhelpful response)
> 3. How your prompting improved over time
> 4. One thing you learned from AI that surprised you"

**Rubric**: Metacognitive depth, specific examples, growth mindset

---

### Week 16: Final Portfolio
**Requirements**:
- All prompts.txt files compiled
- Reflection essay: "What I Learned About Learning with AI"
- Analysis: When was AI helpful? When was it not?

**Grade Weight**: 5% of final grade (part of "participation")

---

## Emergency Procedures

### If a Student Refuses to Use AI

**Diagnosis**: Why?
- Ethical concerns? (Address: "AI is a tool, like a calculator")
- Fear/intimidation? (Offer: Extra support, pairing with AI-comfortable peer)
- Prior bad experience? (Explore: What happened? How can we make it better?)

**Accommodation**:
- Cannot exempt (it's required)
- Can provide extra scaffolding (more templates, more examples)
- Can extend deadlines for AI bootcamp catch-up

**Bottom Line**:
This is a learning objective. We don't waive learning objectives, but we support struggle.

---

### If AI Use Becomes Rampant Copy/Paste

**Signs**:
- Code submissions are overly complex for student level
- Student can't explain basic concepts
- Prompts.txt is suspiciously sparse or generic

**Intervention**:
1. One-on-one code explanation session (not accusatory, exploratory)
2. "Walk me through this function. What's happening on line 14?"
3. If student clearly doesn't understand: Resubmit with explanation or lower grade

**Teaching Moment**:
> "AI collaboration isn't about getting code. It's about understanding code. Let's work together so you can explain this."

---

## Success Stories to Share

### Example 1: The Pointer Breakthrough
> "I kept getting segfaults. I asked Claude to explain what happens in memory when I do `Node* temp = head;`. The visualization it described helped me see where I was losing the reference. Then I drew it on paper and fixed it myself!"

**Lesson**: AI helped understanding, not just fixing

---

### Example 2: The Cross-Language Insight
> "I was stuck on recursion in C++. I asked ChatGPT to show me the same algorithm in Python. Seeing it without pointers helped me understand the logic. Then I went back and implemented it in C++ correctly."

**Lesson**: AI as translation tool

---

### Example 3: The Wrong Answer
> "AI suggested a hash function that was terrible—too many collisions. But when I asked WHY it was bad, AI explained the properties of a good hash function. That taught me more than if it had given me a good function in the first place."

**Lesson**: AI mistakes can be more educational than AI successes

---

## Resources to Provide Students

### Week 1 Handouts
- [ ] AI Collaboration Guide (2-page summary of this document)
- [ ] Prompt Templates by task type
- [ ] Good/Bad Prompt Examples
- [ ] prompts.txt template

### Throughout Semester
- [ ] "Best Prompts" board (student-contributed, updated weekly)
- [ ] "AI Said What?" collection (funny/wrong AI responses)
- [ ] FAQ: Common AI Collaboration Issues

---

## Final Philosophy

**What We're Really Teaching**:
- Critical thinking (evaluating AI responses)
- Communication (formulating clear questions)
- Iteration (refining based on feedback)
- Judgment (knowing when to use/ignore AI)
- Accountability (understanding your code, regardless of origin)

**What We're NOT Teaching**:
- Dependence on AI
- Acceptance of AI as authority
- Treating AI as a black box

**The Goal**:
By the end of CSC 249, students should:
1. Use AI as effectively as a senior developer would
2. Know when AI helps and when it hinders
3. Explain their code confidently, regardless of AI involvement
4. See AI as one tool in their toolkit, not a crutch

---

**AI collaboration is not about making things easier. It's about learning more effectively. This is the future of education. Let's do it right.**
