# solution 1, be careful to type conversion
# class Solution(object):
#     def plusOne(self, digits):
#         """
#         :type digits: List[int]
#         :rtype: List[int]
#         """
#         # s = ''.join(digits) : # @ error,  ''.join(list(str)) instead of list(int)
#         s = ''.join(map(str, digits))
#         d = int(s) + 1
#         sd = str(d)
#         return [int(i) for i in sd]

# solution 2: in-place recursion
class Solution(object):
    def plusOne(self, digits):
        self.recursion(digits, len(digits) - 1)
        return digits
    
    def recursion(self, digits, idx):
        if idx == -1:
            digits[:] = [1] + digits[:]
            return
        if digits[idx] != 9:
            digits[idx] += 1
            return
        else:
            digits[idx] = 0
            self.recursion(digits, idx - 1)
