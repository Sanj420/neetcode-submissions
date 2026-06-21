class Solution:
    def isValid(self, s: str) -> bool:
        stk = []
        d = {"]":"[", ")":"(", "}":"{"}
        for i in s:
            if i in d:
                if not stk or stk[-1] != d[i]:
                    return False
                stk.pop()
            else:
                stk.append(i)
        return len(stk) == 0