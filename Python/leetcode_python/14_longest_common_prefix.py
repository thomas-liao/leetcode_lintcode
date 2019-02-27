# # too ugly.....
# class Solution:
#     def longestCommonPrefix(self, strs: List[str]) -> str:
#         # corner cases
#         if strs is None:
#             return None
#         if len(strs) == 0:
#             return ""
#         if len(strs) == 1:
#             return strs[0]
#         idx = 0
#         n = len(strs)
#         for i in range(len(strs[0])):
#             c = strs[0][i]
#             for j in range(1, n):
#                 try:
#                     if strs[j][i] != c:
#                         return strs[0][:idx]
#                 except :
#                     return strs[0][:idx]
#             idx += 1
#         return strs[0][:idx]
            
    
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        idx = 0
        for group_ in zip(*strs):
            if len(set(group_)) > 1:
                return strs[0][:idx]
            idx += 1
        # return strs[0] # wrong, ['aa', 'a']
        return strs[0][:idx]
