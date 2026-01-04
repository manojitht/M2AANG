# Given an array nums of size n, return the majority element.

# The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

 

# Example 1:

# Input: nums = [3,2,3]
# Output: 3
# Example 2:

# Input: nums = [2,2,1,1,1,2,2]
# Output: 2
 

# Constraints:

# n == nums.length
# 1 <= n <= 5 * 104
# -109 <= nums[i] <= 109
# The input is generated such that a majority element will exist in the array.
 

# Follow-up: Could you solve the problem in linear time and in O(1) space?

## Solution: (Boyer Moore's algorithm)


from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # counts = {}
        # sort_counts = []

        # for num in nums:
        #     if num in counts:
        #         counts[num] = counts.get(num) + 1 
        #     else:
        #         counts[num] = 1
        
        # for i in counts.values():
        #     sort_counts.append(i)
        # sort_counts.sort()
        
        # for key, value in counts.items():
        #     if value == sort_counts[-1]:
        #         return key

        candidate = 0
        count = 0

        for num in nums:
            if count == 0:
                candidate = num

            if num == candidate:
                count += 1
            else:
                count -= 1

        return candidate

            

        