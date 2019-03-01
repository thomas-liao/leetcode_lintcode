# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# solution 1, recursion
# class Solution(object):
#     def isSameTree(self, p, q):
#         """
#         :type p: TreeNode
#         :type q: TreeNode
#         :rtype: bool
#         """
#         return self.isSame(p, q)
    
#     def isSame(self, p, q):
#         if not p and not q:
#             return True
#         if not p or not q:
#             return False
#         l = self.isSame(p.left, q.left)
#         r = self.isSame(p.right, q.right)
#         if not l or not r:
#             return False
#         return l and r and p.val == q.val


# solution 2: dfs with stack - non-recursive
# class Solution(object):
#     def isSameTree(self, p, q):
#         stack = [(p, q)]
#         while stack:
#             node1, node2 = stack.pop()
#             if not node1 and not node2:
#                 continue
#             if not node1 or not node2 or node1.val != node2.val:
#                 return False
#             stack.append((node1.right, node2.right))
#             stack.append((node1.left, node2.left))
#         return True


# solution 3: bfs with queue (deque or Queue, don't use list for better efficiency)

class Solution(object):
    def isSameTree(self, p, q):
        from collections import deque
        queue = deque()
        queue.append((p, q))
        
        while queue:
            node1, node2 = queue.popleft()
            if not node1 and not node2:
                continue
            if not node1 or not node2 or node1.val != node2.val:
                return False
            queue.append((node1.left, node2.left))
            queue.append((node1.right, node2.right))
        return True
