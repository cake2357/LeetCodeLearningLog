'''
## Prooblem

You are given an integer array cost where cost[i] is the cost of ith step on a staircase. Once you pay the cost, you can either climb one or two steps.
You can either start from the step with index 0, or the step with index 1.
Return the minimum cost to reach the top of the floor.


Example 1:
Input: cost = [10,15,20]
Output: 15
Explanation: You will start at index 1.
- Pay 15 and climb two steps to reach the top.
The total cost is 15.
Example 2:

Input: cost = [1,100,1,1,1,100,1,1,100,1]
Output: 6
Explanation: You will start at index 0.
- Pay 1 and climb two steps to reach index 2.
- Pay 1 and climb two steps to reach index 4.
- Pay 1 and climb two steps to reach index 6.
- Pay 1 and climb one step to reach index 7.
- Pay 1 and climb two steps to reach index 9.
- Pay 1 and climb one step to reach the top.
The total cost is 6.
 
Constraints:

2 <= cost.length <= 1000
0 <= cost[i] <= 999

'''

# submit
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # 動的計画法で解く
        ## まずリストを初期化
        n = len(cost)
        # 階段はn段ある。求めたいのはtopなので、1段加えてn+1で初期化（出力はdp[n]）
        dp = [0]*(n+1)

        # 最初は1段か2段を選べる。そのときのコストは0
        dp[0] = 0
        dp[1] = 0

        for i in range(2, n+1):
            # i段目のコストを計算
            dp[i] = min(dp[i-1] + cost[i-1],# 1段前なら1段前のコストを足す
                        dp[i-2] + cost[i-2] # 2段前なら2段前のコストを足す
                        )
        return dp[i]

'''
link: https://leetcode.com/problems/min-cost-climbing-stairs/submissions/2047459759
メモリ効率（空間計算量）は悪い。
ChatGPT（GPT-5.5 Thinking）に聞いたところ、dpをすべて求めているからだそう。
必要なのはdp[n]で、直前の2つの値のみ持っていれば良い。
言われてみればそう。

書かせた改善版コードは以下
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)

        prev2 = 0  # dp[i - 2]
        prev1 = 0  # dp[i - 1]

        for i in range(2, n + 1):
            current = min(
                prev1 + cost[i - 1],
                prev2 + cost[i - 2]
            )

            prev2 = prev1
            prev1 = current

        return prev1
'''