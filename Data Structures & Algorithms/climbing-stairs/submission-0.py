class Solution:
    def climbStairs(self, n: int) -> int:
        # Initiate a memoization array of size n
        mem = [-1] * (n + 1)
        def dp(st):
            if st == 2:
                return 2
            
            if st == 1:
                return 1
            
            if mem[st] != -1:
                return mem[st]

            mem[st] = dp(st - 1) + dp(st - 2)
            return mem[st]

        return dp(n)