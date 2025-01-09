# Contains Duplicate (Array & Hashing)
# Solved
# Given an integer array nums, return true if any value appears more than once in the array, otherwise return false.
#
# Example 1:
#
# Input: nums = [1, 2, 3, 3]
#
# Output: true
#
# Example 2:
#
# Input: nums = [1, 2, 3, 4]
#
# Output: false


# Solution 1:

def has_duplicate_one(nums):
    temp_arr = set(nums)
    if len(temp_arr) == len(nums):
        return False
    elif len(temp_arr) != len(nums):
        return True

# Solution 2:

def has_duplicate_two(nums):
    hashset = set()
    for i in nums:
        if i in hashset:
            return True
        hashset.add(i)
    return False

