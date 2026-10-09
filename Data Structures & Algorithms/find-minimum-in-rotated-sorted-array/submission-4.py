class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        lo = 0
        hi = n - 1

        while(lo <= hi):
            mid = (lo + hi)//2
            if nums[mid] <= nums[(mid + 1)%n] and nums[mid] <= nums[(mid + n - 1)%n]:
                return nums[mid]

            elif nums[mid] < nums[hi]:
                hi = mid - 1
            else:
                lo = mid + 1