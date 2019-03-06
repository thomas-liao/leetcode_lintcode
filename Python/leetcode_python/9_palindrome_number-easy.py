# solution 1
# class Solution:
#     def isPalindrome(self, x: int) -> bool:
#         if x < 0:
#             return False
#         rev = 0
#         temp = x
        
#         while temp:
#             digit = temp % 10
#             rev = rev * 10 + digit
#             temp //= 10
        
#         return rev == x

# solution 2
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        org = [e for e in str(x)]
        rev = org[::-1]
        return ''.join(org) == ''.join(rev)
