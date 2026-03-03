# CSC 249 Module 01: Specimen Alpha
## "Object Observation Lab"

---

## Assignment Overview

| | |
|---|---|
| **Module** | M01: OOP Foundations |
| **Series** | Petri Dish 1 of 4 |
| **Duration** | 1 week |
| **Points** | 100 total |
| **Language** | JavaScript (observation) + Python or C++ (translation) |
| **Deliverable** | 1 Pull Request |

---

## The Scenario

> **MEMO -- DEPARTMENT OF BIOLOGICAL OBSERVATION**
>
> Employee,
>
> The Algorithm has detected unclassified life forms in Petri Dish Sector 7. You are assigned to observe, document, and modify specimen behavior.
>
> Each specimen is an *object* with *state* (what it is) and *behavior* (what it does). Your compliance rating depends on demonstrating understanding of specimen internals.
>
> -- Department of Biological Observation

---

## What You're Learning

This lab introduces **objects** through direct observation. Instead of reading about OOP, you'll watch a living object and describe what you see. The JavaScript `Critter` class in the petri dish has the same structure as the `Course` class from Module 1 -- properties (state) and methods (behavior) bundled together.

**Key concepts:**
- Objects have **state** (data stored in properties)
- Objects have **behavior** (actions performed by methods)
- Changing a property can affect multiple aspects of the object
- Objects can interact with each other (separation behavior)

---

## Getting Started

1. Open `petri-dish-01-specimen-alpha.html` in your browser
2. You'll see a neon creature wandering in the petri dish
3. Click on it to select it and see its properties in real-time
4. Experiment with the controls: add specimens, change sliders, toggle wandering

---

## Part A: Observation (20 points)

Observe the specimen and answer these questions in a file called `REFLECTION.md`:

### A1. Property Inventory (8 pts)
List all the properties of a Critter object visible in the Properties panel. For each property, describe in one sentence what it controls visually or behaviorally.

### A2. Behavior Experiment (6 pts)
Set the Speed slider to 0. What happens to the specimen? Now set it to 5. What changes? Explain what the `maxSpeed` property controls in the `update()` method by reading the JavaScript code in the HTML file.

### A3. Value Mapping (6 pts)
Select a specimen and click "Randomize Value" several times. What **two visual properties** change when `value` changes? Why does a Critter with `value=10` look different from one with `value=90`?

---

## Part B: Modification (40 points)

Open the HTML file in a text editor. You'll modify the JavaScript `Critter` class.

### B1. Energy Property (20 pts)
Add a new property called `energy`:
- Starts at `100` in the constructor
- Decreases by `0.1` every frame in `update()`
- When energy reaches 0, it wraps back to 100
- Display energy as the **opacity of the glow** (full energy = bright glow, empty = dim)
- Add the energy value to the properties panel display

### B2. Feed Button (8 pts)
Add a "Feed Specimen" button to the controls panel that:
- Resets the selected critter's energy to 100
- Only works if a specimen is selected

### B3. Trail Enhancement (12 pts)
The trail feature is already partially implemented. Improve it:
- Make the trail **color fade** from bright to transparent (it already does alpha fading -- make the trail thicker near the critter and thinner at the tail)
- The trail should use the critter's color (cyan for normal, magenta for selected)

---

## Part C: Appendix Translation (40 points)

The HTML file contains collapsible Python and C++ skeleton code at the bottom. Your task: complete the skeleton in **your chosen language** (Python or C++).

### Requirements (same for both languages)

1. **Complete the TODOs** in the skeleton:
   - Add `size` and `sides` properties derived from `value`
   - Implement `set_value()` / `setValue()` to also update size and sides
   - Implement `update()` with velocity limiting, position update, and edge wrapping

2. **The program must run and produce output** showing:
   - A critter created with value 50
   - That critter after `setValue(90)` (size and sides should change)
   - That critter after 10 update() calls (position should change)

### Python Submission
```
critter.py
```

### C++ Submission
```
critter.cpp
```

---

## Grading Rubric

### Part A: Observation (20 points)

| Criteria | Points |
|----------|--------|
| All properties listed with accurate descriptions | 8 |
| Speed experiment described correctly, update() explained | 6 |
| Both visual mappings (size + sides) identified and explained | 6 |

### Part B: Modification (40 points)

| Criteria | Points |
|----------|--------|
| Energy property decreases over time, wraps at 0 | 10 |
| Glow opacity maps to energy level | 10 |
| Feed button works correctly | 8 |
| Trail thickness fades, uses correct color | 12 |

### Part C: Translation (40 points)

| Criteria | Points |
|----------|--------|
| Size and sides properties implemented, derived from value | 10 |
| set_value updates derived properties | 10 |
| update() implements velocity limiting + position + wrapping | 15 |
| Program runs and produces correct output | 5 |

---

## Submission

### File Structure

```
module-01-specimen-alpha-yourname/
├── petri-dish-01-specimen-alpha.html  (your modified version)
├── critter.py (or critter.cpp)
├── REFLECTION.md
└── sample_output.txt (copy of your program's output)
```

### Pull Request

- **Branch:** `module-01-specimen-alpha-yourname`
- **Title:** `Module 01 Specimen Alpha - [Your Name]`
- **Include:** All files above

---

## Testing Checklist

- [ ] HTML opens in browser without errors
- [ ] Critters wander, wrap around edges, separate from each other
- [ ] Properties panel updates in real-time for selected critter
- [ ] Energy decreases and affects glow brightness
- [ ] Feed button resets energy
- [ ] Trail has thickness gradient
- [ ] Python/C++ program compiles and runs
- [ ] Output shows value change affecting size and sides
- [ ] Output shows position changing after updates

---

## Tips

### Common Mistakes
- Forgetting to call `updateDerived()` after changing `value`
- Energy going negative instead of wrapping to 100
- Trail drawing outside the `push()`/`pop()` transform block

### AI Prompting Ideas
Good prompts for this assignment:
- "Explain what createVector() does in p5.js compared to storing x,y separately"
- "What does velocity.limit(maxSpeed) do in terms of vector math?"
- "How do I map a value from one range to another in Python?"
- "What's the C++ equivalent of Python's random.uniform()?"

---

## Connection to Course

This is **Petri Dish 1 of 4**. The Critter class you're studying here will appear in all four labs:

1. **Specimen Alpha** (this lab) -- understand objects
2. **Population Census** -- build lists of critters, measure search cost
3. **Classification Protocol** -- sort critters, compare search algorithms
4. **Organizational Structures** -- organize critters into stacks, queues, trees

The JavaScript visualization shows you the *concept*. The Python/C++ translation makes you *implement* it.

---

*The Algorithm thanks you for your diligent observation of Sector 7 specimens.*
