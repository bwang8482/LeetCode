"""
Given a sorted array, remove the duplicates in place such that each element appear only once and return the new length.

Do not allocate extra space for another array, you must do this in place with constant memory.

For example,
Given input array nums = [1,1,2],

Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively. It doesn't matter what you leave beyond the new length.
"""

"""Solution:
1. two pointer to track the array
2. size for non-repeated list and i for traverse position
"""

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        previous = -float('inf')
        size = 0
        for i,num in enumerate(nums):
            if num != previous:
                nums[size] = nums[i]
                size += 1
                previous = num
        return size
