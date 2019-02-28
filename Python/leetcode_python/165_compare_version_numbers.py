# # solution 1
# # well... my very straightforward(disgusting) solution
# class Solution(object):
#     def compareVersion(self, version1, version2):
#         """
#         :type version1: str
#         :type version2: str
#         :rtype: int
#         """
#         v1 = Element(version1)
#         v2 = Element(version2)
#         if v1 < v2:
#             return -1
#         if v1 > v2: return 1
#         else:
#             return 0
# class Element:
#     def __init__(self, s):
#         temp = map(int, s.split('.'))
#         n = len(temp)
#         if n > 0:
#             self.first = temp[0]
#         else:
#             self.first = 0
#         if n > 1:
#             self.second = temp[1]
#         else:
#             self.second = 0
#         if n > 2:
#             self.third = temp[2]
#         else:
#             self.third = 0
#         if n > 3:
#             self.fourth = temp[3]
#         else:
#             self.fourth = 0
            
#     def __lt__(self, other):
#         if self.first != other.first:
#             return self.first < other.first
#         else:
#             if self.second != other.second:
#                 return self.second < other.second
#             else:
#                 if self.third != other.third:
#                     return self.third < other.third
#                 else:
#                     return self.fourth < other.fourth
            
#     def __eq__(self, other):
#         return self.first == other.first and self.second == other.second and self.third == other.third and self.fourth == other.fourth



# solution 2
class Solution(object):
    def compareVersion(self, version1, version2):
        v1 = map(int, version1.split('.'))
        v2 = map(int, version2.split('.'))
        
        for i in range(max(len(v1), len(v2))):
            a = v1[i] if i < len(v1) else 0
            b = v2[i] if i < len(v2) else 0
            if a > b:
                return 1
            if a < b:
                return -1
        return 0
