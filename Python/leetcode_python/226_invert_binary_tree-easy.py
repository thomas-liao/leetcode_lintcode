# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# solution 1, recursion
# class Solution(object):
#     def invertTree(self, root):
#         """
#         :type root: TreeNode
#         :rtype: TreeNode
#         """
#         self.helper(root)
#         return root
    
#     def helper(self, root):
#         if root is None:
#             return
#         self.helper(root.left)
#         self.helper(root.right)
#         root.right, root.left = root.left, root.right
    

    
# # solution 2, other recursion
# class Solution(object):
#     def invertTree(self, root):
#         if not root:
#             return
#         inv = self.invertTree
#         root.left, root.right = inv(root.right), inv(root.left)
#         return root
    
    
# solution 3, iterative
class Solution(object):
    def invertTree(self, root):
        stack = [root]
        while stack:
            node = stack.pop()
            if node:
                node.left, node.right = node.right, node.left
                stack.append(node.left)
                stack.append(node.right)
        return root

# practice again
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return root
        l = self.invertTree(root.left)
        r = self.invertTree(root.right)
        # l, r = r, l# error it doesn't change anything?
        root.left, root.right = r, l
        return root
