"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.

"""


from ast import List


def longestCommonPrefix(self, strs: List[str]) -> str:
           referencia = strs[0]
           prefix = ""
           for i in range(len(referencia)):
                print(referencia[i])
                for s in strs[1:]:
                     print(s[i])
                     if i >= len(s) or s[i] != referencia[i]:
                        return prefix
                prefix = prefix + s[i]     
           return prefix