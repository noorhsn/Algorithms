# Big O Notation

## Overview

Big O notation is a mathematical notation used to describe the limiting behavior of a function when the argument tends towards a particular value or infinity. In computer science, it's used to classify algorithms according to how their run time or space requirements grow as the input size grows.

## Common Time Complexities

From fastest to slowest:

1. **O(1) - Constant Time**
   - The algorithm takes the same amount of time regardless of input size
   - Example: Accessing an array element by index

2. **O(log n) - Logarithmic Time**
   - The algorithm's running time grows logarithmically with input size
   - Example: Binary search

3. **O(n) - Linear Time**
   - The running time grows linearly with input size
   - Example: Linear search, traversing an array

4. **O(n log n) - Linearithmic Time**
   - Common in efficient sorting algorithms
   - Example: Merge sort, Quick sort (average case)

5. **O(n²) - Quadratic Time**
   - Running time grows quadratically with input size
   - Example: Bubble sort, Selection sort, Insertion sort

6. **O(2ⁿ) - Exponential Time**
   - Running time doubles with each addition to input
   - Example: Recursive Fibonacci (naive implementation)

7. **O(n!) - Factorial Time**
   - Running time grows factorially
   - Example: Generating all permutations

## Space Complexity

Big O notation is also used to describe space complexity:
- How much memory an algorithm uses relative to input size
- Includes both auxiliary space and space used by input

## Best, Average, and Worst Case

- **Best Case**: Minimum time required (often less useful)
- **Average Case**: Expected time for typical input
- **Worst Case**: Maximum time required (most commonly analyzed)

## Examples

```python
# O(1) - Constant
def get_first_element(arr):
    return arr[0]

# O(n) - Linear
def find_max(arr):
    max_val = arr[0]
    for num in arr:
        if num > max_val:
            max_val = num
    return max_val

# O(n²) - Quadratic
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr
```

## Key Takeaways

- Big O describes upper bound (worst case)
- Focus on the dominant term (drop constants and lower-order terms)
- O(3n² + 5n + 2) simplifies to O(n²)
- Helps compare algorithm efficiency
