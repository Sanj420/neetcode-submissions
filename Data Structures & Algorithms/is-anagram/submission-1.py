class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        else:
            h = {}
            for i in s:
                h[i] = h.get(i,0) + 1
            for i in t:
                h[i] = h.get(i,0) - 1
            for i in h.values():
                if i!=0:
                    return False
        return True