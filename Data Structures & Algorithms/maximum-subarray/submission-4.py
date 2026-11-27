class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        summ, maxi = 0, min(nums[0],0)
        l = 0
        for r in range(len(nums)):
            summ += nums[r]
            maxi = max(maxi, summ)
            while(l <= r and summ < 0):
                summ -= nums[l]
                l += 1
        return maxi