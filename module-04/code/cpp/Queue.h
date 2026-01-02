/**
 * Queue implementation - First In, First Out (FIFO)
 * Module 04: Linear Structures
 *
 * Note: This uses std::deque for O(1) operations at both ends.
 */

#ifndef QUEUE_H
#define QUEUE_H

#include <deque>
#include <stdexcept>
#include <string>

template <typename T>
class Queue {
private:
    std::deque<T> items;

public:
    /**
     * Add item to back of queue.
     */
    void enqueue(const T& item) {
        items.push_back(item);
    }

    /**
     * Remove and return front item.
     * Throws std::out_of_range if empty.
     */
    T dequeue() {
        if (isEmpty()) {
            throw std::out_of_range("Cannot dequeue from empty queue");
        }
        T item = items.front();
        items.pop_front();
        return item;
    }

    /**
     * Return front item without removing.
     * Throws std::out_of_range if empty.
     */
    T front() const {
        if (isEmpty()) {
            throw std::out_of_range("Cannot peek empty queue");
        }
        return items.front();
    }

    /**
     * Return true if queue is empty.
     */
    bool isEmpty() const {
        return items.empty();
    }

    /**
     * Return number of items in queue.
     */
    int size() const {
        return items.size();
    }
};

#endif // QUEUE_H
