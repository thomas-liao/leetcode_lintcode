# solution 1, my own version, kind of ugly
# class Solution:
#     def addBinary(self, a: str, b: str) -> str:
#         if not a and not b:
#             return ""
#         if not a:
#             return b
#         if not b:
#             return a
#         result = []
#         self.recursionAddBinary(a, b, result, 0, False)
#         record = map(str, result[::-1])
#         return ''.join(record)

#     def recursionAddBinary(self, a, b, result, idx, carry):
#         len1, len2 = len(a), len(b)
#         if idx == max(len1, len2):
#             if not carry:
#                 return
#             else:
#                 result.append(1)
#                 return
#         new_carry = False
      
#         # @error, indexing: order:   a[0], a[1], a[2]...a[i]
#         #                   reverse: a[-1-0], a[-1-1],  a[-1-2].... a[-1-i]
#         sum_ = carry + (int(a[-idx]) if idx < len1 else 0) + (int(b[-idx]) if idx < len2 else 0)
#         if sum_ >= 2:
#             new_carry = True
#         new_digit = sum_ % 2
#         result.append(new_digit)
#         self.recursionAddBinary(a, b, result, idx + 1, new_carry)

# practice again - recursive
# class Solution:
#     def addBinary(self, a: str, b: str) -> str:
#         if not a and not b:
#             return ""
#         if not a:
#             return b
#         if not b:
#             return a
#         result = []
#         self.recursiveAddBinary(a, b, 0, result, False)
#         # result = map(str, result)[::-1] #@ error, map object is not subscritable
#         result = map(str, result[::-1])
#         return ''.join(result)
        
#     def recursiveAddBinary(self, a, b, idx, result, carry):
#         len1, len2 = len(a), len(b)
#         if idx == max(len1, len2):
#             if not carry:
#                 return
#             else: 
#                 result.append(1)
#                 return
#         sum_ = carry + (int(a[-1-idx] if idx < len1 else 0)) + (int(b[-1-idx] if idx < len2 else 0))
#         new_carry = sum_ >= 2
#         result.append(sum_ % 2)
#         self.recursiveAddBinary(a, b, idx + 1, result, new_carry)



# solution 2, iterative
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        if not a and not b:
            return ""
        if not a:
            return b
        if not b:
            return a
        len1, len2 = len(a), len(b)
        carry = False
        record = []
        for idx in range(max(len1, len2)):
            sum_ = carry + (int(a[-1-idx]) if idx < len1 else 0) + \
            (int(b[-1-idx]) if idx < len2 else 0)
            new_digit = sum_ % 2
            record.append(new_digit)
            carry = sum_ >= 2
        if carry:
            record.append(1)
        
        record = map(str, record[::-1])
        return ''.join(record)
