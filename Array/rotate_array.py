"""
Problem: Left Rotate the Array

Given an array of integers `nums` and an integer `d`, perform the following operation:

Left Rotate by d Places:
Move each element of the array `d` positions to the left, and move the first `d` elements to the end of the array in the same order.
Return the resulting array.

Example 1
Input:
  nums = [1, 2, 3, 4, 5], d = 2
Output:
  Left Rotate by d Places: [3, 4, 5, 1, 2]

Example 2
Input:
  nums = [10, 20, 30, 40], d = 3
Output:
  Left Rotate by d Places: [40, 10, 20, 30]

Constraints
  1 ≤ nums.length ≤ 10^4
  1 ≤ nums[i] ≤ 10^9
  1 ≤ d ≤ nums.length

Follow-up
  Can you solve the rotation in-place with O(1) extra space?
"""

# Approach 1:

from typing import List


def rotate(self, nums: List[int], k: int) -> None:
    n = len(nums)
    temp = []
    for i in range(k):
        temp.append(nums[i])
    print(f"temp: {temp}")

    for i in range(k, n):
        nums[i - k] = nums[i]

    for i in range(n - k, n):
        nums[i] = temp[i - (n - k)]


# Time Complexity: O(n + k) where n is the length of the array and k is the number of places to rotate.
# The first loop runs k times to fill the temporary array, and the second loop runs n-k times to shift elements.
# Space Complexity: O(k) for the temporary array


# Approach 2: Using Slicing (Pythonic way)
def rotate(self, nums: List[int], d: int) -> None:
    n = len(nums)
    d = d % n  # Handle cases where d >= n
    nums[:] = nums[d:] + nums[:d]  # Rotate using slicing


# Time Complexity: O(n) where n is the length of the array.
# Space Complexity: O(n) for the new list created by slicing, but in-place modification of nums is done.


# Right Rotate the array by d places
# Approach 1:
def rotate_right(self, nums: List[int], d: int) -> None:
    n = len(nums)
    d = d % n  # Handle cases where d >= n

    temp = []
    for i in range(n - d):
        temp.append(nums[i])

    for i in range(n - d, n):
        nums[i - (n - d)] = nums[i]

    for i in range(d, n):
        nums[i] = temp[i - d]


# Time Complexity: O(n + d) where n is the length of the array and d is the number of places to rotate.
# Space Complexity: O(d) for the temporary array


# Approach 3: Using Reverse (In-place)
def rotate_in_place(self, nums: List[int], d: int) -> None:
    n = len(nums)
    d = d % n  # Handle cases where d >= n

    # Helper function to reverse a portion of the array
    def reverse(start: int, end: int) -> None:
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1

    # Reverse the elements from 0 to d
    reverse(0, d - 1)
    # Reverse the elements from d to n
    reverse(d, n - 1)
    # Reverse the entire array
    reverse(0, n - 1)

    # For rotate in-place but from right
    # reverse(0, n - 1)  # Reverse the entire array
    # reverse(0, d - 1)  # Reverse the first d elements
    # reverse(d, n - 1)  # Reverse the last d elements


# Time Complexity: O(n) where n is the length of the array.
# Space Complexity: O(1) since we are reversing in-place without using extra space.

if __name__ == "__main__":
    nums = [1, 2, 3, 4, 5, 6, 7]
    d = 2
    rotate(None, nums, d)
    print("Left Rotate by d Place:", nums)  # Output: [3, 4, 5, 6, 7, 1, 2]

    nums = [1, 2, 3, 4, 5, 6, 7]
    d = 2
    rotate_in_place(None, nums, d)
    print("Left Rotate by d Place (In-place):", nums)  # Output: [3, 4, 5, 6, 7, 1, 2]

    nums = [10, 20, 30, 40, 50, 60, 70]
    d = 3
    rotate(None, nums, d)
    print("Left Rotate by d Places:", nums)  # Output: [40, 10, 20, 30]

    nums = [-1]
    d = 2
    rotate_right(None, nums, d)
    print("Right Rotate by d Places:", nums)  # Output: [-1]
