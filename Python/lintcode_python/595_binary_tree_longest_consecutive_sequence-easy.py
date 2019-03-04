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
    @return: the length of the longest consecutive sequence path
    """
    def longestConsecutive(self, root):
        # write your code here
        self.max_ = 0
        self.helper(root, None, 0)
        return self.max_
    
    def helper(self, root, prev, count):
        self.max_ = max(self.max_, count)
        if not root:
            return
        if prev is None:
            self.helper(root.left, root.val, 1)
            self.helper(root.right, root.val, 1)
            return
        updatedCount = 1 if root.val != prev + 1 else count + 1
        # self.max_ = max(self.max_, updatedCount) # this line is redundant actually
        self.helper(root.left, root.val, updatedCount)
        self.helper(root.right, root.val, updatedCount)
