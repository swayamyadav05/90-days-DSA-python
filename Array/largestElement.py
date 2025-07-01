# Method 1: Using sorted() function (Brute Force)
def largest_element1(arr):
    return sorted(arr)[-1]


# Time Complexity: O(n log n)
# Space Complexity: O(1)


# Method 2: Using max() function (Optimized)
def largest_element(arr):
    max_element = arr[0]
    for i in range(1, len(arr)):
        if arr[i] > max_element:
            max_element = arr[i]
    return max_element


# Time Complexity: O(n)
# Space Complexity: O(1)

arr = [1, 2, 4, 5, 2, 3]
print(largest_element1(arr))
print(largest_element(arr))
