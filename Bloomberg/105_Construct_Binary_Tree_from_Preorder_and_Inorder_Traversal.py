"""
Given preorder and inorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.
"""

"""
Solution:
1. preorder defines the root
2. inorder defines the nodes in the left of this root

    4       
   / \      
  2   6
 / \ / \
 1 3 5 7

 preorder: 4,2,1,3,6,5,7
 inorder : 1,2,3,4,5,6,7

first element in preorder is 4 (root)
=> inorder: 1,2,3 | 4 | 5,6,7
             left  node right
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if inorder:
        	val = preorder.pop(0)
        	root = TreeNode(val)
        	index = inorder.index(val)
        	root.left = self.buildTree(preorder, inorder[:index])
        	root.right = self.buildTree(preorder, inorder[index+1:])
        	return root




