# 28. Find the Index of the First Occurrence in a String

# Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

# Example 1:
# Input: haystack = "sadbutsad", needle = "sad"
# Output: 0
# Explanation: "sad" occurs at index 0 and 6.
# The first occurrence is at index 0, so we return 0.

# Example 2:
# Input: haystack = "leetcode", needle = "leeto"
# Output: -1
# Explanation: "leeto" did not occur in "leetcode", so we return -1.

## Solution (easy: sliding window, hard: KMP algorithm)

from typing import List

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        left = 0
        right = len(needle)

        while right <= len(haystack):
            if haystack[left:right] == needle:
                return left
            else:
                left += 1
                right += 1
        return -1



# #Using for loop:
# class Solution:
#     def strStr(self, haystack: str, needle: str) -> int:
#         # We stop when the remaining string is shorter than needle
#         # range is exclusive, so we add +1
#         for i in range(len(haystack) - len(needle) + 1):
#             if haystack[i : i + len(needle)] == needle:
#                 return i
#         return -1

