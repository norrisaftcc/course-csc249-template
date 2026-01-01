# Tutorial: Stacks

**Module:** M04 - Linear Structures
**Language:** C++ and Python
**Prerequisites:** Basic class design, arrays/lists

## Learning Objectives

By the end of this tutorial, you will be able to:
- Explain the LIFO (Last In, First Out) principle
- Implement a stack using an array/list
- Use stack operations: push, pop, peek, isEmpty, size
- Identify real-world applications of stacks

## Introduction

A **stack** is a linear data structure that follows the **Last In, First Out (LIFO)** principle. Think of a stack of plates: you can only add or remove plates from the top.

### Real-World Stack Examples

- **Browser back button** - Most recent page visited is first to go back to
- **Undo functionality** - Most recent action is first to undo
- **Function call stack** - Most recent function call returns first
- **Syntax validation** - Matching parentheses, brackets, braces

## Key Concepts

### Stack Operations

| Operation | Description | Time Complexity |
|-----------|-------------|-----------------|
| `push(item)` | Add item to top | O(1) |
| `pop()` | Remove and return top item | O(1) |
| `peek()` | Return top item without removing | O(1) |
| `isEmpty()` | Check if stack is empty | O(1) |
| `size()` | Return number of items | O(1) |

### Visual Representation

```
push(A)     push(B)     push(C)     pop()       pop()

  ┌───┐     ┌───┐       ┌───┐       ┌───┐       ┌───┐
  │   │     │   │       │ C │ ←top  │   │       │   │
  ├───┤     ├───┤       ├───┤       ├───┤       ├───┤
  │   │     │ B │ ←top  │ B │       │ B │ ←top  │   │
  ├───┤     ├───┤       ├───┤       ├───┤       ├───┤
  │ A │←top │ A │       │ A │       │ A │       │ A │ ←top
  └───┘     └───┘       └───┘       └───┘       └───┘
```

## Implementation

### Python Version

```python
class Stack:
    def __init__(self):
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
```

### C++ Version

```cpp
#include <vector>
#include <stdexcept>

template <typename T>
class Stack {
private:
    std::vector<T> items;

public:
    void push(const T& item) {
        items.push_back(item);
    }

    T pop() {
        if (isEmpty()) {
            throw std::out_of_range("Cannot pop from empty stack");
        }
        T item = items.back();
        items.pop_back();
        return item;
    }

    T peek() const {
        if (isEmpty()) {
            throw std::out_of_range("Cannot peek empty stack");
        }
        return items.back();
    }

    bool isEmpty() const {
        return items.empty();
    }

    int size() const {
        return items.size();
    }
};
```

## Practice Exercises

### Exercise 1: Balanced Parentheses

Write a function that checks if a string has balanced parentheses.

```python
def is_balanced(expression):
    """Return True if parentheses are balanced."""
    stack = Stack()
    for char in expression:
        if char == '(':
            stack.push(char)
        elif char == ')':
            if stack.is_empty():
                return False
            stack.pop()
    return stack.is_empty()

# Test
print(is_balanced("((a + b) * c)"))  # True
print(is_balanced("((a + b)"))        # False
print(is_balanced(")("))              # False
```

### Exercise 2: Reverse a String

Use a stack to reverse a string.

```python
def reverse_string(s):
    """Reverse a string using a stack."""
    stack = Stack()
    for char in s:
        stack.push(char)

    result = ""
    while not stack.is_empty():
        result += stack.pop()
    return result

print(reverse_string("hello"))  # "olleh"
```

### Exercise 3: Undo System

Implement a simple text editor with undo functionality (this is part of the lab assignment).

## Common Mistakes

1. **Forgetting to check for empty stack** before pop/peek
2. **Removing from wrong end** - stack removes from the end (top), not beginning
3. **Confusing pop and peek** - pop removes, peek only looks

## Summary

- Stacks follow LIFO: Last In, First Out
- All operations are O(1) when using dynamic array
- The "top" of the stack is where items are added and removed
- Stacks are used for undo, recursion, expression parsing, and more

## Next Steps

- Complete the [Undo System Lab](../labs/lab-undo-system/)
- Learn about [Queues](queues.md) - the FIFO counterpart
- Explore [Linked Lists](linked-lists.md) as an alternative implementation
