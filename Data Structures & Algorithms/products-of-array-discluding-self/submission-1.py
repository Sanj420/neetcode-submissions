class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1]
        pre = 1
        post = 1
        for i in range(len(nums)-1):
            pre*=nums[i]
            res.append(pre)
        for i in range(len(nums)-1,-1,-1):
            res[i]*=post
            post*=nums[i]
        return res