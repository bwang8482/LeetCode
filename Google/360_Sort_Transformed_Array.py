"""
Given a sorted array of integers nums and integer values a, b and c. Apply a function of the form f(x) = ax2 + bx + c to each element x in the array.

The returned array must be in sorted order.

Expected time complexity: O(n)

Example:
nums = [-4, -2, 2, 4], a = 1, b = 3, c = 5,

Result: [3, 9, 15, 33]

nums = [-4, -2, 2, 4], a = -1, b = 3, c = 5

Result: [-23, -5, 1, 7]
"""

"""Solution:
    1. this question is a sorting problem based on high school math.
    2. the function is a parabola with center point and edges
    3. the max value based on the sign of a.
    4. if a<0 center point -b/(2a) is the maximum point. otherwise, its the smallest point
    5. therefore, running merge sort from two ends to center point.
"""


class Solution(object):
    def sortTransformedArray(self, nums, a, b, c):
        """
        :type nums: List[int]
        :type a: int
        :type b: int
        :type c: int
        :rtype: List[int]
        """
        left, right = 0, len(nums)-1
        ans = []
        # traverse from two ends to center
        if a <= 0:
            while left <= right:
                left_rst = a*nums[left]*nums[left] + b*nums[left] + c
                right_rst = a*nums[right]*nums[right] + b*nums[right] + c
                if left_rst <= right_rst:
                    ans.append(left_rst)
                    left += 1
                else:
                    ans.append(right_rst)
                    right -= 1
        # traverse from center to two ends
        else:
            while left <= right:
                left_rst = a*nums[left]*nums[left] + b*nums[left] + c
                right_rst = a*nums[right]*nums[right] + b*nums[right] + c
                if left_rst >= right_rst:
                    ans.append(left_rst)
                    left += 1
                else:
                    ans.append(right_rst)
                    right -= 1   
            ans = ans[::-1]
        return ans















