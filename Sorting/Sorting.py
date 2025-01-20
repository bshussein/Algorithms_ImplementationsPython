# Assignment 3: Sorting

# Using quicksort and mergesort as the two sorting algorithms

# Time = O(n\log n)
# Worst case: O(n^2) (If pivot is constantly smallest or largest value in array)
# Space = O(n)
def quick_sort(arr):
    n = len(arr) # Number of elements in the array
    if n <= 1:
        return arr

    pivot = arr[n // 2] # Assigning pivot as the middle value in the array

    # dividing around the pivot into sub arrays (partitioning)
    L = [x for x in arr if x < pivot]  # Elements less than the pivot (left side)
    M = [x for x in arr if x == pivot]  # Elements equal to the pivot (midpoint)
    R = [x for x in arr if x > pivot]  # Elements greater than the pivot (right side)

    # Recursively sorting left and right sub arrays and combine with pivot (midpoint)
    return quick_sort(L) + M + quick_sort(R)

# Time = O(n\log n) Space = O(n)
def merge_sort(arr):
    n = len(arr)
    if n <= 1:
        return arr

    midpoint = n // 2 # Split array into two
    L = merge_sort(arr[:midpoint]) # Left half (auxiliary array)
    R = merge_sort(arr[midpoint:]) # Right half (auxiliary array)

    l, r = 0, 0 # Left and right index
    sorted_arr = [] # sorted array held in a list

    # Merging the two sorted halves
    while l < len(L) and r < len(R): # Within the bounds of the array
        if L[l] < R[r]:
            sorted_arr.append(L[l]) # Append the left half array when left half index is smaller than the right
            l += 1
        else:
            sorted_arr.append(R[r]) # Append the left half array when right half index is smaller than the left
            r += 1

    # Add remaining elements from left and right halves
    while l < len(L):
        sorted_arr.append(L[l])
        l += 1
    while r < len(R):
        sorted_arr.append(R[r])
        r += 1

    return sorted_arr

# Function to sort string using (Quicksort or Mergesort)
def sort_string(s, algorithm):
    s_arr = list(s)  # Convert string to list of characters
    if algorithm == "quick_sort":
        return ''.join(quick_sort(s_arr)) # Sort the characters and join them back into a single string.
    elif algorithm == "merge_sort":
        return ''.join(merge_sort(s_arr)) # Sort the characters and join them back into a single string.
    else:
        raise ValueError("Unsupported sorting algorithm")

# Function to group anagram words using Quicksort or Mergesort
def anagram_sets(strs, algorithm="quick_sort"):
    anagrams = {}

    for s in strs:
        sorted_s = sort_string(s, algorithm)  # Use sorting algorithm to sort strings

        # Place anagrams together based on their sorted letters
        if sorted_s in anagrams:
            # Add the string into the list
            anagrams[sorted_s].append(s)
        else:
            # Create new list
            anagrams[sorted_s] = [s]

    return list(anagrams.values())  # Return the grouped anagrams


# Test Case 1:
strings_1 = ["bat", "tab", "name", "mane", "enam", "gabriel", "law"]
print(f"\nTest Case 1: {strings_1}")

# Test case 1 using quicksort
print("Anagram sets using quick_sort:", anagram_sets(strings_1, "quick_sort"))
# Test case 1 using mergesort
print("Anagram sets using merge_sort:", anagram_sets(strings_1, "merge_sort"))

print("-" * 100)

# Test Case 2:
strings_2 = ["176", "761", "ned", "den", "fee", "tree"]
print(f"Test Case 2: {strings_2}")

# Test case using quicksort
print("Anagram sets using quick_sort:", anagram_sets(strings_2, "quick_sort"))
# Test case using mergesort
print("Anagram sets using merge_sort:", anagram_sets(strings_2, "merge_sort"))

print("-" * 100)

# Test Case 3:
strings_3 = ["123", "321", "213", "abc", "cab", "bca", "", " ", "!?!", "!?!"]
print(f"Test Case 3: {strings_3}")

# Test case using quicksort
print("Anagram sets using quick_sort:", anagram_sets(strings_3, "quick_sort"))
# Test case using mergesort
print("Anagram sets using merge_sort:", anagram_sets(strings_3, "merge_sort"))

print("-" * 100)
