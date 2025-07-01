"""
Problem: Check if the array is sorted in ascending order

This file provides a function to check whether a given array is sorted in ascending order.
It demonstrates a simple linear scan approach.
"""


def is_sorted(arr):
    """
    Returns True if the array is sorted in ascending order, False otherwise.
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    # Iterate through the array and compare each element with the previous one
    for i in range(1, len(arr)):
        if arr[i] < arr[i - 1]:
            return False  # Found a pair out of order
    return True  # All pairs are in order


# Example usage
if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5]
    print("Is the array sorted in ascending order?", is_sorted(arr))  # Output: True

    arr2 = [5, 3, 2, 1]
    print("Is the array sorted in ascending order?", is_sorted(arr2))  # Output: False

    # Example Output:
    # Is the array sorted in ascending order? True
    # Is the array sorted in ascending order? False
