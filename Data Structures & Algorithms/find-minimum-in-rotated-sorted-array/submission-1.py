class Solution:
    def findMin(self, nums: List[int]) -> int:
        l=0
        r=len(nums)-1
        while(l<r):
            mid=(l+r)//2
            if nums[r]<nums[l]:
                if nums[mid]>=nums[l]:
                    l=mid+1
                elif nums[mid]<nums[l]:
                    r=mid
            else:
                break

        return nums[l]