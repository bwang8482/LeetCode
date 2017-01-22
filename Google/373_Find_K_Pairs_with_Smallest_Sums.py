"""
You are given two integer arrays nums1 and nums2 sorted in ascending order and an integer k.

Define a pair (u,v) which consists of one element from the first array and one element from the second array.

Find the k pairs (u1,v1),(u2,v2) ...(uk,vk) with the smallest sums.

Example 1:
Given nums1 = [1,7,11], nums2 = [2,4,6],  k = 3

Return: [1,2],[1,4],[1,6]

The first 3 pairs are returned from the sequence:
[1,2],[1,4],[1,6],[7,2],[7,4],[11,2],[7,6],[11,4],[11,6]
Example 2:
Given nums1 = [1,1,2], nums2 = [1,2,3],  k = 2

Return: [1,1],[1,1]

The first 2 pairs are returned from the sequence:
[1,1],[1,1],[1,2],[2,1],[1,2],[2,2],[1,3],[1,3],[2,3]
Example 3:
Given nums1 = [1,2], nums2 = [3],  k = 3 

Return: [1,3],[2,3]

All possible pairs are returned from the sequence:
[1,3],[2,3]
"""


"""Solution:
    1. this problem can be solved by priority queue
    2. we need a pair (i,j) to track the location of two pointers for two lists
    3. push i to priority queue and move j to j+1 when pair (i,j) is picked. 
"""

class Solution(object):
    def kSmallestPairs(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[List[int]]
        """
        if not nums1 or not nums2: return []
        queue, ans = [], []
        length1, length2 = len(nums1), len(nums2)
        count = k
        for i in range(min(k, length1)):
            # Tip: using heapq.heappush to push element
            heapq.heappush(queue, (nums1[i] + nums2[0], i, 0))
        # Error 1: remember to check if the queue is emtpy. K may be large
        while count != 0 and queue:
            val, i, j = heapq.heappop(queue)
            ans.append([nums1[i],nums2[j]])
            count -= 1
            if j + 1 < length2:
                heapq.heappush(queue, (nums1[i] + nums2[j+1], i, j+1))
        return ans

"""Summary:
    this problem is actually a two pointers problem, using priority queue to store
the locations of two pointers. 
"""



































