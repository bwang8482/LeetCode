"""
Implement int sqrt(int x).

Compute and return the square root of x.
"""

"""Solution:
Binary search:
1. Set L to 0 and R to n − 1.
2. If L > R, the search terminates as unsuccessful.
3. Set m (the position of the middle element) to the floor (the largest previous integer) of (L + R) / 2.
4. If Am < T, set L to m + 1 and go to step 2.
5. If Am > T, set R to m – 1 and go to step 2.
6. Now Am = T, the search is done; return m.
"""

"""Error:
1. mid = left + (right - left) / 2, in case for overflow when left + right
2. mid > x/mid, in case for mid*mid > x when mid*mid overflow
3. left = mid + 1, right = mid - 1
4. condition for left <= right
"""

class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        left = 1
        right = x
        mid = left + (right - left)/2
        ret = 0
        while left <= right:
        	mid = left + (right - left)/2
        	if mid <= x/mid:
        		left = mid + 1
        		ret = mid
        	if mid > x/mid:
        		right = mid - 1
        return ret
