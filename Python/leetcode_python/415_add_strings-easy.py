# now allowed!
# class Solution:
#     def addStrings(self, num1: str, num2: str) -> str:
#         if not num1 and not num2:
#             return None
#         return str(int(num1) + int(num2))


# solution
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        n1 = [int(c) for c in num1]
        n2 = [int(c) for c in num2]
        
        carry = 0
        res = []
        while n1 or n2:
            digit = (n1.pop() if n1 else 0) + (n2.pop() if n2 else 0) + carry
            if digit > 9:
                carry = 1
                digit = digit % 10
            else:
                carry = 0
            
            res.append(digit)
                
        if carry:
            res.append(carry)
        
        return ''.join(map(str, res[::-1]))   
