"""
Implement pow(x, n).
"""

"""
Solution:
1. case x^0: return 1
2. case x^(n < 0): return (1/x)^(n)
3. split the power into sqaure  3^4 = (3*3)^(4/2) = 9^2 = 81^1
"""

class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n is 0:
            return 1.0
        if n < 0:
            x = 1.0/x
            n = -n
        if n%2 == 1:
            return x*self.myPow(x*x, n/2)
        else:
            return self.myPow(x*x,n/2)
