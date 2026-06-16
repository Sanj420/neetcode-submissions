class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        h = {}
        for i in nums:
            h[i] = h.get(i,0)+1
        d = sorted(h.items(), key=lambda x: x[1], reverse = True)
        res = []
        for i in range(k):
            res.append(d[i][0])
        return res