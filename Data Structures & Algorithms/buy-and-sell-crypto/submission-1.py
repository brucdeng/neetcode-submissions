class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        minSeen = prices[0]
        for price in prices:
            if price < minSeen:
                minSeen = price
            profit = max(profit, price - minSeen)
        return profit