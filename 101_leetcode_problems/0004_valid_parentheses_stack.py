# Valid Parentheses
# Solved
# You are given a string s consisting of the following characters: '(', ')', '{', '}', '[' and ']'.
#
# The input string s is valid if and only if:
#
# Every open bracket is closed by the same type of close bracket.
# Open brackets are closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.
# Return true if s is a valid string, and false otherwise.
#
# Example 1:
#
# Input: s = "[]"
#
# Output: true
# Example 2:
#
# Input: s = "([{}])"
#
# Output: true
# Example 3:
#
# Input: s = "[(])"
#
# Output: false



# Solution 1
def is_valid(self, s: str) -> bool:
    stack = []
    hashmap = {")": "(", "]": "[", "}": "{"}

    for char in s:
        if char in hashmap.keys():
            if stack and stack[-1] == hashmap[char]:
                stack.pop()
            else:
                return False
        else:
            stack.append(char)

    if not stack:
        return True
    else:
        return False

# Approach used Stack data structure Big O is O(n), Space complexity O(n)
