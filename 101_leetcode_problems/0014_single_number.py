# 136. Single Number

# Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

# You must implement a solution with a linear runtime complexity and use only constant extra space.

 
# Example 1:
# Input: nums = [2,2,1]
# Output: 1

# Example 2:
# Input: nums = [4,1,2,1,2]
# Output: 4

# Example 3:
# Input: nums = [1]
# Output: 1

 
# Constraints:
# 1 <= nums.length <= 3 * 104
# -3 * 104 <= nums[i] <= 3 * 104
# Each element in the array appears twice except for one element which appears only once.


## Solution (using XOR operation)
class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        result = 0
        for num in nums:
            result ^= num
        return result
    
## Alternative Solution (using dict to find the single number - My solution)
class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        num_dict = {}
        for num in nums:
            if num in num_dict:
                del num_dict[num]
            else:
                num_dict[num] = 1
        return list(num_dict.keys())[0]

# or
class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        nums_dict = {}

        for num in nums:
            if num in nums_dict:
                nums_dict[num] = nums_dict[num] + 1
            else:
                nums_dict[num] = 1
        return [k for k, v in nums_dict.items() if 1 == v][0]