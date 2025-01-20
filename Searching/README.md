# Binary Search Algorithm Implementations

This repository contains Python implementations of binary search algorithms to solve two tasks involving searching for elements in sorted data structures. The implementations achieve logarithmic time complexity.

---

## Features

### **Task 1: Find First and Last Occurrence**
- **Problem**: Given a sorted array of integers, find the first and last occurrence of a target value. If the target is not found, return `[-1, -1]`.
- **Complexity**: O(log n) runtime complexity.
- **Solution**: Implements a binary search algorithm to find the first and last indices of the target.

#### Example:
```python
nums = [4, 9, 10, 13, 17, 17, 19, 21]
target = 17
Output: [4, 5]
```

### **Task 2: Search in a 2D Matrix**
- **Problem**: Given an `m x n` matrix where each row is sorted, and the first integer of each row is greater than the last integer of the previous row, find whether a target exists in the matrix.
- **Complexity**: O(log(m * n)) runtime complexity.
- **Solution**: Implements a binary search algorithm on a virtual 1D representation of the matrix.

#### Example:
```python
matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
target = 3
Output: True
```

---

## How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/<your-username>/Algorithms_ImplementationsPython.git
   ```
2. Navigate to the folder:
   ```bash
   cd Searching
   ```
3. Run the Python script:
   ```bash
   python binary_search.py
   ```
   
---

## Test Cases

### Task 1: First and Last Occurrence
The following test cases validate the implementation:
| Input                           | Target | Expected Output |
|---------------------------------|--------|-----------------|
| `[1, 2, 5, 8, 17, 17, 19, 22]` | 17     | `[4, 5]`        |
| `[2, 3, 4, 5, 10, 11, 14]`     | 12     | `[-1, -1]`      |
| `[]`                            | 0      | `[-1, -1]`      |
| `[7, 7, 7, 7, 7, 7, 7]`         | 7      | `[0, 6]`        |

### Task 2: Search in 2D Matrix
The following test cases validate the implementation:
| Input Matrix                              | Target | Expected Output |
|-------------------------------------------|--------|-----------------|
| `[[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]` | 3      | `True`          |
| `[[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]` | 13     | `False`         |
| `[]`                                      | 0      | `False`         |

---

## Learning Outcomes

- Understand and implement binary search algorithms for one-dimensional and two-dimensional data.
- Optimize search operations to logarithmic time complexity.
- Handle edge cases, such as empty inputs and missing target values.

---

This repository demonstrates efficient search operations using binary search in Python.
