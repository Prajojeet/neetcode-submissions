class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        t = [[-1 for _ in range(amount + 1)] for _ in range(len(coins) + 1)]
        # recursive solution
        def dp(n, curr_amount):
            if curr_amount == 0:
                return 0
            if n == -1:
                return float('inf')
            
            if t[n][curr_amount] != -1:
                return t[n][curr_amount]

            if curr_amount >= coins[n]:
                take = 1 + dp(n, curr_amount - coins[n])
                skip = dp(n - 1, curr_amount)
                t[n][curr_amount] = min(take, skip)
                return t[n][curr_amount]
            else:
                skip = dp(n - 1, curr_amount)
                t[n][curr_amount] = skip
                return t[n][curr_amount]
        

        ans = dp(len(coins) - 1, amount)
        return ans if ans != float('inf') else -1