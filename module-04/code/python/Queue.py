"""
Queue implementation - First In, First Out (FIFO)
Module 04: Linear Structures

Note: This uses a simple list implementation. For O(1) dequeue,
consider using collections.deque instead.
"""

from collections import deque


class Queue:
    """A queue using collections.deque for O(1) operations."""

    def __init__(self):
        """Initialize an empty queue."""
        self.items = deque()

    def enqueue(self, item):
        """Add item to back of queue."""
        self.items.append(item)

    def dequeue(self):
        """Remove and return front item. Raises IndexError if empty."""
        if self.is_empty():
            raise IndexError("Cannot dequeue from empty queue")
        return self.items.popleft()

    def front(self):
        """Return front item without removing. Raises IndexError if empty."""
        if self.is_empty():
            raise IndexError("Cannot peek empty queue")
        return self.items[0]

    def is_empty(self):
        """Return True if queue is empty."""
        return len(self.items) == 0

    def size(self):
        """Return number of items in queue."""
        return len(self.items)

    def __str__(self):
        """String representation showing items front to back."""
        if self.is_empty():
            return "Queue: (empty)"
        items_str = " <- ".join(str(item) for item in self.items)
        return f"Queue (front first): {items_str}"


# Demo usage
if __name__ == "__main__":
    queue = Queue()

    print("=== Queue Demo ===")
    print(f"Empty? {queue.is_empty()}")

    queue.enqueue("first")
    queue.enqueue("second")
    queue.enqueue("third")

    print(f"\nAfter enqueueing 'first', 'second', 'third':")
    print(queue)
    print(f"Size: {queue.size()}")

    print(f"\nFront: {queue.front()}")
    print(f"Dequeue: {queue.dequeue()}")
    print(f"Dequeue: {queue.dequeue()}")

    print(f"\nAfter two dequeues:")
    print(queue)
