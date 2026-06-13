"""
## Problem
Given an integer numRows, return the first numRows of Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:

Example 1:

Input: numRows = 5
Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
Example 2:

Input: numRows = 1
Output: [[1]]
 

Constraints:

1 <= numRows <= 30
"""

# submit
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows==1:
            return [[1]]
        elif numRows==2:
            return [[1], [1,1]]
        else:
            dp = [[1], [1,1]]
            for i in range(2,numRows):
                prevRow = dp[-1]
                newRow = [1]
                for j in range(len(prevRow)-1):
                    newRow.append(prevRow[j] + prevRow[j+1])
                newRow.append(1)
                dp.append(newRow)
        return dp

"""
## 所感
DPの考え方はわかってきた。元々軽く勉強していたので、Easyはパスしても良いかもしれない。
https://leetcode.com/problems/pascals-triangle/submissions/2031799464
再帰で解くイメージがあったが、Solutionsを見てもそこまでだった。

"""