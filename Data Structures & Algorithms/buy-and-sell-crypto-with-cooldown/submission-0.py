class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        hold = -prices[0]
        rest = 0
        sell = 0
        
        for i in range(1, n):
            holdtmp = hold
            selltmp = sell
            hold = max(hold, rest - prices[i])
            sell = max(holdtmp + prices[i], rest)
            rest = max(selltmp, rest)

            
        
        return max(hold, rest, sell)
    