class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit, buy, sell = 0, prices[0], 0

        for i in range(1,len(prices)):
            if prices[i] < buy:
                buy = prices[i]
            if prices[i] - buy > profit:
                sell = prices[i] - buy
            
            profit = max(sell, profit)

        return profit
