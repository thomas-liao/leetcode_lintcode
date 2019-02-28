# solution 1
# class Solution:
#     def reverse(self, x):
#         temp = x
#         res = 0
#         flag = False
#         if x < 0:
#             flag = True
#             temp = -x
      
#         while temp:
#             d = temp % 10
#             res = 10*res + d
#             temp = temp // 10
#         if flag:
#             res = - res
#         if res < -2**31 or res > 2**31 - 1:
#             return 0
#         return res
            
      
# solution 2:
class Solution:
    def reverse(self, x):
        flag = False
        if x < 0:
            flag = True
            x = - x
        s = list(str(x))[::-1]
        res = int(''.join(s))
        if flag:
            res = - res
        if res < -2**31 or res > 2**31 - 1:
            return 0
        return res
