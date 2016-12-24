"""
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

How many possible unique paths are there?
"""

"""
Solution:
1. there are must be m-1 downward move and n-1 right move
2. calcualte the number of combination
"""

class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        def factorial(num):
        	result = 1
        	while num != 0:
        		result *= num
        		num -= 1
        	return result
        return factorial(m+n-2)/(factorial(n-1)*factorial(m-1))

        