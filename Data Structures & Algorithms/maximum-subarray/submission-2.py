class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n=len(nums)

        pointer=0
        maxx=min(nums[0],0)
        summ=0
        
        for i in range(n):
            if summ<=0:
                summ=0
            summ+=nums[i]
            maxx=max(summ,maxx)
        return maxx
