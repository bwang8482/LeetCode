# You are given two linked lists representing two non-negative numbers. The most significant digit comes first and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

# Follow up:
# What if you cannot modify the input lists? In other words, reversing the lists is not allowed.

# Example:

# Input: (7 -> 2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 8 -> 0 -> 7

"""
Solution:
1. convert linked list to integer
2. add two integers
3. convert integer to linked list
4. corner case 0
"""


class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        
        b = prices[0]
        p = 0
        for i in range(len(prices)):
            if prices[i] < b:
                b = prices[i]
            else:
                p = max(p, prices[i]-b)
        return p