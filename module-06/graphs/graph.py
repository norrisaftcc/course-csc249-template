"""
graph.py — CSC 249 Graph Class

Edge weights are strings for maximum flexibility:
    "6743 miles"  for distances
    "north"       for directions  
    "married to"  for relationships

Usage:
    from graph import Graph
    g = Graph()
    kitchen = g.add_vertex("Kitchen")
    hallway = g.add_vertex("Hallway")
    g.add_directed_edge(kitchen, hallway, "north")
    g.add_directed_edge(hallway, kitchen, "south")
"""


class Vertex:
    """A node in the graph with a string label."""
    
    def __init__(self, label: str):
        self.label = label
    
    def __repr__(self):
        return f"Vertex('{self.label}')"


class Edge:
    """A connection between two vertices with a string weight/label."""
    
    def __init__(self, from_vertex: Vertex, to_vertex: Vertex, weight: str = "->"):
        self.from_vertex = from_vertex
        self.to_vertex = to_vertex
        self.weight = weight
    
    def __repr__(self):
        return f"Edge({self.from_vertex.label} --[{self.weight}]--> {self.to_vertex.label})"


class Graph:
    """
    A graph stored as an adjacency list.
    
    Internally uses two dictionaries:
        from_edges: vertex -> list of edges leaving that vertex
        to_edges:   vertex -> list of edges arriving at that vertex
    """
    
    def __init__(self):
        self._from_edges: dict[Vertex, list[Edge]] = {}
        self._to_edges: dict[Vertex, list[Edge]] = {}
    
    def add_vertex(self, label: str) -> Vertex:
        """Add a new vertex with the given label. Returns the Vertex."""
        new_vertex = Vertex(label)
        self._from_edges[new_vertex] = []
        self._to_edges[new_vertex] = []
        return new_vertex
    
    def add_directed_edge(self, from_vertex: Vertex, to_vertex: Vertex, 
                          weight: str = "->") -> Edge | None:
        """Add a one-way edge. Returns the Edge, or None if it already exists."""
        if self.has_edge(from_vertex, to_vertex):
            return None
        new_edge = Edge(from_vertex, to_vertex, weight)
        self._from_edges[from_vertex].append(new_edge)
        self._to_edges[to_vertex].append(new_edge)
        return new_edge
    
    def add_undirected_edge(self, vertex_a: Vertex, vertex_b: Vertex, 
                            weight: str = "->") -> tuple[Edge | None, Edge | None]:
        """Add a two-way edge (creates two directed edges)."""
        return (
            self.add_directed_edge(vertex_a, vertex_b, weight),
            self.add_directed_edge(vertex_b, vertex_a, weight)
        )
    
    def get_edges(self) -> list[Edge]:
        """Get all edges in the graph."""
        edges = []
        for edge_list in self._from_edges.values():
            edges.extend(edge_list)
        return edges
    
    def get_edges_from(self, vertex: Vertex) -> list[Edge]:
        """Get all edges leaving from a vertex."""
        return self._from_edges[vertex]
    
    def get_edges_to(self, vertex: Vertex) -> list[Edge]:
        """Get all edges arriving at a vertex."""
        return self._to_edges[vertex]
    
    def get_vertex(self, label: str) -> Vertex | None:
        """Find a vertex by its label. Returns None if not found."""
        for vertex in self._from_edges:
            if vertex.label == label:
                return vertex
        return None
    
    def get_vertices(self) -> list[Vertex]:
        """Get all vertices in the graph."""
        return list(self._from_edges.keys())
    
    def has_edge(self, from_vertex: Vertex, to_vertex: Vertex) -> bool:
        """Check if a directed edge exists from from_vertex to to_vertex."""
        if from_vertex not in self._from_edges:
            return False
        for edge in self._from_edges[from_vertex]:
            if edge.to_vertex == to_vertex:
                return True
        return False
