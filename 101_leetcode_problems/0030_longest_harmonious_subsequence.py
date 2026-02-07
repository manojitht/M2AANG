# 594. Longest Harmonious Subsequence

# We define a harmonious array as an array where the difference between its maximum value and its minimum value is exactly 1.

# Given an integer array nums, return the length of its longest harmonious subsequence among all its possible subsequences.

# Example 1:
# Input: nums = [1,3,2,2,5,2,3,7]
# Output: 5

# Explanation:
# The longest harmonious subsequence is [3,2,2,2,3].

# Example 2:
# Input: nums = [1,2,3,4]
# Output: 2

# Explanation:
# The longest harmonious subsequences are [1,2], [2,3], and [3,4], all of which have a length of 2.

# Example 3:
# Input: nums = [1,1,1,1]
# Output: 0

# Explanation:
# No harmonic subsequence exists.

## My Solution

from typing import List
from collections import Counter

class Solution:
    def findLHS(self, nums: List[int]) -> int:
        if not nums:
            return 0

        freq_count = Counter(nums)
        max_len = 0

        for num in freq_count:
            if num + 1 in freq_count:
                curr_len = freq_count[num] + freq_count[num + 1]
                if curr_len > max_len:
                    max_len = curr_len
        return max_len
    
sol = Solution()
print(sol.findLHS([1,3,2,2,5,2,3,7]))