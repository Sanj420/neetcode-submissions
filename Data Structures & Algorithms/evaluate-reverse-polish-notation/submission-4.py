class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stk = []
        res=0
        for i in tokens:
            if i not in "+-/*":
                stk.append(int(i))
            elif i=="+":
                res=stk[-1]+stk[-2]
                stk.pop()
                stk.pop()
                stk.append(res)
            elif i=="-":
                res=stk[-2]-stk[-1]
                stk.pop()
                stk.pop()
                stk.append(res)
            elif i=="*":
                res=stk[-1]*stk[-2]
                stk.pop()
                stk.pop()
                stk.append(res)
            elif i=="/":
                res=int(stk[-2]/stk[-1])
                stk.pop()
                stk.pop()
                stk.append(res)
        return int(stk[-1])