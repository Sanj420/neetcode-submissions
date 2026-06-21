class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = []       
        front = 0
        res = []
        l = 0
        for r in range(len(nums)):
            while len(q) > front and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r)
            if q[front] < l:
                front += 1
            if r + 1 >= k:
                res.append(nums[q[front]])
                l += 1
        return res