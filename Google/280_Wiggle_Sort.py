"""
Given an unsorted array nums, reorder it in-place such that nums[0] <= nums[1] >= nums[2] <= nums[3]....

For example, given nums = [3, 5, 2, 1, 6, 4], one possible answer is [1, 6, 2, 5, 3, 4].
"""

"""Solution:
    1. for each number, if it does not satisfy the condition, swap it with the previous one
    2. if nums[2] > nums[1], swap nums[1] and nums[2]. 
    3. nums[2] > nums[1] >= nums[0], nums[2] > nums[0] after swaping.
"""

class Solution(object):
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        for i in range(1,len(nums)):
            # Error: use () for each statement
            if (i%2) ^ (nums[i] > nums[i-1]):
                nums[i], nums[i-1] = nums[i-1], nums[i]

