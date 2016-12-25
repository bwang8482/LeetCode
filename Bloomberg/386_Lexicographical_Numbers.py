"""
Given an integer n, return 1 - n in lexicographical order.
For example, given 13, return: [1,10,11,12,13,2,3,4,5,6,7,8,9].
Please optimize your algorithm to use less time and space. The input size may be as large as 5,000,000.
"""

"""
Solution:
1. multiple the previous number by 10: 1 -> 10
2. if the number > n, restore and add 1: 1 -> (10/10 + 1) = 2
3. if the number still > n, repeat the previous step: n = 220, (220*10)/10 + 1 = 221 => 23
4. if the number has a carry, divide to base: 219 -> (220 -> 22)
"""


class Solution(object):
    def lexicalOrder(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        result = [1]
        while len(result) < n:
        	# multiple the previous number
        	new = result[-1] * 10
        	# compute the current number
        	while new > n:
        		new = new/10 + 1
        		while new%10 == 0:
        			new /= 10
        	result.append(new)
        return result








