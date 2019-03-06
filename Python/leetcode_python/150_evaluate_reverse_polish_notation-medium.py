class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        assert len(tokens) > 0
        stack = []
        
        for e in tokens:
            if e not in ['+', '-', '*', '/']:
                stack.append(e)
            else:
                r, l = int(stack.pop()), int(stack.pop())
                # print("r: ", r, " l: ", l, " e: ", e)
                if e == '+':
                    stack.append(l + r)
                elif e == '-':
                    stack.append(l - r)
                elif e == '*':
                    stack.append(l * r)
                else:
                    # corner case:
                    # -1 // 22 = -1 instead of 0....
                    # -33 // 22 = -2 instead of -1...
                    # neg // pos or pos // neg doesn't behave like you think sometimes
                    if l * r >= 0:
                        stack.append(abs(l) // abs(r))
                    else:
                        stack.append(-1*(abs(l) // abs(r)))
        return int(stack.pop())
                        
                        
        
