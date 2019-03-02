# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        if not root:
            return []
        result = []
        self.backtrack(root, sum, 0, [], result)
        return result
    
    def backtrack(self, root, target, cur_sum, subset, result):
        if not root:
            return
        cur_sum += root.val
        subset.append(root.val)
        # leaf node
        if not root.left and not root.right:
            if cur_sum == target:
                result.append(subset.copy())
            subset.pop()
            return
        self.backtrack(root.left, target, cur_sum, subset, result)
        self.backtrack(root.right, target, cur_sum, subset, result)
        subset.pop()
