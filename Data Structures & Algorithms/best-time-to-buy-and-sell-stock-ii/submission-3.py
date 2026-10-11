class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, profit = 0, 0
        for r in range(1, len(prices)):
            if prices[r - 1] > prices[r]:
                if (prices[r - 1] - prices[l]) >= 0:
                    profit += prices[r - 1] - prices[l]
                l = r

        if prices[l] < prices[-1]:
            profit +=  prices[r] - prices[l]
        
        return profit

            

