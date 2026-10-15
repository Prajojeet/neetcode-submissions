class Solution:
    def canJump(self, nums: List[int]) -> bool:
        MaxInd = 0
        for i, num in enumerate(nums):
            if i > MaxInd:
                return False
            
            MaxInd = max(i + num, MaxInd)

        return True