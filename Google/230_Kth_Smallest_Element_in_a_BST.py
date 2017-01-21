"""
Given a binary search tree, write a function kthSmallest to find the kth smallest element in it.

Note: 
You may assume k is always valid, 1 ≤ k ≤ BST's total elements.

Follow up:
What if the BST is modified (insert/delete operations) often and you need to find the kth smallest frequently? How would you optimize the kthSmallest routine?
"""


"""Solution 1: dfs
    1. using in-order traverse with recursion
    2. return the node when node visited is k 
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        self.count, self.ans = k, None
        self.dfs(root)
        return self.ans

    def dfs(self, root):
        if root is None: return
        self.dfs(root.left)
        self.count -= 1
        if self.count == 0:
            # Error 1: using self.ans to store answer
            self.ans = root.val
            return
        self.dfs(root.right)

"""Summary:
    1. the algorithm will traverse every node until the kth smallest node.
    2. the run time is O(k)
    3. we could use binary search to reduce the runtime to O(logk)
"""


"""Solution 2: dfs with binary search
    1. using dfs to count the number of node that smaller than current node
    2. using binary search to decide to traverse left or right child.
    3. avoid useless traversing.
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        if root is None: return None
        # Error 1: remember to count the number of node in left child
        count = self.dfs(root.left)
        if count < k-1:
            return self.kthSmallest(root.right, k-1-count)
        elif count > k-1:
            return self.kthSmallest(root.left, k)
        return root.val

    def dfs(self, root):
        return 0 if root == None else 1 + self.dfs(root.left) + self.dfs(root.right)

"""Summary:
    1. the binary search dfs has no significant runtime improvement.
    2. the count function needs many redundant traverses for each node.
"""

























