# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        if not root:
            return 0
        self.result = 0
        self.recursion(root, sum, [])
        return self.result
    
    def recursion(self, root, target,subset):
        if not root:
            return
        subset.append(root.val)
        # check if there exists path sum
        sum_ = 0
        for i in range(len(subset)):
            sum_ += subset[-1-i]
            if sum_ == target:
                # result.add(tuple(subset[-1-i:].copy))
                # temp = tuple(subset[-1-i:])
                # print("temp: ", temp)
                # result.add(temp) --> tuple, + set, deduplication, #@ error remember you cannot
                # add a list into set() becuase list is mutable while set requires its element
                # being immutable, e.g. tuple()
                self.result += 1
        
        self.recursion(root.left, target, subset)
        self.recursion(root.right, target, subset)
        subset.pop()
