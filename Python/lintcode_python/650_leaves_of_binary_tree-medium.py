

class Solution:
    """
    @param: root: the root of binary tree
    @return: collect and remove all leaves
    """
    def findLeaves(self, root):
        # write your code here
        if not root:
            return []
        if not root.left and not root.right:
            return [[root.val]]
        dict_ = {}
        n = self.recordDistance(root, dict_)
        ret = {}
        for i in range(1, n + 1):
            ret[i] = []
        
        for node in dict_.keys():
            v = dict_[node]
            ret[v].append(node.val)
        
        ans = []
        print(ret)
        for i in range(1, n + 1):
        # for i in range(1, n + 1)[::-1]:
            ans.append(ret[i])
        return ans
        
    
    def recordDistance(self, root, dict_):
        if not root:
            return 0
        l = self.recordDistance(root.left, dict_)
        r = self.recordDistance(root.right, dict_)
        val = max(l, r) + 1
        dict_[root] = val
        return val
