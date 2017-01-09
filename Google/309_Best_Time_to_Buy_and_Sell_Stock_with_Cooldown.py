"""
Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete as many transactions as you like (ie, buy one and sell one share of the stock multiple times) with the following restrictions:

You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).
After you sell your stock, you cannot buy stock on next day. (ie, cooldown 1 day)
Example:

prices = [1, 2, 3, 0, 2]
maxProfit = 3
transactions = [buy, sell, cooldown, buy, sell]
"""


"""Solution:
    1. this question can be solved by dp
    2. it may have two different states, cost or profit
    3. we want to find the minimize the cost and maximize the profit
    4. for each cost, the value will be current profit of two day before - price
    5. for each profit, the value will be the price - cost
"""

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices: return 0
        size = len(prices)
        
        cost = [0]*size
        profit = [0]*size
        cost[0] = 0-prices[0]
        for i in range(1,size):
            profit[i] = max(profit[i-1], prices[i] + cost[i-1])
            # Error 1: remember to calculate index 1 seperately
            if i == 1:
                cost[i] = max(cost[i-1], 0 - prices[i])
            else:
                cost[i] = max(cost[i-1], profit[i-2] - prices[i])
        return profit[-1]














