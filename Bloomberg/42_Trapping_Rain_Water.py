"""
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.

For example, 
Given [0,1,0,2,1,0,1,3,2,1,2,1], return 6.
"""

"""
Solution:
1. calculate from two sides.
2. if left lower than right, calculate from left and move right
3. if right lower than left, calculate from right and move left
"""

class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left = 0
        right = len(height) - 1
        left_max = 0
        right_max = 0
        water = 0
        while left <= right:
        	if height[left] <= height[right]:
        		if height[left] > left_max:
        			left_max = height[left]
        		else:
        			water += left_max - height[left]
        		left += 1
        	else:
        		if height[right] > right_max:
        			right_max = height[right]
        		else:
        			water += right_max - height[right]
        		right -= 1
        return water
