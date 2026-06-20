'''
## Problem
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

 

Example 1:

Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
Example 2:

Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.
 

Constraints:

1 <= prices.length <= 105
0 <= prices[i] <= 104
'''

# submit
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # buy the first day at first.
        buy = prices[0]
        profit = 0
        for i in range(1,len(prices)):
            # in the case of lower price, buy.
            if buy > prices[i]:
                buy = prices[i]
            # in the case of bigger profit, update. 
            elif prices[i] - buy > profit:
                profit = prices[i] - buy
        return profit

'''
## Link
https://leetcode.com/problems/best-time-to-buy-and-sell-stock/submissions/2039345273

## Comment
I wrote it naively, but the result wasn't bad.
The computational complexity itself is not bad, but it seems the execution is slowed down by Python-specific overhead.
'''