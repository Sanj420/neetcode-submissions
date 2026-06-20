class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        x = len(s1)-1
        l = 0
        r = x
        while r<len(s2):
            if sorted(s1) == sorted(s2[l:r+1]):
                return True
            l+=1
            r+=1
        return False