# Task 1:
# Generate all permutations using backtracking
def permutations(s):
    # Helper function to backtrack through possible permutations
    def backtrack(start, end):
        # Base case
        if start == end:  # Only one character left, return string as list
            permutations_list.append(''.join(s))  # Convert list of characters into a string and add to list
            return

        # Loop through each character position
        for i in range(start, end):
            # Swap characters to form a new permutation
            s[start], s[i] = s[i], s[start]
            # Recurse with the next starting index
            backtrack(start + 1, end)
            # Backtrack to undo the swap for the next iteration (helps the function look for other permutations)
            s[start], s[i] = s[i], s[start]

    # Convert the string to a list of characters for swapping
    s = list(s)
    permutations_list = []
    backtrack(0, len(s))
    return permutations_list


# Function to check if s2 contains a permutation of s1
def contains_permutation(s1, s2):
    s1_perms = permutations(s1)

    # Check for any permutation occurring within s2
    for perm in s1_perms:
        if perm in s2:
            return True

    return False # No permutations found


# Task 1: Example Usage
print("\n--------------- Task 1 -------------------")
print(f"s1: 'ab', s2: 'eidbaooo', Output: {contains_permutation('ab', 'eidbaooo')}")  # True
print(f"s1: 'ab', s2: 'eidboaoo', Output: {contains_permutation('ab', 'eidboaoo')}")  # False
print(f"s1: 'ben', s2: 'carneb', Output: {contains_permutation('ben', 'carneb')}")  # True
print(f"s1: 'rev', s2: 'universal', Output: {contains_permutation('rev', 'universal')}")  # True
print(f"s1: 'sun', s2: 'universal', Output: {contains_permutation('sun', 'universal')}")  # False


# Task 2: Find the minimum number of vertical moves needed to rearrange 8 queens on a chessboard such that no two queens attack each other horizontally or diagonally.
class Board:
    def __init__(self, positions):
        self.positions = positions

    def count_conflicts(self, row, col):
        conflicts = 0

        # Searching within the column for any conflicts with the queen
        for i in range(8):  # Loop through the columns
            if i == col:
                continue  # Skip the current column. (no conflict)

            # Check if there's another queen in the same row.
            if self.positions[i] == row:
                conflicts += 1  # If conflict present in row increment by 1

            # Checking conflict through positive and negative diagonals
            if (self.positions[i] + i) == (row + col):  # Positive diagonal (r + c)
                conflicts += 1
            if (self.positions[i] - i) == (row - col):  # Negative diagonal (r - c)
                conflicts += 1

        return conflicts

    # Function to place queens using backtracking
    def solve(self, col=0):
        if col == 8:
            return True  # All queens are placed without conflict

        # Try placing a queen in each row for the current column
        for row in range(8):
            if self.is_safe(row, col):  # If safe to place the queen
                self.positions[col] = row  # Place the queen
                if self.solve(col + 1):  # Recur to place the next queen
                    return True # Solution is found
                self.positions[col] = -1  # Backtrack if placing the queen doesn't lead to a solution

        return False  # Need to backtrack (no safe solution)

    # Check if a queen can be placed at the given row and column
    def is_safe(self, row, col):
        for c in range(col):
            if (self.positions[c] == row or  # Same row
                    self.positions[c] - c == row - col or  # Same positive diagonal
                    self.positions[c] + c == row + col):  # Same negative diagonal
                return False # Not safe
        return True

    # Function to relocate the queen where it wouldn't be a conflict with the other queens
    def min_moves(self):
        moves = 0  # Keep track of number of moves

        # Loop through each column and place the queen in a row that would avoid conflict
        for col in range(8):
            # Get current count of conflicts for the queen at its initial row.
            min_conflicts = self.count_conflicts(self.positions[col], col)
            best_row = self.positions[col]

            # Try each possible row to find a better position.
            for row in range(8):
                if row != self.positions[col]:  # ignore queen's current row position
                    conflicts = self.count_conflicts(row, col) # Count of conflicts

                    # If fewer conflicts are found, update the new row.
                    if conflicts < min_conflicts:
                        min_conflicts = conflicts
                        best_row = row # Update current row as best row

            # If better row is found update the position of the queen to the (new row).
            if best_row != self.positions[col]:
                self.positions[col] = best_row
                moves += 1  # Increment the move count since the queen's position has changed.

        return moves


# Task 2 Test Case:
def test_task2():
    print("\n---------------------- Task 2 ------------------------")
    cases = [
        ([1, 2, 3, 4, 5, 6, 7, 8], 7),
        ([1, 1, 1, 1, 1, 1, 1, 1], 7),
        ([1, 3, 5, 7, 2, 4, 6, 8], 0),  # No moves needed
        ([2, 4, 1, 7, 5, 2, 7, 3], 2)
    ]

    # Run through each test case.
    for input_case, expected_moves in cases:
        board = Board(input_case[:])  # Use a copy of the list to avoid modifying the original test cases
        result = board.min_moves()
        print(f"Input: {input_case}, Minimum Moves Made: {result}, Expected: {expected_moves}")


test_task2()
