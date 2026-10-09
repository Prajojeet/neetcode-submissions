class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # (lower bound + 1) i.e mid < target and mid + 1 > target

        lo = 0
        hi = len(nums) - 1
        while(lo <= hi):
            mid = (lo + hi)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                hi = mid - 1
            else:
                lo = mid + 1
        
        return lo