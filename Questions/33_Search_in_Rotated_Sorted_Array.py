"""
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

You are given a target value to search. If found in the array return its index, otherwise return -1.

You may assume no duplicate exists in the array.
"""

"""Solution:
    1. binary search
"""

class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:
            return -1

        left, right = 0, len(nums)-1
        # binary search
        while left <= right:
            mid = left + (right - left)/2
            # if find target
            if nums[mid] == target:
                return mid
            # if left -> mid in order
            elif nums[left] <= nums[mid]:
                # between left and mid
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            # if mid -> right in order
            else:
                # between mid and right
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        return -1





