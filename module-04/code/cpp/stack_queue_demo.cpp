/**
 * Stack and Queue Demo
 * Module 04: Linear Structures
 *
 * Compile: g++ -std=c++11 stack_queue_demo.cpp -o demo
 */

#include <iostream>
#include <string>
#include "Stack.h"
#include "Queue.h"

using namespace std;

int main() {
    // Stack Demo
    cout << "=== Stack Demo ===" << endl;
    Stack<string> stack;

    cout << "Empty? " << (stack.isEmpty() ? "yes" : "no") << endl;

    stack.push("first");
    stack.push("second");
    stack.push("third");

    cout << "\nAfter pushing 'first', 'second', 'third':" << endl;
    cout << "Size: " << stack.size() << endl;
    cout << "Peek: " << stack.peek() << endl;
    cout << "Pop: " << stack.pop() << endl;
    cout << "Pop: " << stack.pop() << endl;
    cout << "Size after pops: " << stack.size() << endl;

    // Queue Demo
    cout << "\n=== Queue Demo ===" << endl;
    Queue<string> queue;

    cout << "Empty? " << (queue.isEmpty() ? "yes" : "no") << endl;

    queue.enqueue("first");
    queue.enqueue("second");
    queue.enqueue("third");

    cout << "\nAfter enqueueing 'first', 'second', 'third':" << endl;
    cout << "Size: " << queue.size() << endl;
    cout << "Front: " << queue.front() << endl;
    cout << "Dequeue: " << queue.dequeue() << endl;
    cout << "Dequeue: " << queue.dequeue() << endl;
    cout << "Size after dequeues: " << queue.size() << endl;

    return 0;
}
