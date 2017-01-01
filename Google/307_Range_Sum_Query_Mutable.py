"""
Given an integer array nums, find the sum of the elements between indices i and j (i ≤ j), inclusive.

The update(i, val) function modifies nums by updating the element at index i to val.
Example:
Given nums = [1, 3, 5]

sumRange(0, 2) -> 9
update(1, 2)
sumRange(0, 2) -> 8
Note:
The array is only modifiable by the update function.
You may assume the number of calls to update and sumRange function is distributed evenly.
"""

"""Solution:
    1. binary indexed tree
    2. update: index += index & (-index)
    3. sum: index -= index & (-index)
"""

class NumArray(object):
    def __init__(self, nums):
        """
        initialize your data structure here.
        :type nums: List[int]
        """
        self.size = len(nums)
        self.nums = [0]*self.size
        self.array = [0]*(self.size+1)
        # update to initialize
        for i,val in enumerate(nums):
            self.update(i, val)


    def update(self, i, val):
        """
        :type i: int
        :type val: int
        :rtype: int
        """
        # calculate the difference
        val -= self.nums[i]
        # Error 1: sign
        self.nums[i] += val
        index = i + 1
        while index < self.size + 1:
            self.array[index] += val
            index += index & (-index)


    def sumRange(self, i, j):
        """
        sum of elements nums[i..j], inclusive.
        :type i: int
        :type j: int
        :rtype: int
        """
        total = 0
        # Error 2: boundary
        right = j + 1
        left = i
        while right:
            total += self.array[right]
            right -= right & (-right)
        while left:
            total -= self.array[left]
            left -= left & (-left)
        return total


# Your NumArray object will be instantiated and called as such:
# nums = [5,18,13]
# numArray = NumArray(nums)
# print numArray.nums
# print numArray.array
# print numArray.sumRange(0, 2)
# numArray.update(1, -1)
# print numArray.nums
# print numArray.array
# numArray.update(2, 3)
# print numArray.nums
# print numArray.array
# numArray.update(0, 5)
# print numArray.nums
# print numArray.array
# numArray.update(0, -4)
# print numArray.nums
# print numArray.array
# print numArray.sumRange(0, 2)
# numArray = NumArray(nums)

# numArray.sumRange(0, 1)
# numArray.update(1, 10)
# numArray.sumRange(1, 2)
