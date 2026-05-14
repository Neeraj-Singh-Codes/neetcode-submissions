class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        r = 0
        maxP = 0
        while r < len(prices):
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                maxP = max(maxP, profit)
            else:
                l = r
            
            r += 1
            
        return maxP





















        # buy = 0
        # sell = 1
        # maxProfit = 0
        # while sell < len(prices):
        #     if prices[buy] < prices[sell]:
        #         profit = prices[sell] - prices[buy]
        #         maxProfit = max(profit, maxProfit)
        #     else:
        #         buy = sell
        #     sell += 1
        # return maxProfit