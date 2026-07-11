class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0

        minPrice = 101

        for price in prices:
            profit = price - minPrice
            maxProfit = max(maxProfit, profit)
            minPrice = min(minPrice, price)


        return maxProfit
        