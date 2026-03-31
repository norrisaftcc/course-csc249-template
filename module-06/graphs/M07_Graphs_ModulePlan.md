# M07 Graphs Module — Development Plan
## CSC 249: Data Structures and Algorithms

---

## Overview

This module introduces graphs as a data structure through a two-part sequence: a short **lab** that builds familiarity with graph vocabulary and API, followed by a **homework** where students build a navigable text-adventure-style system using graph nodes and edges. Both deliverables are available in C++ and Python tracks.

---

## Key Design Decisions

### 1. Unify to String Weights from the Start

Last year's dual-header approach (`Graph.h` with `double` weights vs. `StringGraph.h` with `string` weights) caused confusion. **This year we use string-labeled edges exclusively.** Rationale:

- Strings are more general — distances can be stored as `"6743 miles"`, relationships as `"married to"`, directions as `"north"`
- One graph class, one mental model
- If students need numeric weights for algorithms (Dijkstra, etc.), they parse strings — a useful real-world skill
- Eliminates the "which header do I include?" question entirely

**Action**: Provide a single `Graph.h` (C++) and `graph.py` (Python) with string edge labels.

### 2. Python Graph Implementation

Provide a lightweight `Graph` class in Python that mirrors the C++ API closely enough that students can reason about both. Not networkx — too much abstraction hides the structure. Our class should use:

- `dict` for adjacency (mirrors `unordered_map`)
- Named classes for `Vertex` and `Edge` (mirrors C++ structs)
- Same method names: `add_vertex()`, `add_directed_edge()`, `add_undirected_edge()`, `get_edges_from()`, etc.

This supports dual-language competence: students see the same graph operations in both languages.

### 3. "Create Before Theory" Progression

| Phase | Activity | What Students Build |
|-------|----------|-------------------|
| **Slides** | Visual introduction to graph vocabulary | Mental model |
| **Lab** | Run demo, then build their own small graph | Working graph in code |
| **Homework** | Build a navigable room/location system | Text adventure game |
| **Theory** | BFS, DFS, shortest path (later modules) | Algorithm understanding |

The slides exist to give students just enough vocabulary to be dangerous — not to front-load theory.

### 4. Text Adventure Homework — Framework Approach

The homework asks students to model a physical space (house, campus, dungeon, town) as a graph where rooms are nodes and connections are edges. Edge labels describe directions or transitions.

**C++ approach**: No external library needed. The graph IS the adventure framework. Students write a simple command loop:
```
> look          (show current room + connections)
> go north      (follow edge labeled "north")
> exits         (list available edges from current node)
```

**Python approach**: Two options offered:
1. **Vanilla Python** — Same approach as C++, graph + command loop
2. **adventurelib** (optional enrichment) — Adds a text parser with `@when("go DIRECTION")` decorators. Students who want polish can use it. Not required.

This avoids a mandatory external dependency while giving ambitious students a path to something more impressive.

### 5. AlgoCratic Theme (Light Touch)

The lab and homework can carry a light AlgoCratic flavor:
- Lab: "The Algorithmic Bureau of Transportation needs you to model their flight network..."
- Homework: "Design the floor plan for your assigned AlgoCratic Housing Unit (or rebel and design your dream house instead)"

Students can ignore the theme and make whatever they want. The theme is a wrapper, not a constraint.

---

## Artifact Inventory

### Artifact 1: Slide Deck (HTML/JS)
**Purpose**: Introduce graph vocabulary and concepts visually  
**Content**:
- What is a graph? (nodes + edges, that's it)
- Vocabulary: vertex, edge, directed vs. undirected, weighted, path, cycle
- Real-world examples (maps, social networks, file systems, game worlds)
- ASCII/visual diagrams showing each concept
- The adjacency list representation (how our code stores it)
- Quick preview of the flight demo output
- "What you'll build" teaser for the lab and homework

**Style**: Our usual HTML/JS deck format with dark theme, ASCII diagrams, minimal text per slide.

### Artifact 2: Lab — Graph Familiarity (C++ version)
**Purpose**: Get students hands-on with the graph API  
**Structure**:
1. **Part 1 — Run the Demo**: Compile and run the flight graph. Read the code. Annotate what each section does.
2. **Part 2 — Build Your Own Graph**: Design a graph (draw it first), then implement it in code using the provided `Graph` class.
3. **Part 3 — Query Your Graph**: Write code to answer questions about your graph (find all neighbors, check if edge exists, count edges, etc.)

**Deliverables**: Source code + image/sketch of their graph + prompts.txt  
**Points**: ~50-60 (short lab, not a full assignment)

### Artifact 3: Lab — Graph Familiarity (Python version)
**Purpose**: Same as C++ version, but using Python graph class  
**Notes**: Mirrors C++ lab structure. Python graph class provided. Same exercises, same deliverables.

### Artifact 4: Homework — Navigable System (C++ version)
**Purpose**: Build a text-adventure-style program using graphs  
**Structure**:
1. **Design Phase**: Sketch a map of 6-10 rooms/locations. Label connections with directions or descriptions.
2. **Build Phase**: Implement the map as a graph. Write a game loop that lets the user navigate.
3. **Polish Phase**: Add room descriptions, items, or interactions (stretch goals).

**Required features**:
- At least 6 nodes (rooms/locations)
- At least 8 edges (connections)
- A game loop that displays current location and available exits
- User can navigate by typing a direction/connection name
- Graceful handling of invalid input
- At least one room with a "dead end" (only one exit)
- A clear "you win" or "you've explored everything" condition

**Stretch goals** (bonus points):
- Items you can pick up and carry
- Locked doors that require an item
- A simple puzzle
- ASCII art for rooms
- An NPC that gives hints

**Deliverables**: Source code + map image + prompts.txt + README describing the world  
**Points**: ~100

### Artifact 5: Homework — Navigable System (Python version)
**Purpose**: Same as C++ version  
**Notes**: Uses Python graph class. Optional adventurelib integration documented as enrichment path.

---

## Starter Code Strategy

### C++ — Unified `Graph.h`
Based on the existing `StringGraph.h`, renamed to just `Graph.h`. The `Edge` weight is a `std::string`. Provide:
- `Graph.h` — the graph class
- `main_demo.cpp` — the flight graph demo (for the lab)
- `main_adventure.cpp` — skeleton for the homework (game loop stub)

### Python — `graph.py`
A new file mirroring the C++ API:
```python
class Vertex:
    def __init__(self, label: str): ...

class Edge:
    def __init__(self, from_vertex, to_vertex, weight: str = "->"): ...

class Graph:
    def add_vertex(self, label: str) -> Vertex: ...
    def add_directed_edge(self, from_v, to_v, weight="->") -> Edge: ...
    def add_undirected_edge(self, a, b, weight="->") -> tuple: ...
    def get_edges_from(self, vertex) -> list: ...
    def get_edges_to(self, vertex) -> list: ...
    def get_vertex(self, label: str) -> Vertex: ...
    def get_vertices(self) -> list: ...
    def has_edge(self, from_v, to_v) -> bool: ...
```

Plus:
- `demo_flights.py` — the flight graph demo (for the lab)
- `adventure_starter.py` — skeleton for the homework

---

## Open Questions for Discussion

### Q1: Lab Scope
The lab is intentionally short (one class period). Should Part 3 (querying the graph) be included, or is "run demo + build your own" enough?

### Q2: Homework Room Count
6-10 rooms is the current target. Too few feels trivial; too many becomes tedious. Is this the right range for a homework-sized assignment?

### Q3: adventurelib for Python
Include as optional enrichment, or leave it out entirely to keep both languages parallel? Adding it creates a divergence between the C++ and Python experiences.

### Q4: Shared Graph Class or Separate Files?
Should the homework reuse the same `Graph.h`/`graph.py` from the lab, or should students build their own simplified version? Reusing teaches "library consumer" skills; building teaches internals.

### Q5: Where Does This Sit in the 16-Week Sequence?
Graphs are currently in weeks 9-13 (Hierarchical & Network Structures). This module would likely be weeks 11-12, after trees and before the integration phase. Does that timing still feel right?

---

## Development Order

1. **This conversation**: Finalize the plan (this document)
2. **Next**: Slide deck (establishes vocabulary for everything else)
3. **Then**: Lab assignments (C++ and Python, can be developed in parallel)
4. **Then**: Homework assignments (C++ and Python)
5. **Finally**: Starter code files (Graph.h, graph.py, demo files, skeleton files)

---

*Module plan v1 — ready for review and iteration.*
