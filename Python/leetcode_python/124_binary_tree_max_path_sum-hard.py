class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.max = None
        if root is None:
            return None
        self.helper(root)
        return self.max
    def helper(self, root):
        if root is None:
            return 0
        l = self.helper(root.left)
        r = self.helper(root.right)
        val = root.val
        ret = val + max(0, l) + max(0, r)
        if self.max is None or ret > self.max:
            self.max = ret
        # return ret # wrong ~ @ error
        return max(val, val + l, val + r)
    
# node as pivot node, then it can go as val, val + l, val + r, val + l + r
# however if it is not pivot node (passing up to upper stack), the max can only be among
# val, val + r, val + l
