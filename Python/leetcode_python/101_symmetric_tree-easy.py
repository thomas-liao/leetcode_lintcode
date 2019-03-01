# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# solution 1, recursion
# class Solution(object):
#     def isSymmetric(self, root):
#         """
#         :type root: TreeNode
#         :rtype: bool
#         """
#         return self.helper(root, root)
        
#     def helper(self, root1, root2):
#         if not root1 and not root2:
#             return True
#         if not root1 or not root2 or root1.val != root2.val:
#             return False
#         flag_1 = self.helper(root1.left, root2.right)
#         if not flag_1:
#             return False
#         flag_2 = self.helper(root1.right, root2.left)
#         if not flag_2:
#             return False
#         return True
       
        
# solution 2, non-recursion - dfs
class Solution(object):
    def isSymmetric(self, root):
        stack = [(root, root)]
        
        while stack:
            node1, node2 = stack.pop()
            if not node1 and not node2:
                continue
            if not node1 or not node2 or node1.val != node2.val:
                return False
            stack.append((node1.left, node2.right))
            stack.append((node1.right, node2.left))
        return True
        
