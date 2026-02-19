```
================================================================
    PETRI DISH VISUALIZATION SERIES -- INSTRUCTOR WALKTHROUGH
              CSC 249: Data Structures & Algorithms
================================================================
         __________________________________________
        |                                          |
        |   "Petri Dish: The Complete Walkthrough" |
        |                                          |
        |   Author: Department of Pedagogy         |
        |   Version: 1.0                           |
        |   Last Updated: February 2026            |
        |   Platform: Any Browser + p5.js          |
        |   Difficulty: *** (Instructor Edition)   |
        |__________________________________________|

================================================================
                     TABLE OF CONTENTS
================================================================

  I.    Introduction / Overview ...................... [INTRO]
  II.   Before You Start (Setup & Prereqs) .......... [SETUP]
  III.  Walkthrough: Petri Dish 01 .................. [PD-01]
  IV.   Walkthrough: Petri Dish 02 .................. [PD-02]
  V.    Walkthrough: Petri Dish 03 .................. [PD-03]
  VI.   Walkthrough: Petri Dish 04 .................. [PD-04]
  VII.  Pacing Guide & Time Budgets ................. [PACING]
  VIII. Common Student Questions (FAQ) .............. [FAQ]
  IX.   Grading Tips & Pitfalls .................... [GRADE]
  X.    Secret Endings & Easter Eggs ................ [SECRET]
  XI.   Credits / Acknowledgments ................... [CREDITS]

  Use Ctrl+F and search [TAG] to jump to sections.

================================================================
                I. INTRODUCTION / OVERVIEW             [INTRO]
================================================================

Welcome, instructor. You've unlocked the Petri Dish Visualization
Series. This is a 4-week arc of browser-based labs that teach
Big-O through sparkly neon polygon creatures. Students never see
a formal definition of O(N) before they've watched a counter tick
up N times. That's the whole trick.

THE PITCH (for your syllabus or intro lecture):
  "Over the next four weeks, you'll build an increasingly complex
  ecosystem of digital creatures. Each week adds a new algorithm.
  By the end, you'll have watched sorting, searching, and data
  structures happen in real-time -- and measured their cost."

THE ACTUAL PITCH (for you):
  These are JavaScript visualizations that students can't break
  because they open in a browser. The JS is intentionally simple
  and heavily commented. The real work is in the Python/C++
  appendices and the reflection questions. The sparkly stuff is
  the hook. The appendix code is the protein.

WHY JAVASCRIPT WHEN WE TEACH PYTHON/C++?
  Three reasons:
  1. Zero setup. Students double-click an HTML file.
  2. Visualization requires a canvas. Python doesn't have one
     out of the box. C++ definitely doesn't.
  3. Pedagogically, seeing the same algorithm in THREE languages
     (JS visual, Python text, C++ text) is better than two.
     It forces the student to see the CONCEPT, not the SYNTAX.

  If a student asks "why are we learning JavaScript?" the answer
  is "we're not -- we're learning algorithms. JavaScript is just
  the petri dish they happen to live in."

================================================================
              II. BEFORE YOU START                     [SETUP]
================================================================

INSTRUCTOR SETUP CHECKLIST:
  [ ] Verify all 4 HTML files open in your browser
      - module-01/demo/petri-dish-01-specimen-alpha.html
      - module-02/labs/petri-dish-02-population-census.html
      - module-03/labs/petri-dish-03-classification.html
      - module-04/labs/petri-dish-04-structures.html
  [ ] Verify p5.js loads (requires internet first time, then cached)
  [ ] Have the assignment specs open for reference
  [ ] Know where the appendix Python/C++ code sections are
      (bottom of each HTML, in collapsible <details> elements)
  [ ] If recording a YouTube lecture, have OBS or equivalent ready
      with browser capture

STUDENT PREREQS PER ASSIGNMENT:
  PD-01: Can write a class in Python or C++ (from M01 lecture)
  PD-02: Understands what a list/array is (any prior CS course)
  PD-03: Has completed PD-02 (needs context of linear search)
  PD-04: Has completed PD-03 (needs sorting context); parallels
         the main M04 Stacks/Queues assignment

TECH REQUIREMENTS:
  - A web browser made after 2015 (Chrome, Firefox, Edge, Safari)
  - That's it. That's the whole list.
  - No Node.js. No npm install. No Python environment for the viz.
  - The Python/C++ appendix code runs in whatever the student
    already has set up for the course.

================================================================
           III. WALKTHROUGH: PETRI DISH 01             [PD-01]
           "Specimen Alpha -- Object Observation Lab"
================================================================

>> WEEK OVERVIEW
   Module: M01 (OOP Foundations)
   Points: 100
   In-class time needed: ~30 min demo + discussion
   Student work time: ~2-3 hours outside class
   Difficulty: * (gentle intro)

>> THE SETUP (what to say when you introduce it)

   Open the HTML in your browser, projected for the class. One
   neon polygon creature will be wandering around. Click on it.
   The properties panel lights up.

   SAY THIS:
   "This is a Critter. It's an object. It has state -- look at
   these properties updating in real-time. It has behavior --
   it's wandering, it's avoiding edges. Everything you see is
   defined in a JavaScript class that looks almost identical to
   the Python/C++ class you built last week."

   DO THIS:
   - Change the Speed slider to 0. "What happened? Why?"
   - Change Speed to 5. "And now?"
   - Click "Randomize Value" a few times. "What changes?"
   - Click "Add Specimen" twice. "Watch what happens when they
     get close to each other."

   The students should notice:
   1. Speed 0 = no movement (maxSpeed controls update())
   2. Randomizing value changes size AND shape (sides count)
   3. Multiple critters repel each other (separate() method)

>> PART A: OBSERVATION (20 pts)

   This is pure "look at the thing and describe what you see."
   Students who actually open the code will do better, but even
   students who only interact with the UI can answer these.

   EXPECTED ANSWERS:
   A1 (properties): id, value, pos.x, pos.y, vel.x, vel.y,
       speed, size, sides, wandering, maxSpeed, maxForce.
       Each controls something visible.
   A2 (speed experiment): Speed 0 = critter stops because
       maxSpeed=0 means vel.limit(0) clamps velocity to zero.
   A3 (value mapping): Size (bigger) and sides (more polygon
       sides). A value=10 critter is a small triangle; value=90
       is a large octagon.

   COMMON MISTAKE: Students list "pos.x" and "pos.y" as one
   property "position." Accept this -- they're thinking in the
   right direction.

>> PART B: MODIFICATION (40 pts)

   This is where students open the HTML in a text editor and
   actually change the JavaScript. This is the riskiest part
   pedagogically because students may panic at JavaScript.

   PREEMPTIVE FRAMING:
   "You're not learning JavaScript. You're modifying an existing
   class. Look for the constructor, look for the methods. It
   reads like Python with curly braces."

   B1 (Energy property):
   Students need to add `this.energy = 100` in the constructor,
   `this.energy -= 0.1; if (this.energy <= 0) this.energy = 100;`
   in update(), and modify the shadowBlur/alpha in display() to
   use `this.energy`.

   HINT TO GIVE IF STUCK:
   "Look at how `this.size` is used in display(). Energy should
   affect the glow the same way size affects the polygon."

   B2 (Feed button):
   Students need to add a <button> in the HTML and a function
   that does `if (selectedCritter) selectedCritter.energy = 100;`

   B3 (Trail enhancement):
   The trail already exists. Students need to change strokeWeight
   to use `map(i, 0, this.trail.length, 0.5, 3)` for thickness
   and use the critter's current color for the trail.

>> PART C: APPENDIX TRANSLATION (40 pts)

   The real test. Students take the Critter class and rewrite it
   in Python or C++. The skeleton is in the collapsible appendix.

   KEY TEACHING MOMENT:
   "Notice how the JavaScript Critter and the Python CritterData
   have the same STRUCTURE -- properties in the constructor,
   methods that operate on them. The language is different. The
   concept is identical."

   GOTCHA: Students will try to import p5.js stuff into Python.
   Remind them: "No graphics. Just the data and math."

   The update() method is the hard part. They need:
   - speed = sqrt(vx*vx + vy*vy)
   - if speed > maxSpeed: scale = maxSpeed/speed; vx *= scale; vy *= scale
   - x += vx; y += vy
   - edge wrapping with modulo or conditionals

>> BOSS STRATEGY (common failure modes)

   FAILURE: "The HTML broke and nothing shows up"
   FIX: They probably deleted a closing brace or tag. Tell them
   to open browser DevTools (F12) and look at the Console tab.
   The error message will point to the exact line.

   FAILURE: "My Python program just prints the constructor values"
   FIX: They forgot to call update() in a loop. The skeleton's
   main block has `for _ in range(10): c.update()` -- make sure
   they uncommented it.

   FAILURE: "I don't know JavaScript"
   FIX: "You don't need to. You need to read JavaScript. It's
   Python with {curly braces} and var/let/const instead of
   nothing. Class Critter { constructor() {} } is the same as
   class Critter: def __init__(self)."

================================================================
           IV. WALKTHROUGH: PETRI DISH 02              [PD-02]
           "Population Census -- List & Linear Search"
================================================================

>> WEEK OVERVIEW
   Module: M02 (Algorithm Analysis)
   Points: 100
   In-class time: ~40 min (demo + data collection + discussion)
   Student work time: ~3-4 hours
   Difficulty: ** (introduces measurement)

>> THE SETUP

   This one is best taught as a live data-collection activity.
   Project the HTML. Have students follow along on their own
   laptops.

   SCRIPT:
   "Today we're going to answer a question: how expensive is it
   to build a list? And how expensive is it to search one?"

   "Everyone open Petri Dish 02. Set N to 10. Click Spawn.
   How many operations? Write it down."

   "Now set N to 20. Spawn. Operations? Write it down."

   "N=30. N=40. N=50. Write them all down."

   "Now look at your numbers. What's the pattern?"

   [Students will say "it's the same as N" or "it goes up by 10
   each time." Either answer is correct.]

   "That pattern has a name: O(N). Linear. Double the input,
   double the work."

>> THE SEARCH DEMO (the money moment)

   "Now let's search. Set N to 50 and spawn. Enter a value you
   can see in the dish -- pick one near the end of the list."

   "Click Search. Watch the orange flashes. COUNT THEM."

   Students will see each critter light up orange one by one
   until the target is found (magenta) or all are checked (red).

   "How many comparisons? Was it close to 50? Now search for a
   value that doesn't exist -- try 999."

   "How many comparisons NOW?"

   [Always 50. The whole list. Worst case.]

   "What if I told you there's a search that only needs 6
   comparisons for 50 items? That's next week."

   [This creates anticipation for PD-03. Use it.]

>> PART A: LIST CONSTRUCTION (25 pts)

   Straightforward data collection. The only question that trips
   students up is A3: "Is there a best/worst case for list
   building?" The answer is NO -- building always takes exactly
   N operations regardless of the data. This is unusual because
   most algorithms DO have best/worst cases, so students expect
   one here.

>> PART B: LINEAR SEARCH (25 pts)

   The key insight is worst case = N (not found), best case = 1
   (first element), average = N/2. Students often write "O(N/2)"
   for average case. Gently correct: "In Big-O, we drop
   constants. O(N/2) is O(N). The 1/2 doesn't matter when N is
   a million."

>> PART C: CODE MODIFICATION (25 pts)

   The "best match" feature is a sneaky way to introduce the
   concept of tracking state during iteration. Students need a
   variable that updates as they scan -- this is the precursor
   to the "current minimum" variable in selection sort next week.

   HINT: "It's like finding the tallest person in a room. You
   keep track of the tallest you've seen SO FAR."

>> PART D: APPENDIX (25 pts)

   The Python/C++ code is straightforward. The main challenge is
   getting the experiment runner to print a formatted table.
   Students who struggle with f-strings or cout formatting --
   this is a good time to show them.

>> BOSS STRATEGY

   FAILURE: "My graph is empty"
   FIX: The graph only populates after experiments are logged.
   They need to actually click Spawn and Search, not just
   look at it.

   FAILURE: "Linear search found my value in 3 comparisons,
   that's not O(N)!"
   FIX: "O(N) is the WORST case. You got lucky. Search for a
   value that doesn't exist. How many comparisons now?"

================================================================
           V. WALKTHROUGH: PETRI DISH 03               [PD-03]
           "Classification Protocol -- Sort & Binary Search"
================================================================

>> WEEK OVERVIEW
   Module: M03 (Arrays and Sorting)
   Points: 100
   In-class time: ~50 min (this one needs more live demo time)
   Student work time: ~4-5 hours (hardest of the four)
   Difficulty: *** (two algorithms + comparison)

>> THE SETUP

   This is the climax of the series. Two big reveals:
   1. Sorting is EXPENSIVE (O(N^2))
   2. Binary search is CHEAP (O(log N)) but only works on
      sorted data

   SCRIPT:
   "Last week we searched a list in O(N) time. Today I'm going
   to show you a search that takes O(log N) time. For 1000
   items, that's 10 comparisons instead of 1000. But there's
   a catch."

   [Spawn 30 critters. Click Selection Sort.]

   "Watch the orange flashes. Each one is a comparison. The
   algorithm is scanning for the minimum value, then putting it
   in position. How many comparisons for 30 items?"

   [Answer: 435. Students will be surprised it's so many.]

   "That's N*(N-1)/2 = 30*29/2 = 435. That's O(N^2). Quadratic.
   For 1000 items, it would be about 500,000 comparisons."

   [After sorting completes, critters line up in a neat row.]

   "Now watch binary search."

   [Search for a value. The search checks the middle, dims half
   the critters, checks the new middle, dims half again...]

   "Count the comparisons. For 30 items?"

   [~5. Students will audibly react to the difference.]

   "435 to sort. 5 to search. Was the sorting worth it?"

   [This is THE question. Let them discuss. The answer: it
   depends on how many times you search.]

>> CRITICAL TEACHING MOMENT: THE TRADEOFF

   This is where Big-O becomes PRACTICAL, not just theoretical.

   Write on the board / type in chat:
   - Sort once: O(N^2)
   - Then search K times: K * O(log N)
   - Total: O(N^2) + K * O(log N)

   vs.

   - Linear search K times: K * O(N)
   - Total: K * O(N)

   "For K=1 (one search), linear wins. For K=100, sort+binary
   wins by a landslide. The BREAKEVEN is roughly when
   K * N > N^2, or K > N."

   Students don't need to memorize this formula. They need to
   FEEL it: "sorting is an investment that pays dividends."

>> PART C: INSERTION SORT (25 pts)

   This is the hardest modification in the series. Students need
   to implement a second sorting algorithm with the same visual
   animation pattern. The key difference:

   Selection sort: find minimum, swap to front
   Insertion sort: take next element, slide it left until placed

   HINT FOR STUDENTS:
   "Selection sort SCANS the whole unsorted part each time.
   Insertion sort SHIFTS elements to make room. Think of
   sorting playing cards in your hand."

   EXPECTED DISCOVERY: Insertion sort does fewer comparisons
   on nearly-sorted data. This is a preview of why we'll learn
   multiple sorting algorithms -- different ones are better for
   different situations.

>> BOSS STRATEGY

   FAILURE: "Binary search gives wrong results"
   FIX: Binary search only works on SORTED data. If they skipped
   the sort step, the search will fail randomly.

   FAILURE: "My insertion sort doesn't animate"
   FIX: They probably implemented it as a regular function that
   runs instantly instead of as a state machine that advances one
   step per frame. Point them at the selection sort state machine
   code as a template.

   FAILURE: "Why is selection sort always the same number of
   comparisons regardless of the data?"
   FIX: Good question! Selection sort's inner loop always runs
   fully. It doesn't short-circuit. "That's actually a WEAKNESS.
   Insertion sort CAN short-circuit on sorted data."

================================================================
           VI. WALKTHROUGH: PETRI DISH 04              [PD-04]
           "Organizational Structures -- Stack/Queue/BST"
================================================================

>> WEEK OVERVIEW
   Module: M04 (Linear Structures)
   Points: 100
   In-class time: ~40 min
   Student work time: ~3-4 hours
   Difficulty: ** (conceptually dense but less code modification)

>> THE SETUP

   Three panels. Same critters. Different structures. This one
   teaches itself if you let it.

   SCRIPT:
   "Generate 10 specimens. Now push all 10 onto the stack.
   Now pop 5. Write down the order they came out."

   "Reset. Generate the same 10. Enqueue all 10 into the queue.
   Dequeue 5. Write down the order."

   "Compare your two lists. What's different?"

   [Stack: reverse order. Queue: same order. This is the entire
   lesson. LIFO vs FIFO, demonstrated in 2 minutes.]

>> THE BST REVEAL

   "Now for the tree. Generate 10 random specimens and insert
   them all into the BST. Notice how each one goes left or
   right based on its value. Search for something."

   [The search path lights up -- students see it going
   left/right at each node.]

   "Now click 'Insert 1-10 (sorted)'. Watch the tree shape."

   [It becomes a straight line going right. A linked list.]

   "Search for 100 now. How many comparisons?"

   [10. The same as the list length. O(N).]

   "THAT is why balanced trees matter. This degenerate tree is
   the worst case. A balanced tree would give us O(log N)."

   [You don't need to teach AVL trees here. Just plant the seed
   that "tree shape matters." They'll encounter it in M06.]

>> THE PARALLEL WITH M04 MAIN ASSIGNMENT

   PD-04 runs the SAME WEEK as the main M04 Stacks/Queues
   assignment. The visualization shows them WHAT stacks and
   queues do; the main assignment makes them BUILD one.

   RECOMMENDED SEQUENCE:
   Day 1: Introduce PD-04 in class (live demo, 20 min)
   Day 2: Students work on PD-04 reflection questions
   Day 3: Students implement Stack/Queue in Python/C++
          (from the main M04 assignment spec)
   Day 4: Students complete the BST section and appendix code

>> BOSS STRATEGY

   FAILURE: "The BST search prompt() popup is ugly"
   FIX: Yes it is. It's a prompt(). If a student wants to
   replace it with a text input, give them bonus vibes. The
   prompt is intentionally low-tech to keep the JS simple.

   FAILURE: "I don't understand why the degenerate tree is bad"
   FIX: "Count. How many nodes did you visit to find 100?
   All 10. That's linear search wearing a tree costume.
   A balanced tree would only visit 3-4."

================================================================
           VII. PACING GUIDE & TIME BUDGETS            [PACING]
================================================================

RECOMMENDED 4-WEEK SCHEDULE:

Week 1 (M01): Petri Dish 01 -- Specimen Alpha
  Mon: M01 lecture (OOP concepts, Course class)
  Wed: PD-01 live demo (20 min) + lab time
  Fri: Due: PD-01 submission
  Notes: This week is gentle. Students are getting used to
         the format and the AlgoCratic theme.

Week 2 (M02): Petri Dish 02 -- Population Census
  Mon: M02 lecture (Big-O intro, what is "cost"?)
  Wed: PD-02 live data-collection activity (40 min in class)
  Fri: Due: PD-02 submission
  Notes: The in-class data collection is critical. Don't skip
         it. Students measuring things together builds buy-in.

Week 3 (M03): Petri Dish 03 -- Classification Protocol
  Mon: M03 lecture (sorting concepts, selection sort)
  Wed: PD-03 live sort demo (30 min) + binary search reveal
  Fri: Due: PD-03 submission (may need weekend extension)
  Notes: This is the hardest week. The insertion sort
         modification is substantial. Consider making it
         extra credit if your students are struggling.

Week 4 (M04): Petri Dish 04 -- Organizational Structures
  Mon: M04 lecture (stacks/queues concepts)
  Wed: PD-04 live demo (20 min) + main M04 assignment intro
  Fri: Due: PD-04 + M04 main assignment
  Notes: Two assignments due simultaneously. PD-04 is lighter
         on code modification to compensate. The reflection
         questions are the bulk of the work.

TOTAL INSTRUCTOR PREP TIME: ~2 hours per week
  - 30 min: Open HTML, review the assignment spec
  - 30 min: Prepare talking points for live demo
  - 30 min: Review student submissions (automated via rubric)
  - 30 min: Buffer for questions and troubleshooting

================================================================
           VIII. COMMON STUDENT QUESTIONS               [FAQ]
================================================================

Q: "Why can't I just use sort() and call it a day?"
A: "You CAN. But this course is about understanding what
   sort() DOES. When you know what's inside the black box,
   you know when to use which box."

Q: "Will JavaScript be on the test?"
A: "No. JavaScript is the delivery vehicle. The algorithms
   are the cargo. Your Python/C++ implementation is what
   gets graded for correctness."

Q: "Why does the visual look like a retro arcade game?"
A: "Because retro arcade games are cool and make you want
   to stare at the screen. That's called engagement."
   [Real answer: high-contrast neon on black is readable on
   projectors, streams, and cheap laptop screens. The mono
   font is accessible. The aesthetic is functional.]

Q: "Can I use ChatGPT/Claude for the JavaScript modifications?"
A: "Yes, with documentation. Same AI collaboration policy as
   every other assignment. Log what you asked, what it gave
   you, and what you changed. The appendix Python/C++ code
   must be your own implementation, though. That's the test."

Q: "I'm a C++ student. Do I have to write Python too?"
A: "No. Pick one. The appendix has both skeletons. Choose
   your weapon."

Q: "The critters are kinda cute. Can I make them do [X]?"
A: "That's the extension challenge spirit. If you have time
   after the required parts, go wild. Document what you added."

Q: "Binary search is O(log N). What's 'log'?"
A: "How many times can you cut something in half before it
   disappears? That's log base 2. For 1000 items: 10 cuts.
   For a million: 20 cuts. Logarithms grow INCREDIBLY slowly.
   That's why binary search is so fast."

================================================================
           IX. GRADING TIPS & PITFALLS                 [GRADE]
================================================================

RUBRIC FILES ARE IN:
  module-01/rubrics/petri-dish-01-rubric.yaml
  module-02/rubrics/petri-dish-02-rubric.yaml
  module-03/rubrics/petri-dish-03-rubric.yaml
  module-04/rubrics/petri-dish-04-rubric.yaml

GRADING PRIORITIES (what actually matters):

  1. REFLECTION QUALITY > CODE QUALITY
     A student who writes a thoughtful reflection about why
     binary search is O(log N) but has a slightly buggy
     implementation should score higher than a student with
     perfect code and "idk it's fast" in their reflection.

  2. APPENDIX CODE > HTML MODIFICATIONS
     The Python/C++ translation is the actual learning. The
     HTML modifications are fun but less pedagogically critical.
     If you need to cut a Part for time pressure, cut Part B
     (HTML modification) before Part C (appendix translation).

  3. MEASUREMENT DATA > MEMORIZED ANSWERS
     If a student's data table shows they actually ran the
     experiments, they get the points even if their Big-O
     notation is slightly wrong. "Operations = N" is worth
     almost as much as "O(N)" -- they demonstrated the concept.

PITFALL: Don't dock points for JavaScript style.
  Students are not JS developers. `var` instead of `let`?
  Fine. Missing semicolons? JavaScript doesn't care and
  neither should you. The appendix Python/C++ is where you
  enforce language conventions.

PITFALL: The BST "degenerate tree" question.
  Some students will say "the sorted tree is O(log N) because
  it's a tree." They're wrong but they're reasoning from
  structure, which shows sophistication. Guide them: "Count
  the actual comparisons. Does the data match O(log N)?"

================================================================
           X. SECRET ENDINGS & EASTER EGGS             [SECRET]
================================================================

These are not in the assignment specs. They're for instructors
who want to add extra flair or surprise students.

SECRET 1: THE SPEED RUN
  Challenge: "Who can sort 50 critters in the fewest TOTAL
  operations (comparisons + swaps)?" Run this as a friendly
  competition. Students who implement insertion sort on
  nearly-sorted data will win. This teaches algorithm
  selection through competition.

SECRET 2: THE EXISTENTIAL CRISIS
  In PD-01, if a student sets maxSpeed to 0 and maxForce to 0,
  the critter just... sits there. Inert. It still has state but
  no behavior. "Is an object with no behavior still an object?"
  This is a great discussion prompt for the OOP philosophy unit.

SECRET 3: THE DEGENERATE SPEEDRUN
  In PD-04, insert values 1-100 into the BST. Then search for
  100. The path is 100 comparisons. Show this, then ask: "What
  order would you insert to get the SHORTEST tree?" Answer: 50,
  25, 75, 12, 37, 62, 87... (binary subdivision). This previews
  balanced BST insertion, covered in M06.

SECRET 4: THE EXISTENTIAL SORT
  In PD-03, sort 50 critters by value. Then spawn a new batch
  of 50 and sort again. The second sort has different comparison
  and swap counts. "Wait, selection sort is supposed to always
  be N(N-1)/2 comparisons!" It is. The comparisons ARE the same.
  But the swaps differ because different data has different
  numbers of out-of-place elements.

SECRET 5: FLOCKING BEHAVIOR
  In PD-01, add 20+ critters. They form loose clusters because
  of the separation behavior. Ask: "These critters only have
  a 'stay away from neighbors' rule. Why do they form groups?"
  Answer: edge wrapping + separation creates emergent clustering.
  This is a hook for the graphs module (M07) where we study
  connected components.

================================================================
           XI. CREDITS / ACKNOWLEDGMENTS               [CREDITS]
================================================================

The Petri Dish Visualization Series was developed for CSC 249:
Data Structures and Algorithms.

Built with:
  - p5.js (Processing for the web)
  - Courier New (the one true monospace font)
  - An unreasonable amount of neon cyan (#00fff5)

Pedagogical approach:
  - "Bloom's Taxonomy Starts with Create"
  - The Rippetoe Principle: do it, feel it, fix it, understand it
  - Mandatory AI collaboration with documentation requirements

Special thanks to:
  - The Algorithm (for its infinite wisdom and compliance metrics)
  - The Department of Biological Observation (for specimen care)
  - The Department of Efficiency Metrics (for counting everything)
  - The Department of Citizen Classification (for imposing order)
  - The Department of Task Processing (for organizational structure)

================================================================
        This document is INSTRUCTOR-ONLY. Do not distribute
        to students unless you want them to see the answers.
        (But honestly, if they find it, they earned it.)
================================================================
     This walkthrough is best viewed in a fixed-width font.
               GameFAQs wouldn't have it any other way.
================================================================
```
