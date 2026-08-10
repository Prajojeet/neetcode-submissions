class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        curr_bought=prices[0]
        maximum=0
        for i in range(len(prices)-1):
            if prices[i]>prices[i+1]:
                maximum+=(prices[i]-curr_bought)
                curr_bought=prices[i+1]
        return maximum+(prices[-1]-curr_bought)

            

