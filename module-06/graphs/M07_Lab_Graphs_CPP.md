# M07 Lab: Graph Familiarity (C++)
## CSC 249 — Data Structures and Algorithms

---

## Submission

- **Files**: Your `.cpp` file + image of your graph + `prompts.txt`
- **Submit**: GitHub repo link (pull request)
- **Points**: 60
- **AI Use**: ALLOWED — save your prompts!

---

## Overview

In this lab you'll get hands-on with the `Graph` class by running a working demo, then designing and building your own graph.

**Starter files** (provided):
- `Graph.h` — the graph class (vertices, edges, adjacency list)
- `demo_flights.cpp` — a working example that models a flight network

---

## Part 1: Run the Demo (15 points)

### Step 1: Compile and run

```
g++ -std=c++17 demo_flights.cpp -o demo_flights
./demo_flights
```

You should see a flight network with 4 cities and their connections.

### Step 2: Read the code

Open `demo_flights.cpp` and answer these questions in comments at the top of your own file:

1. What does `AddVertex()` return?
2. What's the difference between `AddDirectedEdge()` and `AddUndirectedEdge()`?
3. What does `GetEdgesFrom()` give you? How is that different from `GetEdgesTo()`?
4. What does the edge `weight` represent in this demo?

### Step 3: Add a city

Add a 5th city to the flight demo (pick any real city). Add at least 2 flight connections to existing cities. Compile, run, and verify your new city shows up.

**Deliverable**: Your answers to the 4 questions + the modified demo with your 5th city.

---

## Part 2: Design Your Own Graph (20 points)

### Step 1: Choose a topic

Pick something that can be modeled as a graph. Some ideas:

- **A map** — how you get to school, favorite places in town, a campus map
- **A video game map** — locations from a game you play
- **A family tree** — people as vertices, relationships as edges ("parent of", "sibling of")
- **A character map** — characters from a show, movie, or book with relationships
- **A flowchart** — steps to complete a process, with decision branches
- **A recipe dependency graph** — tasks and what must happen before each one

### Step 2: Sketch it

Before writing any code, draw your graph. You need:

- At least **5 vertices**
- At least **6 edges**
- **Meaningful edge labels** (not just "->")

Ways to make your sketch:
- Draw by hand and photograph it
- Use draw.io, Excalidraw, or any drawing tool
- Ask an AI image tool to generate it
- Screenshot a real map and mark the vertices and edges

### Step 3: Implement it

Create a new file (`my_graph.cpp`) that:

1. Includes `Graph.h`
2. Creates your vertices
3. Creates your edges with descriptive weights
4. Prints all vertices and their connections (model this on the demo)

Decide: are your edges directed or undirected? This depends on your topic. Roads are usually undirected. A flowchart is directed. Family relationships can go either way depending on how you label them.

**Deliverable**: `my_graph.cpp` that compiles and runs + your graph sketch image.

---

## Part 3: Query Your Graph (25 points)

Add the following queries to your `my_graph.cpp`. Print the results.

### Query 1: Neighbor Count
For each vertex, print how many outgoing edges it has.

```cpp
for (Vertex* v : myGraph.GetVertices()) {
    cout << v->label << " has " 
         << myGraph.GetEdgesFrom(v)->size() 
         << " connections" << endl;
}
```

### Query 2: Connection Check
Pick two vertices. Check if a direct edge exists between them. Print the result.

```cpp
cout << "Direct connection? " 
     << (myGraph.HasEdge(vertexA, vertexB) ? "Yes" : "No") << endl;
```

### Query 3: Find by Label
Use `GetVertex()` to look up a vertex by its label string. Print what you find.

```cpp
Vertex* found = myGraph.GetVertex("Kitchen");
if (found) {
    cout << "Found: " << found->label << endl;
} else {
    cout << "Not found!" << endl;
}
```

### Query 4: Edge Summary
Print the total number of vertices and edges in your graph.

```cpp
cout << "Vertices: " << myGraph.GetVertices().size() << endl;
cout << "Edges: " << myGraph.GetEdges().size() << endl;
```

**Deliverable**: All four queries added to your file, producing correct output.

---

## Grading Rubric

| Component | Points |
|-----------|--------|
| Part 1: Demo answers + 5th city added | 15 |
| Part 2: Graph sketch (5+ vertices, 6+ edges, labeled) | 10 |
| Part 2: Working implementation | 10 |
| Part 3: All four queries working correctly | 25 |
| **Total** | **60** |

Bonus (+5): Graph uses a creative or unusual topic with thoughtful edge labels.

---

## Common Mistakes to Avoid

**Wrong**: Forgetting that `GetEdgesFrom()` returns a pointer to a vector — you need `*` to dereference it in a range-for loop.

```cpp
// Wrong: missing the *
for (Edge* e : graph.GetEdgesFrom(v)) { ... }

// Right: dereference the pointer
for (Edge* e : *graph.GetEdgesFrom(v)) { ... }
```

**Wrong**: Using `AddUndirectedEdge()` when your graph should be directed (or vice versa). Think about whether the connection goes both ways.

**Wrong**: Forgetting to print `edge->weight` — the label is the most interesting part of your graph!

---

## AI Assistance Tips

Good prompts for this lab:
- "Explain the difference between an adjacency list and an adjacency matrix"
- "I'm building a graph of [my topic]. What should my vertices and edges be?"
- "Help me understand why `GetEdgesFrom` returns a pointer to a vector"
- "My graph compiles but the output looks wrong — here's what I see: [paste output]"

Save your prompts in `prompts.txt`. This is part of your submission.

---

*CSC 249 — Data Structures | Alamance Community College*
