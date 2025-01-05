# Two Sum
# Solved
# Given an array of integers nums and an integer target, return the indices i and j such that nums[i] + nums[j] == target and i != j.
#
# You may assume that every input has exactly one pair of indices i and j that satisfy the condition.
#
# Return the answer with the smaller index first.
#
# Example 1:
#
# Input:
# nums = [3,4,5,6], target = 7
#
# Output: [0,1]
# Explanation: nums[0] + nums[1] == 7, so we return [0, 1].
#
# Example 2:
#
# Input: nums = [4,5,6], target = 10
#
# Output: [0,2]
# Example 3:
#
# Input: nums = [5,5], target = 10
#
# Output: [0,1]

# Solution

def two_sum( nums, target):
    # Solution 1 - Brute Force
    # count = 0
    # while len(nums) != count:
    #     for i in range(len(nums)):
    #         if nums[count] + nums[i] == target and count != i:
    #             return [count, i]
    #             break
    #     count += 1

    # Solution 2 - Hash Map
    hash_map = {}
    for index, value in enumerate(nums):
        num = target - value
        if num in hash_map:
            return [hash_map[num], index]
        hash_map[value] = index
