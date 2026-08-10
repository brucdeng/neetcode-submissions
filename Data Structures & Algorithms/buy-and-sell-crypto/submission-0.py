class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        minBuy = prices[0]
        for i in range(len(prices)):
            if prices[i] - minBuy > profit:
                profit = prices[i] - minBuy
            if prices[i] < minBuy:
                minBuy = prices[i]
        return profit