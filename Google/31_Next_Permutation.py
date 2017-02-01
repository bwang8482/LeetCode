"""
Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.

If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).

The replacement must be in-place, do not allocate extra memory.

Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.
1,2,3 → 1,3,2
3,2,1 → 1,2,3
1,1,5 → 1,5,1
"""


"""Solution:
    1. this problem have 2 sub-problems:
        1) find next permutation if exist
        2) find lowest permutation if no next permutation
    2. in order to find next permutation: we should check from right to left
        1) if nums[i] < nums[j], sort array nums[j:]
        2) swap the smallest value that larger than nums[i] with nums[i]
    3. if no next permutation, sort array lexicographically
"""

class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if not nums or len(nums) == 1:
            return
        length = len(nums)
        i, j = length - 2, length - 1
        while i >= 0:
            # Error 2: use int not str for lexicographically
            if nums[j] > nums[i]:
                # Error 1: sort nums[j:]
                nums[:] = nums[:j] + sorted(nums[j:])
                while nums[j] <= nums[i] and j < length - 1:
                    j += 1
                nums[j], nums[i] = nums[i], nums[j]
                return
            else:
                i -= 1
                j -= 1
        # Error 3: using nums[:] instead of nums to sort in place
        nums[:] = sorted(nums)
        return

"""Summary:
    1. the key idea is the same but I didn't figure out sorting nums[j:]
    2. lexicographically order is confused. 11 should < 3 but 11 > 3 in the problem.
"""




