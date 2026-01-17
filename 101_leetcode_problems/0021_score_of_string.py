# 3110. Score of a String

# You are given a string s. The score of a string is defined as the sum of the absolute difference between the ASCII values of adjacent characters.

# Return the score of s.
 
# Example 1:
# Input: s = "hello"
# Output: 13

# Explanation:
# The ASCII values of the characters in s are: 'h' = 104, 'e' = 101, 'l' = 108, 'o' = 111. So, the score of s would be |104 - 101| + |101 - 108| + |108 - 108| + |108 - 111| = 3 + 7 + 0 + 3 = 13.

# Example 2:
# Input: s = "zaz"
# Output: 50

# Explanation:
# The ASCII values of the characters in s are: 'z' = 122, 'a' = 97. So, the score of s would be |122 - 97| + |97 - 122| = 25 + 25 = 50.

## My Solution (loop through string & calculate score O(n) time & O(1) space)

class Solution:
    def scoreOfString(self, s: str) -> int:
        score = 0
        for char in range(len(s) - 1):
            if ord(s[char]) < ord(s[char + 1]):
                score += ord(s[char + 1]) - ord(s[char])
            else:
                score += ord(s[char]) - ord(s[char + 1])
        return score

