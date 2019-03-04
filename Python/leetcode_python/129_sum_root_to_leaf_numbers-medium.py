# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        if not root:
            return 0
        self.sum_ = 0
        self._sum(root, [])
        return self.sum_
    
    
    def _sum(self, root, subset):
        if not root:
            return
        subset.append(root.val)
        # if leaf node
        if not root.left and not root.right:
            self.sum_ += int(''.join(map(str, subset)))
            subset.pop()
            return
        
        if root.left:
            self._sum(root.left, subset)
        if root.right:
            self._sum(root.right, subset)
        subset.pop()
