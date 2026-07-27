class Solution:
    def search(self, nums: List[int], target: int) -> int:
    # Found the separation
        l, r = 0, len(nums) - 1

        while l < r:
            mid = (l + r) // 2
            
            # If mid element is greater than rightmost element, 
            # the minimum/pivot must be in the right half
            if nums[mid] > nums[r]:
                l = mid + 1
            # Otherwise, the minimum is at mid or in the left half
            else:
                r = mid

        rot = l
    # Find the target in sorted array (Again same binary search)

        l=0
        r=len(nums)-1

        # If target greater than right end, binary search between left and rot-1
        if target>nums[r]:
            rot=rot-1
            while(l<rot):
                mid=(l+rot)//2
                if nums[mid]<target:
                    l=mid+1
                elif nums[mid]>=target:
                    rot=mid
        else:
            while(rot<r):
                mid=(r+rot)//2
                if nums[mid]<target:
                    rot=mid+1
                elif nums[mid]>=target:
                    r=mid             

        if nums[rot]==target:
            return rot
        else:
            return -1
        
