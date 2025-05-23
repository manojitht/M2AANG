# Valid Anagram (Array and Hashing)
# Solved
# Given two strings s and t, return true if the two strings are anagrams of each other, otherwise return false.
#
# An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.
#
# Example 1:
#
# Input: s = "racecar", t = "carrace"
#
# Output: true
# Example 2:
#
# Input: s = "jar", t = "jam"
#
# Output: false
# Constraints:
#
# s and t consist of lowercase English letters.

# Solution

def is_anagram(s: str, t: str):
    if len(s) != len(t):
        return False
    if "".join(sorted(s)) == "".join(sorted(t)):
        return True
    else:
        return False