# **Lists, Stacks, and Queues**

This document explores linear data structures, focusing on how data is ordered and the specific protocols for accessing, inserting, and removing elements.

## **1\. Linked Lists**

A **Linked List** is a linear data structure where elements (nodes) are not stored in contiguous memory locations. Instead, each node points to the next, forming a chain.

### **1.1 Singly Linked Lists**

Each node consists of a **data** field and a **next** pointer.

* **Head:** The first node in the list.  
* **Tail:** The last node, whose "next" pointer is null.  
* **Operations:** \* **Prepend:** Adding to the front ($O(1)$).  
  * **Append:** Adding to the end ($O(1)$ if tail pointer is maintained, otherwise $O(N)$).  
  * **Insertion/Deletion:** $O(1)$ if the position is already known, but $O(N)$ if the list must be traversed to find the position.

### **1.2 Doubly Linked Lists**

Nodes contain a data field, a **next** pointer, and a **prev** (previous) pointer.

* **Advantage:** Allows for bi-directional traversal and easier deletion of a known node.  
* **Trade-off:** Increased memory usage per node to store the extra pointer.

## **2\. Stacks (LIFO)**

A **Stack** is an abstract data type that follows the **Last-In, First-Out** principle. Imagine a stack of physical trays; the last tray placed on top is the first one removed.

### **2.1 Core Operations**

* **Push:** Adds an item to the top ($O(1)$).  
* **Pop:** Removes the top item ($O(1)$).  
* **Peek:** Returns the top item without removing it ($O(1)$).

### **2.2 Applications**

* **Function Calls:** The "Call Stack" in programming languages manages function execution and local variables.  
* **Undo Mechanisms:** Tracking recent changes in software (the most recent change is the first to be undone).  
* **Expression Parsing:** Evaluating mathematical notation (like Postfix/Reverse Polish Notation).

## **3\. Queues (FIFO)**

A **Queue** is an abstract data type that follows the **First-In, First-Out** principle. Like a line at a grocery store, the first person to arrive is the first to be served.

### **3.1 Core Operations**

* **Enqueue:** Adds an item to the rear ($O(1)$).  
* **Dequeue:** Removes the item from the front ($O(1)$).  
* **Peek:** Returns the front item without removing it ($O(1)$).

### **3.2 Variations**

* **Deque (Double-Ended Queue):** Allows insertion and removal from both the front and the back.  
* **Priority Queue:** Each element has a "priority." Elements with higher priority are dequeued before those with lower priority, regardless of arrival order.

## **4\. Implementation Trade-offs**

Linear structures can be implemented using either **Arrays** or **Linked Lists**.

| Feature | Array-Based | Linked List-Based |
| :---- | :---- | :---- |
| **Random Access** | $O(1)$ (via index) | $O(N)$ (must traverse) |
| **Resizing** | Costly ($O(N)$ to copy/reallocate) | Dynamic (grows as needed) |
| **Memory** | Contiguous, low overhead | Non-contiguous, higher overhead (pointers) |
| **Insertion at Start** | $O(N)$ (requires shifting) | $O(1)$ (pointer update) |

## **5\. Summary of Topics Exercised**

The exercises and practical tasks for this chapter focused on the following competencies:

* **Pointer Manipulation:** Correctly reassigning next and prev pointers during list insertions and deletions to prevent "memory leaks" or broken chains.  
* **Overflow/Underflow Handling:** Implementing checks for popping from an empty stack or dequeuing from an empty queue.  
* **State Management:** Tracking the head, tail, and length of structures to ensure $O(1)$ performance for common operations.  
* **Iterator Logic:** Implementing traversal methods to access every element in a list without exposing the underlying node structure.