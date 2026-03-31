# adventure.py — CSC 249 Graph Homework Starter
# A navigable world built on a graph.
#
# Run: python adventure.py

from graph import Graph


def build_world(world: Graph) -> "Vertex":
    """
    Build the rooms and connections for your world.
    Returns the starting room vertex.
    
    TODO: Replace this example with YOUR world (6+ rooms, 8+ connections)
    """
    # Example: a tiny 3-room house
    kitchen = world.add_vertex("Kitchen")
    hallway = world.add_vertex("Hallway")
    bedroom = world.add_vertex("Bedroom")
    
    world.add_directed_edge(kitchen, hallway, "east")
    world.add_directed_edge(hallway, kitchen, "west")
    world.add_directed_edge(hallway, bedroom, "north")
    world.add_directed_edge(bedroom, hallway, "south")
    
    return kitchen  # starting room


def look(world: Graph, current_room) -> None:
    """Display the current room and available exits."""
    print()
    print("────────────────────────")
    print(f"You are in the {current_room.label}.")
    
    # TODO: Add room descriptions here (optional but encouraged)
    
    print("Exits:")
    for exit_edge in world.get_edges_from(current_room):
        print(f"  {exit_edge.weight} -> {exit_edge.to_vertex.label}")
    print("────────────────────────")


def try_move(world: Graph, current_room, direction: str):
    """Try to move in a direction. Returns new room or None."""
    for exit_edge in world.get_edges_from(current_room):
        if exit_edge.weight.lower() == direction.lower():
            return exit_edge.to_vertex
    return None


def main():
    world = Graph()
    current_room = build_world(world)
    
    print("========================================")
    print("  Welcome to [YOUR WORLD NAME HERE]")
    print("  Type a direction to move, or:")
    print("    look  - see where you are")
    print("    exits - list available exits")
    print("    quit  - exit the game")
    print("========================================")
    
    look(world, current_room)
    
    while True:
        user_input = input("\n> ").strip().lower()
        
        if user_input in ("quit", "q"):
            print("Thanks for exploring!")
            break
        
        elif user_input in ("look", "l"):
            look(world, current_room)
        
        elif user_input == "exits":
            for exit_edge in world.get_edges_from(current_room):
                print(f"  {exit_edge.weight}")
        
        elif user_input.startswith("go "):
            direction = user_input[3:]
            next_room = try_move(world, current_room, direction)
            if next_room:
                current_room = next_room
                look(world, current_room)
            else:
                print("You can't go that way.")
        
        else:
            # Try raw input as a direction (e.g., just "north")
            next_room = try_move(world, current_room, user_input)
            if next_room:
                current_room = next_room
                look(world, current_room)
            else:
                print(f"I don't understand '{user_input}'.")
                print("Try a direction, 'look', 'exits', or 'quit'.")


if __name__ == "__main__":
    main()
