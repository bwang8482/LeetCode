"""
Follow up for problem "Populating Next Right Pointers in Each Node".

What if the given tree could be any binary tree? Would your previous solution still work?

Note:

You may only use constant extra space.
For example,
Given the following binary tree,
         1
       /  \
      2    3
     / \    \
    4   5    7
After calling your function, the tree should look like:
         1 -> NULL
       /  \
      2 -> 3 -> NULL
     / \    \
    4-> 5 -> 7 -> NULL
"""

"""
Solution 1:
1. constant space to save previous node
2. for each level, save the previous node
3. when another node in the same level, connect the previous to current
"""

# Definition for binary tree with next pointer.
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        level = {}
        def traverse(root, depth):
            if root is None:
              return
            if depth in level:
                level[depth].next = root
            level[depth] = root
            traverse(root.left, depth+1)
            traverse(root.right, depth+1)
            return
        traverse(root, 0)

"""
Solution 2:
1. set pointer
  node -> 1_
(dummy)  /  \
tail -> 2    3
       / \    \
      4   5    7

2. connect next level
    node-> 1_______
          /        \
dummy -> 2(tail) -> 3
        / \          \
       4   5          7

3. move node to next level
             1 -> NULL
            /  \
   node -> 2 -> 3 -> NULL
          / \    \
dummy -> 4-> 5 -> 7 -> NULL

4. traverse all nodes
         1 -> NULL
       /  \
      2 -> 3(node) -> NULL
     / \    \
    4-> 5 -> 7 -> NULL
"""

def connect(self, node):
        head = TreeLinkNode(0)
        cur = head
        while node:
            cur.next = node.left
            if node.left:
                cur = node.left
            cur.next = node.right
            if node.right:
                cur = node.right
            node = node.next
            if not node:
                node = head.next
                cur = head
