"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Node
        :rtype: int
        """
        if not root:
            return 0
        max_ = 0
        for c in root.children:
            max_ = max(max_, self.maxDepth(c))
        return max_ + 1
