"""
Stack implementation - Last In, First Out (LIFO)
Module 04: Linear Structures
"""


class Stack:
    """A stack using a Python list as underlying storage."""

    def __init__(self):
        """Initialize an empty stack."""
        self.items = []

    def push(self, item):
        """Add item to top of stack."""
        self.items.append(item)

    def pop(self):
        """Remove and return top item. Raises IndexError if empty."""
        if self.is_empty():
            raise IndexError("Cannot pop from empty stack")
        return self.items.pop()

    def peek(self):
        """Return top item without removing. Raises IndexError if empty."""
        if self.is_empty():
            raise IndexError("Cannot peek empty stack")
        return self.items[-1]

    def is_empty(self):
        """Return True if stack is empty."""
        return len(self.items) == 0

    def size(self):
        """Return number of items in stack."""
        return len(self.items)

    def __str__(self):
        """String representation showing items top to bottom."""
        if self.is_empty():
            return "Stack: (empty)"
        items_str = " -> ".join(str(item) for item in reversed(self.items))
        return f"Stack (top first): {items_str}"


# Demo usage
if __name__ == "__main__":
    stack = Stack()

    print("=== Stack Demo ===")
    print(f"Empty? {stack.is_empty()}")

    stack.push("first")
    stack.push("second")
    stack.push("third")

    print(f"\nAfter pushing 'first', 'second', 'third':")
    print(stack)
    print(f"Size: {stack.size()}")

    print(f"\nPeek: {stack.peek()}")
    print(f"Pop: {stack.pop()}")
    print(f"Pop: {stack.pop()}")

    print(f"\nAfter two pops:")
    print(stack)
