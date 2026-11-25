class Solution:
    def search(self, nums: List[int], target: int) -> int:
        L = 0
        R = len(nums) - 1

        def binarysearch(l, r):
            while(l <= r):
                mid = (l + r)//2

                if nums[mid] == target:
                    return mid
                
                elif nums[mid] < target:
                    l = mid + 1

                else:
                    r = mid - 1
            return -1

        

        while(L <= R):
            MID = (L + R)//2

            if nums[MID] == target:
                return MID

            elif nums[MID] >= nums[L]: # left part is sorted
                if nums[L] <= target < nums[MID]:
                    return binarysearch(L, MID)
                else:
                    L = MID + 1

            elif nums[R] > nums[MID]: # right part is sorted
                if nums[MID] < target <= nums[R]:
                    return binarysearch(MID, R)
                
                else:
                    R = MID - 1

        return -1
                