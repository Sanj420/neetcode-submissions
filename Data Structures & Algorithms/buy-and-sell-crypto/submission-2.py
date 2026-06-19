class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        buy = prices[0]
        for i in prices[1:]:
            buy = min(buy, i)
            res = max(res, i-buy)
        return res