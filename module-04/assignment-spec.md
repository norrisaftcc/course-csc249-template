# CSC 249 Module 04: Stacks and Queues
## "Task Processing Systems"

---

## Assignment Overview

| | |
|---|---|
| **Module** | M04: Stacks and Queues |
| **Duration** | 1 week |
| **Points** | 100 total |
| **Language** | Your choice: C++ or Python |
| **Deliverable** | 1 Pull Request |

---

## The Scenario

> **MEMO — DEPARTMENT OF TASK PROCESSING**
>
> Employee,
>
> The Algorithm has detected inefficiencies in departmental operations. Two critical systems require implementation:
>
> 1. **Action Reversal System** — Employees frequently make errors. A system to undo recent actions is required. (Stack)
>
> 2. **Citizen Request Queue** — Requests must be processed in order of arrival. No exceptions. First In, First Out. (Queue)
>
> Your compliance rating depends on successful implementation.
>
> — Department of Task Processing

---

## What You're Learning

**Stacks:** Last In, First Out (LIFO)
- Think: stack of plates, browser back button, undo functionality
- The most recent item added is the first one removed

**Queues:** First In, First Out (FIFO)
- Think: line at a store, print queue, ticket system
- The oldest item added is the first one processed

Both are fundamental building blocks used everywhere in software.

---

## Part A: Stack Implementation (40 points)

### Requirements

Implement a `Stack` class with the following operations:

| Operation | Description | Return |
|-----------|-------------|--------|
| `push(item)` | Add item to top of stack | None |
| `pop()` | Remove and return top item | The item (or error if empty) |
| `peek()` | Return top item without removing | The item (or error if empty) |
| `isEmpty()` | Check if stack is empty | Boolean |
| `size()` | Return number of items | Integer |

### Implementation Notes

**You may use:**
- A dynamic array/list as the underlying storage
- Built-in list/vector operations

**You must:**
- Create a class (not just use a raw list)
- Handle the empty stack case for pop/peek
- Include comments explaining your approach

### C++ Skeleton

```cpp
#include <iostream>
#include <vector>
#include <string>
using namespace std;

class Stack {
private:
    vector<string> items;
    
public:
    void push(string item) {
        // TODO: Add item to top
    }
    
    string pop() {
        // TODO: Remove and return top item
        // Handle empty case
    }
    
    string peek() {
        // TODO: Return top item without removing
        // Handle empty case
    }
    
    bool isEmpty() {
        // TODO
    }
    
    int size() {
        // TODO
    }
};
```

### Python Skeleton

```python
class Stack:
    def __init__(self):
        self.items = []
    
    def push(self, item):
        """Add item to top of stack"""
        # TODO
        pass
    
    def pop(self):
        """Remove and return top item. Raise error if empty."""
        # TODO
        pass
    
    def peek(self):
        """Return top item without removing. Raise error if empty."""
        # TODO
        pass
    
    def is_empty(self):
        """Return True if stack is empty"""
        # TODO
        pass
    
    def size(self):
        """Return number of items in stack"""
        # TODO
        pass
```

### Part A Deliverable

Create an "Undo System" demo that:
1. Accepts user actions (strings like "typed 'hello'", "deleted paragraph", "formatted bold")
2. Stores each action on the stack
3. Allows user to undo (pop) recent actions
4. Shows the action being undone

**Sample Interaction:**
```
=== ACTION REVERSAL SYSTEM ===
Commands: [add] action, [undo], [show], [quit]

> add typed 'hello world'
Action recorded: typed 'hello world'

> add deleted paragraph 2
Action recorded: deleted paragraph 2

> add formatted header as bold
Action recorded: formatted header as bold

> show
Action history (most recent first):
  1. formatted header as bold
  2. deleted paragraph 2
  3. typed 'hello world'

> undo
Undoing: formatted header as bold

> undo
Undoing: deleted paragraph 2

> show
Action history (most recent first):
  1. typed 'hello world'

> quit
Session ended. 1 action(s) remain in history.
```

---

## Part B: Queue Implementation (40 points)

### Requirements

Implement a `Queue` class with the following operations:

| Operation | Description | Return |
|-----------|-------------|--------|
| `enqueue(item)` | Add item to back of queue | None |
| `dequeue()` | Remove and return front item | The item (or error if empty) |
| `front()` | Return front item without removing | The item (or error if empty) |
| `isEmpty()` | Check if queue is empty | Boolean |
| `size()` | Return number of items | Integer |

### C++ Skeleton

```cpp
#include <iostream>
#include <vector>
#include <string>
using namespace std;

class Queue {
private:
    vector<string> items;
    
public:
    void enqueue(string item) {
        // TODO: Add item to back
    }
    
    string dequeue() {
        // TODO: Remove and return front item
        // Handle empty case
    }
    
    string front() {
        // TODO: Return front item without removing
        // Handle empty case
    }
    
    bool isEmpty() {
        // TODO
    }
    
    int size() {
        // TODO
    }
};
```

### Python Skeleton

```python
class Queue:
    def __init__(self):
        self.items = []
    
    def enqueue(self, item):
        """Add item to back of queue"""
        # TODO
        pass
    
    def dequeue(self):
        """Remove and return front item. Raise error if empty."""
        # TODO
        pass
    
    def front(self):
        """Return front item without removing. Raise error if empty."""
        # TODO
        pass
    
    def is_empty(self):
        """Return True if queue is empty"""
        # TODO
        pass
    
    def size(self):
        """Return number of items in queue"""
        # TODO
        pass
```

### Part B Deliverable

Create a "Request Processing" demo that:
1. Accepts citizen requests (with ID and description)
2. Adds them to the queue
3. Processes requests in FIFO order
4. Shows queue status

**Sample Interaction:**
```
=== CITIZEN REQUEST QUEUE ===
Commands: [add] id description, [process], [next], [status], [quit]

> add C-1001 Request for permit renewal
Request added: C-1001 - Request for permit renewal
Position in queue: 1

> add C-1002 Complaint about neighbor
Request added: C-1002 - Complaint about neighbor
Position in queue: 2

> add C-1003 License application
Request added: C-1003 - License application
Position in queue: 3

> status
Queue status: 3 request(s) pending
Next up: C-1001 - Request for permit renewal

> process
Processing: C-1001 - Request for permit renewal
Request completed. 2 remaining.

> next
Next up: C-1002 - Complaint about neighbor

> process
Processing: C-1002 - Complaint about neighbor
Request completed. 1 remaining.

> quit
Session ended. 1 request(s) still in queue.
```

---

## Part C: Reflection Questions (20 points)

Answer these questions in a file called `REFLECTION.md`:

### Question 1: Stack vs Queue (8 points)
In your own words, explain the key difference between a stack and a queue. Give one real-world example of each that was NOT mentioned in this assignment.

### Question 2: Implementation Choices (6 points)
You used a list/vector as the underlying storage. What is the Big O complexity of:
- `push` / `enqueue`
- `pop` / `dequeue`

For the queue, removing from the front of a list is O(n) in most implementations. How could you make it O(1)? (Hint: think about what you'd need to track, or look up "circular buffer" or "collections.deque")

### Question 3: AI Collaboration (6 points)
What did you use AI for in this assignment? What did it get right? What did you have to fix or figure out yourself?

---

## Grading Rubric

### Part A: Stack (40 points)

| Criteria | Points |
|----------|--------|
| All 5 operations implemented correctly | 20 |
| Empty stack cases handled | 5 |
| Undo demo works as specified | 10 |
| Code is commented and readable | 5 |

### Part B: Queue (40 points)

| Criteria | Points |
|----------|--------|
| All 5 operations implemented correctly | 20 |
| Empty queue cases handled | 5 |
| Request demo works as specified | 10 |
| Code is commented and readable | 5 |

### Part C: Reflection (20 points)

| Criteria | Points |
|----------|--------|
| Stack vs Queue explanation clear, examples valid | 8 |
| Complexity analysis correct, optimization discussed | 6 |
| AI collaboration documented honestly | 6 |

---

## Submission

### File Structure

```
module-04-stacksqueues-yourname/
├── stack.cpp (or stack.py)
├── queue.cpp (or queue.py)
├── undo_demo.cpp (or undo_demo.py)
├── request_demo.cpp (or request_demo.py)
├── REFLECTION.md
└── test_output.txt (copy of sample runs)
```

### Pull Request

- **Branch:** `module-04-stacksqueues-yourname`
- **Title:** `Module 04 Stacks and Queues - [Your Name]`
- **Include:** All files above

---

## Testing Checklist

### Stack Tests
- [ ] Push multiple items
- [ ] Pop returns correct item (most recent)
- [ ] Peek doesn't remove the item
- [ ] Pop/Peek on empty stack handles gracefully
- [ ] Size updates correctly
- [ ] isEmpty returns correct value

### Queue Tests
- [ ] Enqueue multiple items
- [ ] Dequeue returns correct item (oldest)
- [ ] Front doesn't remove the item
- [ ] Dequeue/Front on empty queue handles gracefully
- [ ] Size updates correctly
- [ ] isEmpty returns correct value

---

## Tips

### Common Mistakes

**Stack:**
- Forgetting that pop removes AND returns
- Not checking for empty before pop/peek
- Removing from wrong end (front instead of back)

**Queue:**
- Removing from wrong end (back instead of front)
- Adding to wrong end (front instead of back)
- Confusing enqueue/dequeue with push/pop terminology

### AI Prompting Ideas

Good prompts for this assignment:
- "Explain the difference between a stack and queue with a visual diagram"
- "What are the Big O complexities for stack operations using a dynamic array?"
- "How do I handle an empty stack exception in Python/C++?"
- "Why is removing from the front of a Python list O(n)?"

Remember: AI can explain concepts and help debug, but you need to implement and understand the code yourself.

---

## Extension Challenges (Optional, no extra credit)

If you finish early and want more:

1. **Double-Ended Queue (Deque):** Implement a structure that allows push/pop from both ends

2. **Stack with Min:** Implement a stack that also tracks the minimum element in O(1) time

3. **Queue using Two Stacks:** Implement a queue using only stack operations (classic interview question)

4. **Priority Queue Preview:** Modify your queue so high-priority requests jump ahead (foreshadowing Module 10)

---

## Why This Matters

Stacks and queues are everywhere:

**Stacks in the wild:**
- Browser back button
- Undo/Redo in any editor
- Function call stack (how recursion works)
- Expression parsing (calculators)
- Syntax validation (matching parentheses)

**Queues in the wild:**
- Print queues
- Message queues (Kafka, RabbitMQ)
- Task scheduling
- Breadth-first search (coming in graphs)
- Any "first come, first served" system

When you understand these two structures, you've got building blocks for half of computer science.

---

*The Algorithm appreciates your orderly processing of tasks.*
