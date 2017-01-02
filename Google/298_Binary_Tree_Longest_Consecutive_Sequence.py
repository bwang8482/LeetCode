"""
Given a binary tree, find the length of the longest consecutive sequence path.

The path refers to any sequence of nodes from some starting node to any node in the tree along the parent-child connections. The longest consecutive path need to be from parent to child (cannot be the reverse).

For example,
   1
    \
     3
    / \
   2   4
        \
         5
Longest consecutive sequence path is 3-4-5, so return 3.
   2
    \
     3
    / 
   2    
  / 
 1
Longest consecutive sequence path is 2-3,not3-2-1, so return 2.
"""

"""Solution:
  1. using dfs to traverse everey node
  2. add 1 to length if consecutive
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def longestConsecutive(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # Error 1: boundary check
        if not root:
          return 0
        self.longest = 0
        # Error 2: pass the length
        def dfs(root, length, val):
            if not root:
                return
            if root.val == val:
                length += 1
            else:
                length = 1
            self.longest = max(length, self.longest)
            dfs(root.left, length, root.val + 1)
            dfs(root.right, length, root.val + 1)
        # Error 3: initialized the length to 0 not 1
        # Error 4: store the target value
        dfs(root, 0, root.val)
        return self.longest










