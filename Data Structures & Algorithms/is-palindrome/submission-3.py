class Solution:
    def isPalindrome(self, s: str) -> bool:
        res = ""
        for i in s.lower():
            if i.isalnum():
                res+=i
        st = 0
        en = len(res) - 1
        while st <= len(res)-1 and en >= 0:
            if res[st] != res[en]:
                return False
            st+=1
            en-=1
        return True