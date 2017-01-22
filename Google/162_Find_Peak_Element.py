"""
162. Find Peak Element   Add to List QuestionEditorial Solution  My Submissions
Total Accepted: 96889
Total Submissions: 269821
Difficulty: Medium
Contributors: Admin
A peak element is an element that is greater than its neighbors.

Given an input array where num[i] ≠ num[i+1], find a peak element and return its index.

The array may contain multiple peaks, in that case return the index to any one of the peaks is fine.

You may imagine that num[-1] = num[n] = -∞.

For example, in array [1, 2, 3, 1], 3 is a peak element and your function should return the index number 2.

click to show spoilers.

Note:
Your solution should be in logarithmic complexity.
"""

"""Solution:
    1. this problem can be solved by binary search
    2. if mid and mid+1 is increasing, move left to mid+1. Otherwise, move right to mid - 1
"""


class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)
        left, right = 0, length-1
        while left <= right:
            mid = left + (right - left) / 2
            # Error 1: remember to check boundary of mid+1
            if mid+1 < length and nums[mid] > nums[mid+1]:
                right = mid - 1
            elif mid+1 < length and nums[mid] < nums[mid+1]:
                left = mid + 1
            else:
                return mid
        return left

"""Summary:
    1. binary search only need to check left or right neighbor, no need for both
    2. remember to check the boundary of neighbors
"""


















