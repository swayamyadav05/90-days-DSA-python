"""
Problem: Second Largest and Second Smallest Element in an Array

This file demonstrates three approaches to finding the second smallest and second largest elements in an array:
1. Brute Force (Sorting)
2. Two-pass (min/max)
3. One-pass (smart comparison)

Each approach is explained and implemented as a function.
"""


# Approach 1: Brute Force (Sorting)
# ---------------------------------
# Sort the array in ascending order.
# The element at index 1 is the second smallest.
# The element at index -2 is the second largest.
# Note: This approach does NOT handle duplicates correctly.
def get_second_largest_smallest_element1(arr):
    """
    Returns the second smallest and second largest elements in the array using sorting.
    Only works if there are no duplicates.
    Time Complexity: O(n log n)
    Space Complexity: O(1)
    """
    if len(arr) < 2:
        return -1, -1  # Edge case: not enough elements
    arr.sort()
    return arr[1], arr[-2]


# Approach 2: Two-pass (min/max)
# ------------------------------
# First, find the smallest and largest in one pass.
# Then, in a second pass, find the smallest value greater than the smallest (second smallest),
# and the largest value less than the largest (second largest).
def get_second_largest_smallest_element2(arr):
    """
    Returns the second smallest and second largest elements in the array using two traversals.
    Handles duplicates.
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    if len(arr) < 2:
        return -1, -1

    smallest = float("inf")
    second_smallest = float("inf")
    largest = float("-inf")
    second_largest = float("-inf")
    for num in arr:
        if num < smallest:
            smallest = num
        if num > largest:
            largest = num

    for num in arr:
        if num < second_smallest and num != smallest:
            second_smallest = num
        if num > second_largest and num != largest:
            second_largest = num

    # If no valid second smallest/largest found, return -1
    if second_smallest == float("inf"):
        second_smallest = -1
    if second_largest == float("-inf"):
        second_largest = -1
    return second_smallest, second_largest


# Approach 3: One-pass (smart comparison)
# ---------------------------------------
# Use four variables: small, second_small, large, second_large.
# Update them in a single traversal using smart comparisons.
def get_second_small(arr):
    """
    Returns the second smallest element in the array using a single traversal.
    Handles duplicates.
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    if len(arr) < 2:
        return -1
    small = float("inf")
    second_small = float("inf")
    for num in arr:
        if num < small:
            second_small = small
            small = num
        elif num < second_small and num != small:
            second_small = num
    return second_small if second_small != float("inf") else -1


def get_second_large(arr):
    """
    Returns the second largest element in the array using a single traversal.
    Handles duplicates.
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    if len(arr) < 2:
        return -1
    large = float("-inf")
    second_large = float("-inf")
    for num in arr:
        if num > large:
            second_large = large
            large = num
        elif num > second_large and num != large:
            second_large = num
    return second_large if second_large != float("-inf") else -1


if __name__ == "__main__":
    arr = [1, 2, 4, 5, 3]
    print(
        "Approach 1 (Brute Force, no duplicates):",
        get_second_largest_smallest_element1(arr),
    )
    print(
        "Approach 2 (Two-pass, handles duplicates):",
        get_second_largest_smallest_element2(arr),
    )
    print(
        "Approach 3 (One-pass, handles duplicates):",
        get_second_small(arr),
        get_second_large(arr),
    )

    # Example Output:
    # Approach 1 (Brute Force, no duplicates): (2, 4)
    # Approach 2 (Two-pass, handles duplicates): (2, 4)
    # Approach 3 (One-pass, handles duplicates): 2 4
