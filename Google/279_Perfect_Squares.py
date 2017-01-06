"""
Given a positive integer n, find the least number of perfect square numbers (for example, 1, 4, 9, 16, ...) which sum to n.

For example, given n = 12, return 3 because 12 = 4 + 4 + 4; given n = 13, return 2 because 13 = 4 + 9.
"""

"""Solution:
    1. using global table to store the numbers
    2. for each n, if table.size is smaller, extend the table with dp
"""

class Solution(object):
    # Tip: declare global table
    _dp = [0]
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = self._dp
        while len(dp) <= n:
            # Error 1: the length should be the length of current dp table
            dp.append(min(dp[-i*i] for i in range(1,int(len(dp)**0.5)+1)) + 1)
        return dp[n]











