'''
## Problem Description
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

 

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
 

Constraints:

1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lowercase English letters if it is non-empty.
'''

## submit
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        min_length = min(len(s) for s in strs)

        for i in range(min_length):
            tmp_char = strs[0][i]
            for s in strs[1:]:
                if s[i] != tmp_char:
                    return strs[0][:i]

        return strs[0][:min_length]
    
'''
https://leetcode.com/problems/longest-common-prefix/submissions/2071664885
パッとアイデアが出て良かった。
'''
