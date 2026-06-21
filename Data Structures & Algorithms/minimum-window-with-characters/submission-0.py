class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s)<len(t) or t == "":
            return ""
        cnT = {}
        window = {}
        res = [-1, -1]
        reslen = float("inf")
        l = 0
        for i in t:
            cnT[i] = cnT.get(i,0) + 1
        have = 0
        need = len(cnT)
        for r in range(len(s)):
            x = s[r]
            window[x] = window.get(x,0) + 1
            if x in cnT and window[x] == cnT[x]:
                have+=1
            while have == need:
                if (r-l+1) < reslen:
                    res = [l,r]
                    reslen = (r-l+1)
                window[s[l]]-=1
                if s[l] in cnT and window[s[l]]<cnT[s[l]]:
                    have-=1
                l+=1
        l,r = res
        return s[l:r+1] if reslen != float("inf") else ""