"""
## Problem
You are climbing a staircase.
It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps.
In how many distinct ways can you climb to the top?

Example 1:

Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
Example 2:

Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
 

Constraints:

1 <= n <= 45
"""

# submit
class Solution:
    def climbStairs(self, n: int) -> int:
        """
        i段目に至るまでに、①1段上がるか②2段上がるか。
        ①ならその場合はdp[i-1]通り
        ②ならその場合はdp[i-2]通り
        最後に上がる段数が違うため、重複しないためその和で書ける
        """
        if n<=2:
            return n
        dp = [0]*(n+1)
        dp[1] = 1
        dp[2] = 2
        for i in range(3,n+1):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[n]

"""
シンプルなDPの問題。
https://leetcode.com/problems/climbing-stairs/submissions/2031421901
"""