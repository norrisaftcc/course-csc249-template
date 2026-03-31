// adventure.cpp — CSC 249 Graph Homework Starter
// A navigable world built on a graph.
//
// Compile: g++ -std=c++17 adventure.cpp -o adventure
// Run:     ./adventure

#include <iostream>
#include <string>
#include <algorithm>
#include "Graph.h"

using namespace std;

// ──────────────────────────────────────────────────
// HELPER: Convert a string to lowercase
// ──────────────────────────────────────────────────
string toLower(string s) {
    transform(s.begin(), s.end(), s.begin(), ::tolower);
    return s;
}

// ──────────────────────────────────────────────────
// TODO: Build your world here
// ──────────────────────────────────────────────────
void buildWorld(Graph& world, Vertex*& startRoom) {
    // Example: a tiny 3-room house
    // Replace this with YOUR world (6+ rooms, 8+ connections)
    
    Vertex* kitchen = world.AddVertex("Kitchen");
    Vertex* hallway = world.AddVertex("Hallway");
    Vertex* bedroom = world.AddVertex("Bedroom");
    
    world.AddDirectedEdge(kitchen, hallway, "east");
    world.AddDirectedEdge(hallway, kitchen, "west");
    world.AddDirectedEdge(hallway, bedroom, "north");
    world.AddDirectedEdge(bedroom, hallway, "south");
    
    startRoom = kitchen;
}

// ──────────────────────────────────────────────────
// Display the current room and available exits
// ──────────────────────────────────────────────────
void look(Graph& world, Vertex* currentRoom) {
    cout << "\n────────────────────────" << endl;
    cout << "You are in the " << currentRoom->label << "." << endl;
    
    // TODO: Add room descriptions here (optional but encouraged)
    
    cout << "Exits:" << endl;
    for (Edge* exit : *world.GetEdgesFrom(currentRoom)) {
        cout << "  " << exit->weight << " -> " << exit->toVertex->label << endl;
    }
    cout << "────────────────────────" << endl;
}

// ──────────────────────────────────────────────────
// Try to move in a direction. Returns new room or nullptr.
// ──────────────────────────────────────────────────
Vertex* tryMove(Graph& world, Vertex* currentRoom, const string& direction) {
    for (Edge* exit : *world.GetEdgesFrom(currentRoom)) {
        if (toLower(exit->weight) == toLower(direction)) {
            return exit->toVertex;
        }
    }
    return nullptr;  // no exit in that direction
}

// ──────────────────────────────────────────────────
// Main game loop
// ──────────────────────────────────────────────────
int main() {
    Graph world;
    Vertex* currentRoom = nullptr;
    
    buildWorld(world, currentRoom);
    
    cout << "========================================" << endl;
    cout << "  Welcome to [YOUR WORLD NAME HERE]" << endl;
    cout << "  Type a direction to move, or:" << endl;
    cout << "    look  - see where you are" << endl;
    cout << "    exits - list available exits" << endl;
    cout << "    quit  - exit the game" << endl;
    cout << "========================================" << endl;
    
    look(world, currentRoom);
    
    string input;
    while (true) {
        cout << "\n> ";
        getline(cin, input);
        input = toLower(input);
        
        if (input == "quit" || input == "q") {
            cout << "Thanks for exploring!" << endl;
            break;
        }
        else if (input == "look" || input == "l") {
            look(world, currentRoom);
        }
        else if (input == "exits") {
            for (Edge* exit : *world.GetEdgesFrom(currentRoom)) {
                cout << "  " << exit->weight << endl;
            }
        }
        else if (input.substr(0, 3) == "go ") {
            // Handle "go north" style input
            string direction = input.substr(3);
            Vertex* nextRoom = tryMove(world, currentRoom, direction);
            if (nextRoom) {
                currentRoom = nextRoom;
                look(world, currentRoom);
            } else {
                cout << "You can't go that way." << endl;
            }
        }
        else {
            // Try the raw input as a direction (e.g., just "north")
            Vertex* nextRoom = tryMove(world, currentRoom, input);
            if (nextRoom) {
                currentRoom = nextRoom;
                look(world, currentRoom);
            } else {
                cout << "I don't understand '" << input << "'." << endl;
                cout << "Try a direction, 'look', 'exits', or 'quit'." << endl;
            }
        }
    }
    
    return 0;
}
