# **Searching and Algorithm Analysis**

This document covers fundamental searching algorithms, the mathematical analysis of algorithm growth rates (Big O), and the principles of recursion.

## **1\. Searching Algorithms**

Searching is the process of finding the location of a specific "key" within a data structure.

### **1.1 Linear Search**

Linear search starts at the beginning of an array and checks each element sequentially until the key is found or the end of the array is reached.

* **Logic:** Iterates from index $0$ to $N-1$.  
* **Efficiency:** \* **Worst Case:** $O(N)$ (key is at the end or not present).  
  * **Best Case:** $O(1)$ (key is at the first index).  
* **Requirement:** Works on both sorted and unsorted arrays.

### **1.2 Binary Search**

Binary search is a much faster algorithm that repeatedly divides the search space in half.

* **Logic:** It checks the middle element. If the key is smaller, it searches the left half; if larger, it searches the right half.  
* **Efficiency:** \* **Worst Case:** $O(\\log N)$.  
  * **Best Case:** $O(1)$ (key is the middle element).  
* **Requirement:** The array **must be sorted**.  
* **Formula:** For an $N$-element array, the maximum steps are $\\lfloor \\log\_2 N \\rfloor \+ 1$.

## **2\. Growth of Functions and Big O Notation**

Complexity analysis describes how an algorithm’s resource usage (time/memory) scales as input size $N$ grows.

### **2.1 Constant Time Operations**

Theoretical analysis counts **constant time operations** ($O(1)$) rather than seconds. These are operations that take the same amount of time regardless of input size:

* Fixed-size arithmetic (e.g., x \+ y).  
* Assignment (e.g., x \= 10).  
* Array indexing (e.g., arr\[i\]).  
* Comparisons of fixed-size values (e.g., if (a \> b)).

### **2.2 Rules for Big O**

1. **Discard lower-order terms:** In $5 \+ 13N \+ 7N^2$, we keep only $7N^2$.  
2. **Discard constants:** $O(7N^2)$ simplifies to $O(N^2)$.

### **2.3 Common Complexities**

* $O(1)$ **(Constant):** Accessing an array element.  
* $O(\\log N)$ **(Logarithmic):** Binary search.  
* $O(N)$ **(Linear):** Linear search.  
* $O(N \\log N)$ **(Linearithmic):** Efficient sorting (Merge Sort).  
* $O(N^2)$ **(Quadratic):** Nested loops (Selection Sort).  
* $O(c^N)$ **(Exponential):** Recursive Fibonacci.

## **3\. Recursion**

A **recursive algorithm** solves a problem by breaking it into smaller subproblems of the same type.

### **3.1 The Two Essential Components**

1. **Base Case:** A terminating condition where the function returns a value without making a further recursive call.  
2. **Recursive Case:** The part where the function calls itself with a smaller input.

### **3.2 Recursion Trees**

A recursion tree is a visual tool used to solve **recurrence relations** (equations that describe recursive runtimes).

* $T(N) \= k \+ T(N/2)$**:** Results in a tree of height $\\log N$, leading to $O(\\log N)$ (e.g., Binary Search).  
* $T(N) \= N \+ T(N/2) \+ T(N/2)$**:** Results in $O(N \\log N)$ (each level of the tree sums to $N$, and there are $\\log N$ levels).  
* $T(N) \= N \+ T(N-1)$**:** Results in $O(N^2)$ (a summation of $N \+ (N-1) \+ \\dots \+ 1$).

## **4\. Summary of Practical Exercises**

The exercises in this module focused on developing the following skills:

* **Trace Analysis:** Manually calculating the number of comparisons made during linear vs. binary searches for specific keys.  
* **Big O Simplification:** Applying rules to reduce complex functions (e.g., $10 \+ O(N^2)$) to their simplest growth rate.  
* **Code Implementation:** Adapting standard algorithms to use **Custom Comparers** (using template classes and inheritance) to search non-integer data like Strings.  
* **Nested Loop Analysis:** Summing the iterations of inner loops to determine the total complexity of algorithms like Selection Sort.