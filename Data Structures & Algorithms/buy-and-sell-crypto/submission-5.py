class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buyindex = 0
        sellindex = 0
        arr = [0] * len(prices)

        for i in range(len(prices)):
            print(prices[i] - prices[sellindex])
            if prices[i] - prices[buyindex] >= max(arr):
                sellindex = i
            if prices[i] < prices[buyindex]:
                if (prices[i] < prices[buyindex]):
                    buyindex = i
                    sellindex = i
            
            arr[i] = prices[sellindex] - prices[buyindex]

        return max(arr)    