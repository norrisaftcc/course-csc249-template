# demo_flights.py — CSC 249 Graph Demo
# Run: python demo_flights.py

from graph import Graph

def main():
    # Create a new Graph
    flights = Graph()
    
    # Add cities as vertices
    tokyo  = flights.add_vertex("Tokyo")
    nyc    = flights.add_vertex("New York")
    london = flights.add_vertex("London")
    sydney = flights.add_vertex("Sydney")
    
    # Add flight routes as undirected edges (you can fly both ways)
    flights.add_undirected_edge(tokyo,  nyc,    "6743 miles")
    flights.add_undirected_edge(tokyo,  london, "5941 miles")
    flights.add_undirected_edge(tokyo,  sydney, "4863 miles")
    flights.add_undirected_edge(nyc,    london, "3425 miles")
    flights.add_undirected_edge(nyc,    sydney, "9868 miles")
    flights.add_undirected_edge(london, sydney, "10562 miles")
    
    # Display each city and its flights
    print("=== FLIGHT NETWORK ===\n")
    
    for city in flights.get_vertices():
        print(f"Airport: {city.label}")
        
        print("  Departures:")
        for flight in flights.get_edges_from(city):
            print(f"    -> {flight.to_vertex.label} ({flight.weight})")
        
        print("  Arrivals:")
        for flight in flights.get_edges_to(city):
            print(f"    <- {flight.from_vertex.label} ({flight.weight})")
        
        print()
    
    # Quick queries
    print("=== QUERIES ===")
    print(f"Direct flight Tokyo to London? "
          f"{'Yes' if flights.has_edge(tokyo, london) else 'No'}")
    print(f"Total airports: {len(flights.get_vertices())}")
    print(f"Flights from New York: {len(flights.get_edges_from(nyc))}")


if __name__ == "__main__":
    main()
