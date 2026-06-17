class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        cnt = 0
        for i in nums:
            if i-1 not in nums:
                l = 0
                while i+l in nums:
                    l+=1
                cnt = max(l,cnt)
        return cnt