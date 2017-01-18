"""
Find the kth largest element in an unsorted array. Note that it is the kth largest element in the sorted order, not the kth distinct element.

For example,
Given [3,2,1,5,6,4] and k = 2, return 5.

Note: 
You may assume k is always valid, 1 ≤ k ≤ array's length.
"""

"""Solution:
quicksort:
1. Initialize left to be 0 and right to be nums.size() - 1;
2. Partition the array, if the pivot is at the k-1-th position, return it (we are done);
3. If the pivot is right to the k-1-th position, update right to be the left neighbor of the pivot;
4. Else update left to be the right neighbor of the pivot.
5. Repeat 2.
"""

class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        def partition(nums, l, r):
        	pivot = nums[l]
        	index = l
        	l += 1
        	while l <= r:
        		print nums[l]
        		print nums[r]
        		if nums[l] > pivot and nums[r] < pivot:
        			temp = nums[l]
        			nums[l] = nums[r]
        			nums[r] = temp
        		elif nums[l] <= pivot:
        			l += 1
        		elif nums[r] >= pivot:
        			r += 1
        	nums[index] = nums[r]
        	nums[r] = pivot
        	return r

        k = len(nums) - k
        left, right = 0, len(nums)-1
        while True:
        	index = partition(nums, left, right)
        	if index == k:
        		return nums[index]
        	if index < k:
        		left = index + 1
        	else:
        		right = index - 1






