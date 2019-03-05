# solution 1, Counter
# from collections import Counter
# class Solution:
#     def findTheDifference(self, s: str, t: str) -> str:
#         if not s:
#             return t
#         diff = Counter(t) - Counter(s)
#         # return diff.keys()[0] # doesn't work in python3! python 2 returns a list
#         # while python 3 returns dict_keys, which is, can use list() to wrap it to convert
#         # to list
#         return list(diff.keys())[0]


# solution 2, xor
# class Solution:
#     def findTheDifference(self, s: str, t: str) -> str:
#         code = 0
#         for c in s + t:
#             code ^= ord(c)
#         return chr(code)
            
    
# solution 3, math
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        code = 0
        for c in t:
            code += ord(c)
        for c in s:
            code -= ord(c)
        return chr(code)
