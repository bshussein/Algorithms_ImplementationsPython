# Algorithms Implementations in Python

This repository contains Python implementations of algorithmic challenges and concepts, consolidated into a single Python file: `recursion.py`.

### Included Challenges

#### 1. Permutations and Substring Check
- **Objective**: Check if a string `s2` contains a permutation of another string `s1`.
- **Key Features**:
  - Generates all permutations of `s1` using backtracking.
  - Efficiently verifies if any permutation exists as a substring in `s2`.

#### 2. Minimum Moves for 8-Queens Problem
- **Objective**: Determine the minimum number of vertical moves required to reposition 8 queens on a chessboard such that no two queens attack each other.
- **Key Features**:
  - Uses a custom `Board` class to track conflicts and reposition queens.
  - Applies a conflict-counting approach to minimize moves.

### File Structure
- `recursion.py`: Contains both the challenges and their implementations.

### Usage
1. Clone the repository.
2. Run `recursion.py` to test the algorithms and view the output.
