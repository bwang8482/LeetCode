"""
Given an unsorted array nums, reorder it such that nums[0] < nums[1] > nums[2] < nums[3]....

Example:
(1) Given nums = [1, 5, 1, 1, 6, 4], one possible answer is [1, 4, 1, 5, 1, 6]. 
(2) Given nums = [1, 3, 2, 2, 3, 1], one possible answer is [2, 3, 1, 3, 1, 2].

Note:
You may assume all input has valid answer.

Follow Up:
Can you do it in O(n) time and/or in-place with O(1) extra space?
"""

"""Solution:
    1. this problem can be solved by two pointers
    2. for num in odd position, check if nums[i] > nums[i-1]
    3. for num in even position, check if nums[i] < nums[i-1]
"""

class Solution(object):
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums)):
            if i%2 ^ (nums[i] > nums[i-1]):
                nums[i], nums[i-1] = nums[i-1], nums[i]
"""Summary:
    this solution cannot handle nums with duplicated num. [1,1,1,2,2]
"""

"""Solution:
    1. this problem also can be solved by sort the array first and find the median
    2. placing the number larger than median before median
    3. and placing the number smaller than median after median
    4. translate the index to wiggle sort index
"""
 
# index     : 0 1 2 3 4 5 6 7 8 9
# value     : 9 8 7 6 5 4 3 2 1 0
# wiggle ind: 5 0 6 1 7 2 8 3 9 4
# wiggle val: 4 9 3 8 2 7 1 6 0 5
# => (1 + 2*i) % (size+1)


class Solution(object):
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        self.size = len(nums)
        median = sorted(nums)[]
        i, j, k = 0, 0, self.size - 1
        while j <= k:
            if nums[self.index(j)] > median:
                nums[self.index(i)], nums[self.index(j)] = nums[self.index(j)], nums[self.index(i)]
                i += 1
                j += 1
            elif nums[self.index(j)] < median:
                nums[self.index(k)], nums[self.index(j)] = nums[self.index(j)], nums[self.index(k)]
                k -= 1
            else:
                j += 1

    def index(self, i):
        # index     : 0 1 2 3 4 5 6 7 8 9
        # value     : 9 8 7 6 5 4 3 2 1 0
        # wiggle ind: 5 0 6 1 7 2 8 3 9 4
        # wiggle val: 4 9 3 8 2 7 1 6 0 5
        # => (1 + 2*i) % (size+1)
        return (1 + 2*i) % (self.size | 1)

"""Summary:
    1. this problem uses unsorted array, so we should try three-way partition.
    2. the translate function should be considered carefully
"""








