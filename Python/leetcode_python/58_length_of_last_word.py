## Solution 1
# class Solution:
#     def lengthOfLastWord(self, s: str) -> int:
#         if not s:
#             return 0
#         s = [token for token in re.findall(r'[a-zA-Z0-9]+', s)]
#         if len(s) == 0:
#             return 0
#         return len(s[-1])

# Solution 2
# class Solution:
#     def lengthOfLastWord(self, s: str) -> int:
#         if not s:
#             return 0
#         idx = len(s) - 1
#         while (idx >= 0 and s[idx] == ' '):
#             idx -= 1
        
#         idx2 = idx
#         while (idx2 >= 0):
#             if s[idx2] != ' ':
#                 idx2 -= 1
#             else:
#                 break
#         return idx - idx2
        
# Solution 3:
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        if not s:
            return 0
        #res = s.split(' ') # wrong, "a " - > ['a', '']
        res = s.split() # right, "a " - >['a']
        print(res)
        if len(res) == 0:
            return 0
        return len(res[-1])
