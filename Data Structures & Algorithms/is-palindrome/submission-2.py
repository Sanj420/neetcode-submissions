class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        res = ""
        for i in s:
            if i.isalnum():
                res+=i
        print(res)
        if res == res[::-1]:
            return True
        return False