/**
 * Stack implementation - Last In, First Out (LIFO)
 * Module 04: Linear Structures
 */

#ifndef STACK_H
#define STACK_H

#include <vector>
#include <stdexcept>
#include <string>

template <typename T>
class Stack {
private:
    std::vector<T> items;

public:
    /**
     * Add item to top of stack.
     */
    void push(const T& item) {
        items.push_back(item);
    }

    /**
     * Remove and return top item.
     * Throws std::out_of_range if empty.
     */
    T pop() {
        if (isEmpty()) {
            throw std::out_of_range("Cannot pop from empty stack");
        }
        T item = items.back();
        items.pop_back();
        return item;
    }

    /**
     * Return top item without removing.
     * Throws std::out_of_range if empty.
     */
    T peek() const {
        if (isEmpty()) {
            throw std::out_of_range("Cannot peek empty stack");
        }
        return items.back();
    }

    /**
     * Return true if stack is empty.
     */
    bool isEmpty() const {
        return items.empty();
    }

    /**
     * Return number of items in stack.
     */
    int size() const {
        return items.size();
    }
};

#endif // STACK_H
