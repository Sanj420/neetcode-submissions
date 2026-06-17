class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)
        cnt = 0
        for i in nums:
            if i-1 not in numset:
                l = 0
                while i+l in numset:
                    l+=1
                cnt = max(l,cnt)
        return cnt