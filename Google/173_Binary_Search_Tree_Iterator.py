"""
Implement an iterator over a binary search tree (BST). Your iterator will be initialized with the root node of a BST.

Calling next() will return the next smallest number in the BST.

Note: next() and hasNext() should run in average O(1) time and uses O(h) memory, where h is the height of the tree.
"""

"""Solution:
    1. this problem can be solved by stack.
    2. if the stack is not empty, self.hasNext() return True
    3. for each node, if its left child and right child is not None
    4. pop it and push right child first and then the left child
"""

# Definition for a  binary tree node
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator(object):
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.stack = []
        if root != None:
            self.stack.append(root)
        

    def hasNext(self):
        """
        :rtype: bool
        """
        # check if stack is empty
        if not self.stack:
            return False
        # check if the element has been iterated
        while type(self.stack[-1]) is not int:
            node = self.stack.pop()
            if node.right:
                self.stack.append(node.right)
            # I only push the integer value to stack
            self.stack.append(node.val)
            if node.left:
                self.stack.append(node.left)
        return True
        

    def next(self):
        """
        :rtype: int
        """
        return self.stack.pop()

        

# Your BSTIterator will be called like this:
# i, v = BSTIterator(root), []
# while i.hasNext(): v.append(i.next())


"""Summary:
    I only push the value of node we iterated, otherwise, the program will stuck in infinite loop,
unless I change the node.left and node.right to None after traversing.
"""




