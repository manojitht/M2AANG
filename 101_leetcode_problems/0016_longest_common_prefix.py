# 14. Longest Common Prefix

# Write a function to find the longest common prefix string amongst an array of strings.

# If there is no common prefix, return an empty string "".


# Example 1:
# Input: strs = ["flower","flow","flight"]
# Output: "fl"

# Example 2:
# Input: strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.

## Solution (Horizontal Scanning)

from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        
        prefix_list = list(strs[0])
        for word in range(1, len(strs)):
            current_word = strs[word]
            
            if len(current_word) < len(prefix_list):
                prefix_list = prefix_list[:len(current_word)]
                
            for j in range(len(prefix_list)):
                if prefix_list[j] != current_word[j]:
                    prefix_list = prefix_list[:j]
                    break
        
        return "".join(prefix_list)