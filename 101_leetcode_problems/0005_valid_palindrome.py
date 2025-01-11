# Valid Palindrome (Two Pointer)
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
    # # Method 1 using reversing
    # new_str = ""
    # for c in s:
    #     if c.isalnum():
    #         new_str += c.lower()
    # return new_str == new_str[::-1]

    # Method 2 using two pointers without built functions for alphanumeric
    l, r = 0, len(s) - 1
    while l < r:
        while l < r and not self.alphaNum(s[l]):
            l += 1
        while r > l and not self.alphaNum(s[r]):
            r -= 1
        if s[l].lower() != s[r].lower():
            return False
        l, r = l + 1, r - 1
    return True


def alphaNum(self, c):
    return (ord('A') <= ord(c) <= ord('Z') or
            ord('a') <= ord(c) <= ord('z') or
            ord('0') <= ord(c) <= ord('9'))