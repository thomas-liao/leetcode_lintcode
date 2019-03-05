# brute force
# class Solution:
#     def rotateString(self, A: str, B: str) -> bool:
#         if not A and not B:
#             return True
#         if not A or not B:
#             return False
#         if len(A) != len(B):
#             return False
#         for _ in range(len(A)):
#             if A == B:
#                 return True
#             A = self.shiftOne(A)
            
#         return False
    
#     def shiftOne(self, A):
#         # A[:] = A[1:] + A[0], # @ error, str doesn't support assignment -- you can't chagnge in place
#         # A = A[1:] + A[0] doesn't work either (it doesn't throw error, however
#         # you are not getting what you want - A, when comes back to rotateString stack
#         # A doesn't get changed!!
#         # so the only way is, return A[1:] + A[0] and do the reference assignment in rotateString stack
#         return A[1:] + A[0]



# solution 2, super smart --
# if B is a rotation of A, then B is in A+A, however, note the len(A) should = len(B)

class Solution:
    def rotateString(self, A: str, B: str) -> bool:
        if not A and not B:
            return True
        if not A or not B:
            return False
        return len(A) == len(B) and B in A + A
