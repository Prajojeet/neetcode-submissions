class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        t = {} # Hashmap because summ can be negative
        def dp(n, summ):
            # Base Case
            if n == -1:
                if summ == target:
                    return 1
                else:
                    return 0

            if (n, summ) in t:
                return t[(n, summ)]
            # Memoization    
            t[(n, summ)] = dp(n - 1, summ + nums[n]) + dp(n - 1, summ - nums[n])
            return t[(n, summ)]

        return dp(len(nums) - 1, 0) 