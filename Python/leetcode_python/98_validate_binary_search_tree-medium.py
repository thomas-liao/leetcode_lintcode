# wrong !!!!!!!!!
# class Solution(object):
#     def isValidBST(self, root):
#         return self.helper(root, None, None)
    
#     def helper(self, root, lb, rb):
#         if not root:
#             return True
#         if lb is not None and rb is not None:
#             return lb < root.val < rb  # wrong... you lb < root.val < rb is true is not enough, we ## still need to examine l and r(next level) in order to determine!!!!
#         if lb is not None:
#             return lb < root.val
#         if rb is not None:
#             return root.val < rb
#         # if not self.helper(root.left, lb, root.val):
#         #     return False
#         # if not self.helper(root.right, root.val, rb):
#         #     return False
#         l = self.helper(root.left, lb, root.val)
#         r = self.helper(root.right, root.val, rb)
#         if not l or not r:
#             return False
#         return True
        
    
# fixed, solution 1
# avoid having too much return and use flag to store your stage..
# most important thing is be organized and make it clear
# class Solution(object):
#     def isValidBST(self, root):
#         return self.helper(root, None, None)
        
#     def helper(self, root, lb, rb):
#         if not root:
#             return True
#         flag1 = True
#         if lb is not None and rb is not None:
#             if not lb < root.val < rb:
#                 flag1 = False
#         if lb is not None:
#             if lb >= root.val:
#                 flag1 = False
#         if rb is not None:
#             if root.val >= rb:
#                 flag1 = False
#         flag2 = self.helper(root.left, lb, root.val) and self.helper(root.right, root.val, rb)
#         return flag1 and flag2


            
            


# solution 2
# use floag(inf)  float('-inf') to make your life easier

class Solution(object):
    def isValidBST(self, root):
        return self._helper(root, float('-inf'), float('inf'))
        
    def _helper(self, root, lb, rb):
        if not root:
            return True
        return (lb < root.val < rb) and self._helper(root.left, lb, root.val) and self._helper(root.right, root.val, rb)
