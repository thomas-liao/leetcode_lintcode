# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None



# prac 1
# class Solution:
#     def hasPathSum(self, root: TreeNode, sum: int) -> bool:
#         if not root:
#             return False
#         return self.helper(root, sum, 0)
    
#     def helper(self, root, target, cur_sum):
#         if not root:
#             return False
#         cur_sum += root.val
#         if not root.left and not root.right and cur_sum == target:
#             return True
#         if self.helper(root.left, target, cur_sum) or self.helper(root.right, target, cur_sum):
#             return True
#         return False
        
# prac2
class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if not root:
            return False
        if not root.left and not root.right:
            if sum - root.val == 0:
                return True
            else:
                return False
        if self.hasPathSum(root.left, sum - root.val):
            return True
        if self.hasPathSum(root.right, sum - root.val):
            return True
        return False
