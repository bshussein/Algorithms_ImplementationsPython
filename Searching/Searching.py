# Task 1: Algorithm with O(log n) runtime complexity.

# Function to find the first and last occurrence of target
def binary_search(arr, target):

    def first_occur(arr, target):
        low = 0 # Starting index
        high = len(arr) - 1 # Ending of index (last element)
        first = -1 # Set to -1 to signify not found

        while low <= high:
            mid = (low + high) // 2 # Mid index
            if arr[mid] == target: # When target is found at mid index
                first = mid # first occurrence
                high = mid - 1  # Continue searching in the left half (search for earlier occurrence)
            elif arr[mid] < target:
                low = mid + 1 # left would move one to the right side
            else: # If target is smaller move high to the left side
                high = mid - 1
        return first

    def last_occur(arr, target):
        low = 0 # Starting index
        high = len(arr) - 1 # Ending of index (last element)
        last = -1 # Set to -1 to signify not found

        while low <= high:
            mid = (low + high) // 2
            if arr[mid] == target:
                last = mid # Set last occurrence to mid index
                low = mid + 1  # Continue searching on the right side
            elif arr[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        return last

    # check if the number is within the array
    first = first_occur(arr, target)
    last = last_occur(arr, target)

    # If target is not found
    if first == -1 or last == -1:
        return [-1, -1]

    else: # If found return the indices of first and last occurrence
        return [first, last]

# Task 1 Test Cases

print("\n------------ Task 1 --------------\n")
test_cases = [
    {'nums': [1, 2, 5, 8, 17, 17, 19, 22], 'target': 17, 'expected': [4, 5]},
    {'nums': [2, 3, 4, 5, 10, 11, 14], 'target': 12, 'expected': [-1, -1]},
    {'nums': [], 'target': 0, 'expected': [-1, -1]},
    {'nums': [1, 1, 1, 3, 5, 6, 6, 7, 7, 7], 'target': 5, 'expected': [4, 4]},
    {'nums': [7, 7, 7, 7, 7, 7, 7], 'target': 7, 'expected': [0, 6]},
    {'nums': [2, 4, 4, 4, 8, 10], 'target': 5, 'expected': [1, 3]},  # Testing the failing function by placing wrong expected result
]

for case in test_cases:
    result = binary_search(case['nums'], case['target']) # Test binary_search function
    print(f"Input: {case['nums']} Target: {case['target']}")
    print(f"Expected Output: {case['expected']}")
    print(f"Actual Output: {result}")
    print(f"Pass/Fail: {'PASS' if result == case['expected'] else 'FAIL'}\n")

    print('-'*50)

# Task 2: Finding a target within a 2D matrix  in O(log(m * n)) time complexity
def matrix_search(matrix, target):
    # Edge case (matrix empty)
    if not matrix or not matrix[0]:
        return False

    # Dimensions of the matrix
    m = len(matrix) # Row
    n = len(matrix[0]) # Column
    tot = m * n # Total number of elements in the matrix

    low = 0 # Starting index
    high = tot - 1 # Ending index

    while low <= high:
        mid = (low + high) // 2 # Mid index
        row_ind = i = mid // n
        col_ind = j = mid % n

        mid_val = matrix[i][j]

        if mid_val == target:
            return True # Target found
        elif mid_val < target:
            low = mid + 1 # Continue searching on the right side
        else:
            high = mid - 1 # Continue searching on the left side

    return False # Target not found

# Task 2 Test Case
print("\n------------ Task 2 --------------\n")
test_cases_2 = [
    {'matrix': [[1, 2, 3, 4], [7, 8, 9, 11], [15, 17, 19, 21]], 'target': 7, 'expected': True},
    {'matrix': [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 'target': 13, 'expected': False},
    {'matrix': [], 'target': 0, 'expected': False},

]

for case in test_cases_2:
    result = matrix_search(case['matrix'], case['target'])
    print(f"Input: {case['matrix']} Target: {case['target']}")
    print(f"Expected Result: {case['expected']}")
    print(f"Actual Result: {result}\n")

    print('-'*50)
