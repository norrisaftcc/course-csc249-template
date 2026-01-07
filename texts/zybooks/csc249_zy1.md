# **Introduction to Data Structures and Algorithms**

This document provides a pedagogical overview of the fundamental concepts in Data Structures and Algorithms (DSA), specifically tailored for 2nd-year Computer Science students.

## **1\. Data Structures: Foundations**

A **data structure** is a specialized format for organizing, storing, and performing operations on data. Core operations include accessing, updating, searching, inserting, and removing data.

### **1.1 Core Data Structures**

* **Record:** Stores subitems (fields) with associated names (e.g., an Employee record with firstName, lastName, and title).  
* **Array:** An ordered collection of elements accessible by a positional index.  
* **Linked List:** Stores items in nodes where each node contains data and a pointer to the next node.  
* **Binary Tree:** A structure where each node has up to two children (left and right).  
* **Hash Table:** Stores unordered items by mapping (hashing) keys to specific array locations.  
* **Heap:** A tree-based structure maintaining a specific property (e.g., in a Max-Heap, a parent's key is $\\ge$ its children's keys).  
* **Graph:** Represents connections (edges) between items (vertices).

### **1.2 Selection Criteria**

Choosing a data structure requires balancing the type of data against the expected operations. For example, while an **Array** allows fast access via index, inserting an item at the beginning requires shifting all subsequent elements ($O(N)$). Conversely, a **Linked List** allows for $O(1)$ insertion at a known position because it only requires updating pointers, avoiding the "shifting problem."

## **2\. Algorithms and Computational Problems**

An **algorithm** is a sequence of steps to solve a **computational problem**. A computational problem is defined by its **input**, a specific **question** about that input, and the desired **output**.

### **2.1 Practical Applications**

Algorithms are the engines behind modern technology:

* **DNA Analysis:** Uses "Longest Common Substring" algorithms to compare genetic sequences.  
* **Search Engines:** Utilize "Binary Search" for fast retrieval from sorted data.  
* **Navigation:** Uses "Dijkstra’s Shortest Path" algorithm on graph data structures to find optimal routes.

### **2.2 Hard Problems: NP-Completeness**

Most efficient algorithms have a **polynomial runtime**. However, **NP-complete** problems (like the "Clique Problem" in social networks) have no known efficient solution. If a problem is identified as NP-complete, developers often pivot from seeking an optimal solution to finding a "good enough" (heuristic) solution.

## **3\. Abstract Data Types (ADTs)**

An **ADT** is a high-level description of a data type based on its operations (e.g., "Insert at rear") rather than its implementation.

### **3.1 Common ADTs and Implementations**

| ADT | Description | Common Underlying Structure |
| :---- | :---- | :---- |
| **List** | Ordered data | Array, Linked List |
| **Stack** | Last-In, First-Out (LIFO) | Linked List, Array |
| **Queue** | First-In, First-Out (FIFO) | Linked List, Array |
| **Set** | Collection of distinct items | Binary Search Tree, Hash Table |
| **Dictionary** | Map of Keys to Values | Hash Table, Binary Search Tree |

### **3.2 The Power of Abstraction**

Abstraction allows a programmer to use a List without knowing if it is array-based or linked-list-based. However, the underlying implementation directly impacts **runtime efficiency**. A developer must understand these details to optimize performance for specific use cases (e.g., frequent insertions vs. frequent random access).

## **4\. Algorithm Efficiency**

Efficiency is measured by **Computational Complexity**, primarily focusing on **Runtime** and **Memory (Space)** usage.

### **4.1 Runtime Complexity: $T(N)$**

$T(N)$ represents the number of operations relative to input size $N$.

* **Best Case:** The scenario where the algorithm performs the minimum operations (e.g., finding the search key at the very first index of an array).  
* **Worst Case:** The scenario where the algorithm performs the maximum operations (e.g., the search key is not in the array, requiring a full scan).

### **4.2 Space Complexity: $S(N)$**

* **Total Space Complexity:** Includes both the input data and any additional memory allocated.  
* **Auxiliary Space Complexity:** Only counts the *extra* or temporary memory used by the algorithm. For example, a "Find Max" algorithm has $O(1)$ auxiliary space because it only uses a few fixed-size variables regardless of how large the input array is.

## **5\. Summary of Practical Exercises**

The laboratory exercises and questions in this module focused on the following competencies:

* **Operational Logic:** Differentiating between the internal logic of appending to an array (resizing/incrementing) versus a linked list (pointer manipulation).  
* **ADT Interaction:** Using high-level interfaces to manage data (e.g., using a List ADT for website history) and understanding why some ADTs (like Queue) are unsuitable for specific operations like reverse iteration.  
* **Code Implementation:** Mapping pseudocode concepts to C++ structures, emphasizing that how a result is achieved (e.g., through proper object-oriented calls) is as critical as the final output.  
* **Complexity Identification:** Identifying best/worst-case scenarios for fundamental algorithms like Linear Search and "Find First Less Than."