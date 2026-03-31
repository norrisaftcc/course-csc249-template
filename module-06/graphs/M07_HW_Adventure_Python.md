# M07 Homework: Navigable World (Python)
## CSC 249 — Data Structures and Algorithms

---

## Submission

- **Files**: `adventure.py`, `graph.py`, map image, `README.md`, `prompts.txt`
- **Submit**: GitHub repo link (pull request)
- **Points**: 100
- **AI Use**: ALLOWED — save your prompts!

---

## The Assignment

Build a text-adventure-style program where a player navigates through a world you design. The world is stored as a **graph**: rooms are vertices, connections are edges, and edge labels are directions.

This is how classic text adventures work — Zork, Colossal Cave Adventure, and the entire MUD genre all stored their worlds as graphs. You're building a small one from scratch.

**Starter files** (provided):
- `graph.py` — the graph class (same one from the lab)
- `adventure.py` — a skeleton with a 3-room example and a working game loop

---

## Phase 1: Design (20 points)

Before you write any code, design your world on paper or in a drawing tool.

### Requirements

- At least **6 rooms/locations** (vertices)
- At least **8 connections** (edges)
- At least **one dead end** (a room with only one exit)
- Every room must be **reachable** from the starting room
- Edge labels must be **direction words** the player will type ("north", "south", "up", "through the door", etc.)

### Choose Your Setting

You can build anything — the graph structure is the same regardless of theme.

- A house or apartment
- A dungeon or cave system
- A spaceship or space station
- A school campus
- A small town
- A forest trail system
- An office building
- Something from a game, book, or show you like

### Deliverable

A map image showing your rooms and connections with labeled edges. This can be:
- A hand-drawn sketch (photograph it)
- A diagram from draw.io, Excalidraw, or similar
- An AI-generated diagram
- A marked-up screenshot

Include this image in your repo.

---

## Phase 2: Build (50 points)

Open `adventure.py` and replace the example `build_world()` function with your own world.

### Required Features

**World construction (20 points)**:
- All your rooms created as vertices
- All connections created as directed edges with direction labels
- Starting room returned correctly
- Remember: if you want two-way connections, add edges in both directions. A hallway you can walk both ways needs `add_directed_edge(room_a, room_b, "north")` AND `add_directed_edge(room_b, room_a, "south")`.

**Room descriptions (10 points)**:
- When the player enters a room or types `look`, show a short description of that room (1-2 sentences)
- You can store descriptions in a dictionary: `descriptions = {"Kitchen": "Copper pots and the smell of cinnamon.", ...}`

**Navigation (10 points)**:
- Player can type a direction to move (e.g., `north`, `go north`)
- Invalid directions produce a clear error message
- The game loop continues until the player types `quit`

**Win/completion condition (10 points)**:
- Define what "winning" means in your world. Some options:
  - Reach a specific room ("You found the exit!")
  - Visit every room ("You've explored the entire map!")
  - Collect items from specific rooms
  - Reach a room within a move limit
- When the condition is met, congratulate the player and end the game (or let them keep exploring)

### Code Quality

- Use meaningful variable names (not `v1, v2, v3`)
- Add comments explaining your world layout
- Keep the code organized — the `build_world()` function should be readable

---

## Phase 3: Polish (10 points)

Add at least **two** of the following to make your world feel more alive:

- **A welcome message** that sets the scene and explains the setting
- **ASCII art** for at least one room
- **A move counter** that tracks how many moves the player has made
- **A "map" command** that lists all rooms and whether they've been visited
- **A "help" command** that reminds the player what they can type
- **Color output** using ANSI escape codes (e.g., `\033[32m` for green) or the `colorama` library

---

## Phase 4: Document (20 points)

### README.md (15 points)

Write a `README.md` that includes:

1. **World description** — What is this place? Why is the player here? (2-3 sentences)
2. **Map overview** — A brief text description of the layout, or reference your map image
3. **How to run** — The exact command needed (`python adventure.py`)
4. **How to win** — What the player should try to do
5. **Design decisions** — Why did you choose directed vs. undirected edges? Did any connections only go one way? Why?

### prompts.txt (5 points)

Save your AI conversations. Focus on documenting:
- How you used AI to help design your world layout
- How you used AI to debug any issues
- Anything interesting you learned from AI about graphs or text adventures

---

## Grading Rubric

| Component | Points |
|-----------|--------|
| **Phase 1: Design** | **20** |
| Map image with 6+ rooms, 8+ edges, labeled | 20 |
| **Phase 2: Build** | **50** |
| World construction (rooms + connections) | 20 |
| Room descriptions | 10 |
| Navigation works correctly | 10 |
| Win/completion condition | 10 |
| **Phase 3: Polish** | **10** |
| Two enhancements from the list | 10 |
| **Phase 4: Document** | **20** |
| README.md with all required sections | 15 |
| prompts.txt | 5 |
| **Total** | **100** |

### Bonus Points (up to +15)

- **Items** (+5): Player can pick up and carry objects. At least 2 items in different rooms.
- **Locked passage** (+5): A connection that requires an item to traverse ("The door is locked. You need a key.")
- **NPC** (+5): A character in one room that says something when you enter or interact.

### Optional Enrichment: adventurelib

If you want a more polished text parser, check out [adventurelib](https://adventurelib.readthedocs.io/). It adds decorator-based command handling:

```python
from adventurelib import when, say

@when("go DIRECTION")
def go(direction):
    # your navigation logic here
    ...

@when("look")
def look_around():
    # your look logic here
    ...
```

This is **not required** — the starter code's game loop works fine. But if you want to experiment with a real text adventure framework, adventurelib is a clean, lightweight option. Install with `pip install adventurelib`.

---

## Tips

**Start small**. Get the skeleton running with the 3-room example first. Make sure you understand how `build_world()`, `look()`, and `try_move()` work before changing anything.

**Build incrementally**. Add one room at a time. Test after each addition. Don't try to build all 6+ rooms at once.

**Think about edge direction**. Not all connections need to be two-way. A ledge you can jump down from but not climb back up = one directed edge. A hallway = two directed edges (one each way). A trap door = directed edge down, no edge back up.

**Use a dictionary for descriptions**. This keeps your `build_world()` function clean:

```python
descriptions = {
    "Kitchen": "Copper pots hang from the ceiling. Smells like cinnamon.",
    "Cellar": "Dark and cold. You hear dripping water.",
    # ... more rooms
}
```

Then in `look()`: `print(descriptions.get(current_room.label, ""))`

**Test edge cases**: What happens when you type gibberish? What happens when you're in the dead-end room? What happens if you type the same direction twice?

---

## Example Session

```
========================================
  Welcome to The Old Farmhouse
  Type a direction to move, or:
    look  - see where you are
    exits - list available exits
    quit  - exit the game
========================================

────────────────────────
You are in the Front Porch.
A creaky wooden porch with a rocking chair.

Exits:
  inside -> Living Room
  around back -> Garden
────────────────────────

> inside

────────────────────────
You are in the Living Room.
Dusty furniture and a grandfather clock that stopped at midnight.

Exits:
  outside -> Front Porch
  upstairs -> Bedroom
  east -> Kitchen
────────────────────────

> go east

────────────────────────
You are in the Kitchen.
Copper pots hang from the ceiling. Something smells faintly of cinnamon.

Exits:
  west -> Living Room
  down -> Cellar
────────────────────────

> down

────────────────────────
You are in the Cellar.
Dark and cold. You hear dripping water.
This is a dead end — the only way out is back up.

Exits:
  up -> Kitchen
────────────────────────

> quit
Thanks for exploring!
```

---

*CSC 249 — Data Structures | Alamance Community College*
