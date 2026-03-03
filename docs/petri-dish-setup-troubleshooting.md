# Petri Dish Lab Series: Setup & Troubleshooting Guide

**CSC 249 -- Data Structures & Algorithms**
*For students, TAs, and instructors dealing with the inevitable "it doesn't work on my computer" emails.*

---

## System Requirements

### Minimum
- A modern web browser (Chrome, Firefox, Edge, Safari -- any version from 2020+)
- A text editor for Python/C++ code
- Python 3.8+ or g++ (for appendix translations)

### That's It
No install. No npm. No build step. No Docker. No environment variables.
The HTML files are self-contained. They load p5.js from a CDN.

---

## Setup Instructions

### Step 1: Get the Files

**If using Git (recommended):**
```bash
git clone [repository-url]
cd course-csc249-template
```

**If downloading manually:**
Download the repository as a ZIP and extract it.

### Step 2: Open the Lab

Navigate to the correct module folder and double-click the HTML file:

| Lab | Path |
|-----|------|
| PD-01 | `module-01/demo/petri-dish-01-specimen-alpha.html` |
| PD-02 | `module-02/labs/petri-dish-02-population-census.html` |
| PD-03 | `module-03/labs/petri-dish-03-classification.html` |
| PD-04 | `module-04/labs/petri-dish-04-structures.html` |

### Step 3: Verify It Works

You should see:
- A dark background with a faint grid
- Neon-colored controls (cyan, magenta, green)
- The title of the lab at the top
- Critter(s) or a "Generate" button

If you see a blank white page, see Troubleshooting below.

---

## Troubleshooting

### Problem: Blank white page

**Cause:** The browser can't load p5.js from the CDN.

**Fix:** Check your internet connection. The HTML files load p5.js from `https://cdnjs.cloudflare.com/ajax/libs/p5.js/1.9.0/p5.min.js`. You need internet access the first time (after that, your browser cache may help).

**Offline workaround:** Download `p5.min.js` from [p5js.org](https://p5js.org/download/) and place it next to the HTML file. Then edit line ~4 of the HTML to change:
```html
<script src="https://cdnjs.cloudflare.com/ajax/libs/p5.js/1.9.0/p5.min.js"></script>
```
to:
```html
<script src="p5.min.js"></script>
```

### Problem: Critters don't move

**Check:** Is the speed slider set to 0? Move it up.

**Check:** Did you click a button that pauses animation (like starting a sort)? Some operations pause free movement while the algorithm runs.

### Problem: Canvas is cut off or too small

**Fix:** Zoom out in your browser (Ctrl/Cmd + minus). The canvas is 800x500px for PD-01 through PD-03. PD-04 uses a wider layout for three panels.

**Fix:** If on a small screen (< 800px wide), try landscape mode or a larger display.

### Problem: Buttons don't respond

**Check:** Open the browser console (F12 or Ctrl/Cmd+Shift+J) and look for red error messages.

**Common cause:** An ad blocker or privacy extension is blocking the CDN script. Whitelist `cdnjs.cloudflare.com` or temporarily disable the extension.

### Problem: "p5 is not defined" in console

**Cause:** p5.js failed to load. Same as "blank white page" -- check internet or use the offline workaround above.

### Problem: Sort/search animation is too fast or too slow

**Fix:** Use the speed/delay slider. Lower values = faster animation. If you want to see every single step, set the delay high. If you just want results, set it low.

### Problem: Numbers seem wrong (comparisons don't match expected)

**Fix:** Always click **Reset** before starting a new experiment. Previous state carries over. For clean data:
1. Click Reset (or Reset All)
2. Generate fresh critters
3. Run your experiment
4. Record the numbers

### Problem: Can't find the Python/C++ appendix code

**Fix:** Scroll down below the canvas area. Look for collapsible sections labeled "Python Appendix" and "C++ Appendix". Click the header to expand them.

### Problem: Python appendix code won't run

**Check:** Are you using Python 3? Run with `python3` not `python`.

**Check:** Did you fill in all the `TODO` comments? The skeleton code has placeholder functions that need your implementation.

**Common error:** `IndentationError` -- Python is picky about spaces vs tabs. Use consistent indentation (4 spaces recommended).

### Problem: C++ appendix code won't compile

**Check:** Use `g++ -std=c++17 -o program critter_XX.cpp` (the `-std=c++17` flag enables modern features).

**Check on Mac:** Make sure Xcode command line tools are installed: `xcode-select --install`

**Check on Windows:** Make sure MinGW or WSL is set up for g++.

### Problem: PD-04 BST tree goes off-screen

This is expected with sorted insertions! The degenerate tree is intentionally ugly -- it's a straight line going right and down. That's the teaching point: sorted insertions create an unbalanced tree.

For the random-insert tree, if it still goes off-screen, you may have too many nodes. Stick to 10-15 for the best visual.

---

## Browser-Specific Notes

### Chrome (Recommended)
Works out of the box. Best DevTools for debugging if needed.

### Firefox
Works great. Canvas rendering may look slightly different (anti-aliasing).

### Safari
Works, but:
- "Prevent cross-site tracking" may block the CDN. If so, go to Safari > Settings > Privacy and uncheck it, or use the offline workaround.
- Canvas glow effects (shadowBlur) render slightly differently.

### Edge
Works. It's Chromium-based, so same behavior as Chrome.

### Internet Explorer
No. Just... no.

---

## For Instructors / TAs

### Quick Validation Check

To verify all 4 labs work before distributing to students:

```bash
# Open all 4 in your default browser
open module-01/demo/petri-dish-01-specimen-alpha.html
open module-02/labs/petri-dish-02-population-census.html
open module-03/labs/petri-dish-03-classification.html
open module-04/labs/petri-dish-04-structures.html
```

For each, verify:
1. Canvas renders (dark background, grid visible)
2. At least one button works (generate/add critter)
3. Critters appear and animate
4. Appendix sections expand when clicked

### Expected Student Questions (and Answers)

**"Do I need to know JavaScript?"**
No. You observe the JavaScript visualization and implement in Python or C++. The JS is provided -- you don't write or modify it (except in PD-01 Part B and PD-03 Part C where modifications are explicitly guided).

**"Can I use a different sorting algorithm for PD-03?"**
Part C asks for insertion sort specifically. If you want to add others for extra exploration, go for it, but insertion sort is required.

**"Do I need both Python AND C++?"**
No. Pick one. The appendix provides skeletons for both. Choose whichever you're more comfortable with.

**"Can I modify the HTML?"**
PD-01 Part B and PD-03 Part C specifically ask you to. For PD-02 and PD-04, the HTML is observation-only (unmodified is fine).

**"The random numbers are different every time. Is that OK?"**
Yes. The visualizations use random values. Your specific numbers will differ from classmates'. The patterns (O(N), O(N^2), O(log N)) will be the same.

### Grading the Appendix Code

Run each student's Python/C++ file. Expected output format:

**PD-02 expected output:**
```
Building population of 10: 10 operations
Building population of 50: 50 operations
Linear search (found): X comparisons
Linear search (not found): N comparisons
```

**PD-03 expected output:**
```
Selection sort (N=10): 45 comparisons, X swaps
Selection sort (N=50): 1225 comparisons, X swaps
Linear search (N=50, worst): 50 comparisons
Binary search (N=50, worst): 6 comparisons
```

**PD-04 expected output:**
```
Stack: push 1,2,3,4,5 -> pop 5,4,3,2,1 (LIFO confirmed)
Queue: enqueue 1,2,3,4,5 -> dequeue 1,2,3,4,5 (FIFO confirmed)
BST (balanced): search for 40 took 3 comparisons
BST (degenerate): search for 100 took 10 comparisons
```

Swap counts in selection sort vary by data. Comparison counts should be deterministic (N*(N-1)/2 for selection sort).

---

## Offline Mode (No Internet)

If students need to work without internet (flight, rural area, etc.):

1. Download `p5.min.js` from https://p5js.org/download/
2. Place it in each module's lab folder next to the HTML file
3. Edit each HTML file's `<script>` tag to use the local path:
   ```html
   <script src="p5.min.js"></script>
   ```
4. Everything else works identically -- no other external dependencies

---

## File Integrity Check

If something seems broken, verify the files haven't been corrupted:

```bash
# Count lines in each HTML (approximate expected counts)
wc -l module-01/demo/petri-dish-01-specimen-alpha.html    # ~700-750
wc -l module-02/labs/petri-dish-02-population-census.html  # ~900-1000
wc -l module-03/labs/petri-dish-03-classification.html     # ~800-900
wc -l module-04/labs/petri-dish-04-structures.html         # ~1000-1100
```

Each file should start with `<!DOCTYPE html>` and end with `</html>`.

---

*If none of the above fixes your issue, take a screenshot of the problem (including the browser console if possible) and email it to your instructor. The Algorithm cannot process vague descriptions of technical difficulties.*
