# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# wrong @
# class Solution:
#     def minDepth(self, root: TreeNode) -> int:
#         if not root:
#             return 0
#         return min(self.minDepth(root.left), self.minDepth(root.right)) + 1

# solution 1
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        return self.helper(root)
    
    def helper(self, root):
        if not root.left and not root.right:
            return 1
        if root.left and root.right:
            return min(self.helper(root.left), self.helper(root.right)) + 1
        if root.left:
            return self.helper(root.left) + 1
        if root.right:
            return self.helper(root.right) + 1
        
