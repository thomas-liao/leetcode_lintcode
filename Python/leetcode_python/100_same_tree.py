# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        return self.isSame(p, q)
    
    def isSame(self, p, q):
        if not p and not q:
            return True
        if not p or not q:
            return False
        l = self.isSame(p.left, q.left)
        r = self.isSame(p.right, q.right)
        if not l or not r:
            return False
        return l and r and p.val == q.val
        
