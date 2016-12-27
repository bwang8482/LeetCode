"""
Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.

Note:
You may assume that nums1 has enough space (size that is greater or equal to m + n) to hold additional elements from nums2. The number of elements initialized in nums1 and nums2 are m and n respectively.
"""

"""
Solution:
1. traverse two array from right to left
"""

class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        # remember to handle the rest of list
        pointer_m = m - 1
        pointer_n = n - 1
        for i in range(m + n):
        	index = m + n - i - 1
        	if pointer_m < 0:
        		while pointer_n >= 0:
        			nums1[pointer_n] = nums2[pointer_n]
        			pointer_n -= 1
        		return	
        	if pointer_n < 0:
        		return
        	if nums1[pointer_m] >= nums2[pointer_n]:
        		nums1[index] = nums1[pointer_m]
        		pointer_m -= 1
        	else:
        		nums1[index] = nums2[pointer_n]
        		pointer_n -= 1

