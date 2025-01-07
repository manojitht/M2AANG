# Valid Palindrome
# Solved
# Given a string s, return true if it is a palindrome, otherwise return false.
#
# A palindrome is a string that reads the same forward and backward. It is also case-insensitive and ignores all non-alphanumeric characters.
#
# Example 1:
#
# Input: s = "Was it a car or a cat I saw?"
#
# Output: true
# Explanation: After considering only alphanumerical characters we have "wasitacaroracatisaw", which is a palindrome.
#
# Example 2:
#
# Input: s = "tab a cat"
#
# Output: false

# Solution 1
def is_palindrome(self, s: str) -> bool:
    # Method 1 using reversing
    new_str = ""
    for c in s:
        if c.isalnum():
            new_str += c.lower()
    return new_str == new_str[::-1]

    # Method 2 using two pointers without built functions for alphanumeric