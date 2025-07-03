"""
Problem Statement: Given an array, and an element num the task is to find if num is present in the given array or not. If present print the index of the element or print -1.

Examples:

Example 1:
Input: arr[]= 1 2 3 4 5, num = 3
Output: 2
Explanation: 3 is present in the 2nd index

Example 2:
Input: arr[]= 5 4 3 2 1, num = 5
Output: 0
Explanation: 5 is present in the 0th index
"""

"""
Approach:
Given an array
We will traverse the whole array and see if the element is present in the array or not
If found we will print the index of the element
Otherwise, we will print -1.
"""


def search(nums: list, num: int):
    for i in range(len(nums)):
        if nums[i] == num:
            return i

    return -1


arr = [1, 2, 4, 5, 6, 8]
num = 8
val = search(arr, num)
print(val)

# Time Complexity: O(n), where n is the length of the array.

# Space Complexity: O(1)
