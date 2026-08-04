class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
       # Alternate approach of doing thing moving from two sides. 
       # Without division means 
        n=len(nums)
        output=[1]*n
        left=1
        for i in range(0,n-1,1):
            left=left*nums[i]
            output[i+1]=left

        right=1
        for i in range(n-1,0,-1):
            right=right*nums[i]
            output[i-1]=right*output[i-1]

        return output
