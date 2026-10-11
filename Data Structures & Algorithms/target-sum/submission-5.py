class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # Make the dp table as counting one
        summ = sum(nums)
        if abs(target) > abs(summ) or (summ + target) % 2 != 0:
            return 0

        t = [[0 for _ in range(summ + 1)] for _ in range(len(nums) + 1)]

        for i in range(len(nums) + 1):
            t[i][0] = 1

        for n in range(1, len(nums) + 1):
            for s in range(summ + 1):
                if nums[n - 1] <= s:
                    t[n][s] = t[n - 1][s - nums[n - 1]] + t[n - 1][s]
                else:
                    t[n][s] = t[n - 1][s]

        #  s1 = (total + target)/2
        return t[len(nums)][(summ + target)//2]