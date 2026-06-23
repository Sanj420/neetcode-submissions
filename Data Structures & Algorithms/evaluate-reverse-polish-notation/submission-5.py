class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stk = []
        ops = {'+', '-', '*', '/'}
        for i in tokens:
            if i not in ops:
                stk.append(int(i))
            else:
                b = stk.pop()
                a = stk.pop() 
                if i == '+':
                    stk.append(a + b)
                elif i == '-':
                    stk.append(a - b)
                elif i == '*':
                    stk.append(a * b)
                elif i == '/':
                    stk.append(int(a / b))
        return stk[0]