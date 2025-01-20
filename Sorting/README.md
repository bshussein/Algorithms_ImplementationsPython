# Anagram Grouping with Quicksort and Mergesort

This repository demonstrates an efficient approach to grouping anagrams from a list of strings using sorting algorithms (Quicksort and Mergesort). The project showcases custom implementations of these sorting algorithms and compares their performance.

---

## Features

### **Task Description**
- **Problem**: Given an array of strings, group all anagrams together. An anagram is a word formed by rearranging the letters of another word using all the original letters exactly once.
- **Sorting Algorithms**: Implemented two sorting algorithms (Quicksort and Mergesort) to sort characters in strings and group anagrams based on sorted forms.
- **Functionality**: 
  - `quick_sort`: Sorts an array using the quicksort algorithm.
  - `merge_sort`: Sorts an array using the mergesort algorithm.
  - `sort_string`: Sorts characters in a string using the chosen sorting algorithm.
  - `anagram_sets`: Groups strings into anagram buckets.

---

## Example

### Input:
```python
strings = ["bucket", "rat", "mango", "tango", "ogtan", "tar"]
```
### Output:
```python
[["bucket"], ["rat", "tar"], ["mango"], ["tango", "ogtan"]]
```

---

## How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/<your-username>/Algorithms_ImplementationsPython.git
   ```
2. Navigate to the folder:
   ```bash
   cd Sorting
   ```
3. Run the Python script:
   ```bash
   python anagram_grouping.py
   ```

---

## Test Cases

### Test Case 1:
```python
Input: ["bat", "tab", "name", "mane", "enam", "gabriel", "law"]
Output using quick_sort: [["bat", "tab"], ["name", "mane", "enam"], ["gabriel"], ["law"]]
Output using merge_sort: [["bat", "tab"], ["name", "mane", "enam"], ["gabriel"], ["law"]]
```

### Test Case 2:
```python
Input: ["176", "761", "ned", "den", "fee", "tree"]
Output using quick_sort: [["176", "761"], ["ned", "den"], ["fee"], ["tree"]]
Output using merge_sort: [["176", "761"], ["ned", "den"], ["fee"], ["tree"]]
```

### Test Case 3:
```python
Input: ["123", "321", "213", "abc", "cab", "bca", "", " ", "!?!", "!?!"]
Output using quick_sort: [["123", "321", "213"], ["abc", "cab", "bca"], [""], [" "], ["!?!", "!?!"]]
Output using merge_sort: [["123", "321", "213"], ["abc", "cab", "bca"], [""], [" "], ["!?!", "!?!"]]
```

---

## Learning Outcomes

- Implement and compare sorting algorithms for specific use cases.
- Group anagrams efficiently using character sorting and hash-based grouping.
- Optimize string operations by leveraging custom sorting methods.

---

This project provides a hands-on understanding of sorting algorithms and their applications in solving problems involving grouped data.
