class Solution:
    def climbStairs(self, n: int) -> int:
        # # Initiate a memoization array of size n
        # mem = [-1] * (n + 1)

        # # Simple recursive approach
        # def dp(st):
        #     if st == 2:
        #         return 2
            
        #     if st == 1:
        #         return 1
            
        #     if mem[st] != -1:
        #         return mem[st]

        #     mem[st] = dp(st - 1) + dp(st - 2)
        #     return mem[st]

        # return dp(n)

        # Ofcourse as only two variables are needed at each step ie (n - 1) count and (n - 2) stair count, we can easily do without recursion
        prev, curr = 1, 1 # Acting as (n - 2) and (n - 1) state
        for i in range(2, n + 1):
            temp = curr
            curr = prev + curr
            prev = temp
        return curr