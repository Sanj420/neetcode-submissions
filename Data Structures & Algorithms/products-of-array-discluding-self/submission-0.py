class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        prod = 1
        for i in nums:
            prod*=i
        for i in nums:
            if i != 0:
                res.append(int(prod/i))
            else:
                res1 = []
                res1.extend(nums)
                res1.remove(0)
                print(res1)
                prod1 = 1
                for j in res1:
                    prod1*=j
                print(prod1)
                res.append(int(prod1))
        return res