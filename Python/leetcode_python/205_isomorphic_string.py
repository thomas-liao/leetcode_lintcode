# failed case: "ab" - >"aa", fixed by adding if len(set(mapping.keys())) != .....
# class Solution:
#     def isIsomorphic(self, s: str, t: str) -> bool:
#         if not s and not t:
#             return True
#         if len(s) != len(t):
#             return False
#         mapping = {}
#         for a, b in zip(s, t):
#             if a not in mapping.keys():
#                 mapping[a] = b
#                 if len(set(mapping.keys())) != len(set(mapping.values())):
#                     return False
#             else:
#                 if mapping[a] != b:
#                     return False
#         return True


# solution 2
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        return len(set(zip(s, t))) == len(set(s)) == len(set(t))
        
