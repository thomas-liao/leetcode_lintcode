"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

# solution 1, kind of ugly
# the trick is... in helperMethod...
# we simplified the criteria by assigning default number 0 and by
# # 
# class Solution:
#     """
#     @param root: the root of binary tree
#     @return: the length of the longest consecutive sequence path
#     """

#     def longestConsecutive2(self, root):
#         # write your code here
#         self.max_ = 0
#         self.helperMethod(root)
#         return self.max_

#     def helperMethod(self, root):
#         if not root:
#             return [0, 0]
#         # left, incr
#         l = r = [0, 0]
#         if root.left:
#             l = self.helperMethod(root.left)
#             if root.val != root.left.val + 1:
#                 l[0] = 0
#             if root.val != root.left.val - 1:
#                 l[1] = 0

#         if root.right:
#             r = self.helperMethod(root.right)
#             if root.val != root.right.val + 1:
#                 r[0] = 0
#             if root.val != root.right.val - 1:
#                 r[1] = 0
#         record = max(l[0] + r[1], r[0] + l[1]) + 1
#         if record > self.max_:
#             self.max_ = record
#         return [max(l[0], r[0]) + 1, max(l[1], r[1]) + 1]

class Solution:
    """
    @param root: the root of binary tree
    @return: the length of the longest consecutive sequence path
    """

    def longestConsecutive2(self, root):
        if not root:
            return 0
        self.max_ = 0
        self.helper(root)
        return self.max_
        
    def helper(self, root):
        
        if not root:
            return [0, 0]
        # left = right = [0, 0] # this gives wrong answer!!
        ## {10,9,11,8,8,12,12,7,9,#,9,11,13,13,11,#,#,8,10,7,10,12,10,14,14,#,14,10,#,7,9,11,9,6,11,9,11,13,#,#,9,15,13,13,13,13,15,11,#,6} -> 8 instead of 9(9 is expected answer)
        
        ## do not do left = right = [0, 0], VERY WRONG
        # for example
        # left = right = [0, 0]
        # right[0] = 1
        # print(left) --> [1, 0] instead of expected [0, 0] 
        left = [0, 0]
        right = [0, 0]

        if root.left:
            temp = self.helper(root.left)
            if root.val == root.left.val + 1:
                left[0] = temp[0]
            if root.val == root.left.val - 1:
                left[1] = temp[1]
        
        if root.right:
            temp = self.helper(root.right)
            if root.val == root.right.val + 1:
                right[0] = temp[0]
            if root.val == root.right.val - 1:
                right[1] = temp[1]
                
        record = 1 + max(left[0]+right[1], left[1] + right[0])
        self.max_ = max(self.max_, record)

        return [max(left[0], right[0]) + 1, max(left[1], right[1]) + 1] 
