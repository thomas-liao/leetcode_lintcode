# # solution 1, ugly
# class Solution(object):
#     def myAtoi(self, str):
#         """
#         :type str: str
#         :rtype: int
#         """
#         if not str:
#             return 0
#         s = str.strip()
#         neg_flag = False
        
#         start_idx = 0
#         end_idx = 0
#         for i in range(len(s)):
#             if i == 0 and s[i] == '-':
#                 neg_flag = True
#                 start_idx += 1
#                 continue
#             if i == 0 and s[i] == '+':
#                 start_idx += 1
#                 continue
#             if i == 0 and s[i] != '-' and not s[i].isdigit():
#                 return 0
#             if s[i].isdigit():
#                 end_idx = i
#             else:
#                 break
#         val = ''.join(list(s)[start_idx : end_idx + 1])
#         if len(val) == 0:
#             return 0
#         val = int(val)
#         if neg_flag:
#             val = - val
#         if val < -2**31 or val > 2**31 - 1:
#             if val < 0:
#                 return -2**31
#             else:
#                 return 2**31 - 1
#         return val

# solution 2
class Solution(object):
    def myAtoi(self, str):
        res = re.search('^[+|-]?\d+', str.strip())
        if res:
            res = int(res.group())
        else:
            return 0
        if res > 2**31 - 1:
            return 2**31 - 1
        if res < -2**31:
            return -2**31
        return res:
