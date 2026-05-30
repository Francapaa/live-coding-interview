class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        bestPrice = prices[0]
        maxProfit = 0
        for price in prices:
            if price < bestPrice:
                bestPrice = price
            if price - bestPrice > maxProfit:
                maxProfit = price - bestPrice
        return maxProfit