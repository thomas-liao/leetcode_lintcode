"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: the root of binary tree
    @return: the root of the maximum average of subtree
    """
    def __init__(self):
        self.res = None
        self.avg = None
        
    def findSubtree2(self, root):
        # write your code here
        if not root:
            return root
        self.helper(root)
        return self.res
    
    def helper(self, root):
        if not root:
            return [0, 0]
        l = self.helper(root.left)
        r = self.helper(root.right)
        cur = [l[0] + r[0] + root.val, l[1] + r[1] + 1]
        cur_avg = cur[0] / cur[1]
        if self.avg is None or self.avg < cur_avg:
            self.avg = cur_avg
            self.res = root
        return cur

