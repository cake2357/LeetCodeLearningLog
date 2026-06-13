"""
## Problem
Given an integer rowIndex, return the rowIndexth (0-indexed) row of the Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:

Example 1:

Input: rowIndex = 3
Output: [1,3,3,1]
Example 2:

Input: rowIndex = 0
Output: [1]
Example 3:

Input: rowIndex = 1
Output: [1,1]
 

Constraints:

0 <= rowIndex <= 33
 

Follow up: Could you optimize your algorithm to use only O(rowIndex) extra space?

"""

# submit
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex==0:
            return [1]
        elif rowIndex==1:
            return [1,1]
        else:
            dp = [[1], [1,1]]
            for i in range(2,rowIndex+1):
                prevRow = dp[-1]
                newRow = [1]
                for j in range(len(prevRow)-1):
                    newRow.append(prevRow[j] + prevRow[j+1])
                newRow.append(1)
                dp.append(newRow)
        return dp[-1]

"""
## 所感
とりあえず前(118)のを改変して作ろうと思ったら解けてしまった。
問題の難しさを理解できていない。
https://leetcode.com/problems/pascals-triangle-ii/submissions/2031813756
"""