# You have a bomb to defuse, and your time is running out! Your informer will provide you with a circular array code of length of n and a key k.

# To decrypt the code, you must replace every number. All the numbers are replaced simultaneously.

# If k > 0, replace the ith number with the sum of the next k numbers.
# If k < 0, replace the ith number with the sum of the previous k numbers.
# If k == 0, replace the ith number with 0.
# As code is circular, the next element of code[n-1] is code[0], and the previous element of code[0] is code[n-1].

# Given the circular array code and an integer key k, return the decrypted code to defuse the bomb!


# Example 1:
# Input: code = [5,7,1,4], k = 3
# Output: [12,10,16,13]
# Explanation: Each number is replaced by the sum of the next 3 numbers. The decrypted code is [7+1+4, 1+4+5, 4+5+7, 5+7+1]. Notice that the numbers wrap around.

# Example 2:
# Input: code = [1,2,3,4], k = 0
# Output: [0,0,0,0]
# Explanation: When k is zero, the numbers are replaced by 0. 

# Example 3:
# Input: code = [2,4,9,3], k = -2
# Output: [12,5,6,13]
# Explanation: The decrypted code is [3+9, 2+3, 4+2, 9+4]. Notice that the numbers wrap around again. If k is negative, the sum is of the previous numbers.

## Solution:

from typing import List

class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        n = len(code)
        # Case 1: If k is 0, return all zeros
        if k == 0:
            return [0] * n
        
        # Create a result array and extend the code to handle circularity
        res = [0] * n
        # Doubling the array makes index wrapping much easier
        extended_code = code + code
        
        for i in range(n):
            if k > 0:
                # Sum the next k elements
                # Start at i+1, end at i+k+1
                res[i] = sum(extended_code[i + 1 : i + k + 1])
            else:
                # Sum the previous |k| elements
                # We use (i + n) to ensure we have enough "room" to look back
                # Start at i + n + k, end at i + n
                res[i] = sum(extended_code[i + n + k : i + n])
                
        return res

# Test it out
sol = Solution()
print(f"k=3:  {sol.decrypt([5,7,1,4], 3)}")   # Output: [12, 10, 16, 13]
print(f"k=0:  {sol.decrypt([1,2,3,4], 0)}")   # Output: [0, 0, 0, 0]
print(f"k=-2: {sol.decrypt([2,4,9,3], -2)}")  # Output: [12, 5, 6, 13]
