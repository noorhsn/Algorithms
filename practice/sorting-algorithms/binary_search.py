"""
Binary Search Algorithm

Time Complexity: O(log n)
Space Complexity: O(1) for iterative, O(log n) for recursive

Binary search is an efficient algorithm for finding an item from a sorted list.
It works by repeatedly dividing the search interval in half.
"""

def binary_search_iterative(arr, target):
    """
    Iterative implementation of binary search.
    
    Args:
        arr: Sorted list of elements
        target: Element to search for
        
    Returns:
        Index of target if found, -1 otherwise
    """
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = left + (right - left) // 2
        
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1


def binary_search_recursive(arr, target, left=0, right=None):
    """
    Recursive implementation of binary search.
    
    Args:
        arr: Sorted list of elements
        target: Element to search for
        left: Left boundary of search (default: 0)
        right: Right boundary of search (default: len(arr) - 1)
        
    Returns:
        Index of target if found, -1 otherwise
    """
    if right is None:
        right = len(arr) - 1
    
    if left > right:
        return -1
    
    mid = left + (right - left) // 2
    
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search_recursive(arr, target, mid + 1, right)
    else:
        return binary_search_recursive(arr, target, left, mid - 1)


# Example usage
if __name__ == "__main__":
    # Test array (must be sorted)
    numbers = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
    
    print("Array:", numbers)
    print()
    
    # Test iterative version
    print("=== Iterative Binary Search ===")
    test_values = [7, 15, 2, 20]
    
    for value in test_values:
        result = binary_search_iterative(numbers, value)
        if result != -1:
            print(f"Found {value} at index {result}")
        else:
            print(f"{value} not found in array")
    
    print()
    
    # Test recursive version
    print("=== Recursive Binary Search ===")
    for value in test_values:
        result = binary_search_recursive(numbers, value)
        if result != -1:
            print(f"Found {value} at index {result}")
        else:
            print(f"{value} not found in array")
