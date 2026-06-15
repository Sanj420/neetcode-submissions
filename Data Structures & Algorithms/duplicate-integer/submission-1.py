class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hs = set(nums)
        if len(hs)!=len(nums):
            return True
        return False