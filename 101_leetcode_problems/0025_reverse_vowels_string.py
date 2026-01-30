# Given a string s, reverse only all the vowels in the string and return it.

# The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.

# Example 1:
# Input: s = "IceCreAm"
# Output: "AceCreIm"

# Explanation:
# The vowels in s are ['I', 'e', 'e', 'A']. On reversing the vowels, s becomes "AceCreIm".

# Example 2:
# Input: s = "leetcode"
# Output: "leotcede"


# Solution:

class Solution:
    def reverseVowels(self, s: str) -> str:
        chars = list(s)
        left = 0
        right = len(s) - 1
        vowels = set("aeiouAEIOU")

        while left < right:
            if chars[left] not in vowels:
                left += 1
            elif chars[right] not in vowels:
                right -= 1
            elif chars[left] in vowels and chars[right] in vowels:
                chars[left], chars[right] = chars[right], chars[left]
                left += 1
                right -= 1
        return "".join(chars)
        
sol = Solution()

testcases = ["IceCreAm", "leetcode", "MaNOjiTh"]

for test in testcases:
    print(sol.reverseVowels(test))