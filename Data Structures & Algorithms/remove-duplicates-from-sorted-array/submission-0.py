class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n=len(nums)
        duplicates=0
        for i in range(1,n,1):
            if nums[i-1]==nums[i]:
                duplicates+=1
            nums[i-duplicates]=nums[i]
        
        return n-duplicates