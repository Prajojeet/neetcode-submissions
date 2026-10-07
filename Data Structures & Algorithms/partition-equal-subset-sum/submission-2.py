class Solution:
    def canPartition(self, nums: List[int]) -> bool:

        summ = sum(nums)

        if summ%2 != 0:
            return False
        target = summ // 2
        lt = len(nums)
        
        # initialize
        t = [[False for _ in range(target + 1)] for _ in range(lt + 1)]
        
        # if target == 0, always true
        for i in range(lt + 1):
            t[i][0] = True

        # run sum subset simply
        for n in range(1, lt + 1):
            for wei in range(1, target + 1):
                if wei >= nums[n - 1]:
                    t[n][wei] = t[n - 1][wei] or t[n - 1][wei - nums[n - 1]]
                else:
                    t[n][wei] = t[n - 1][wei]
        
        return t[lt][target]

            
