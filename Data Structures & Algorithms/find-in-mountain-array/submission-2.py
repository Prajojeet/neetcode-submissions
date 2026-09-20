class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        l = 0 
        r = mountainArr.length() - 1

        # return the peak index
        while(l < r):
            mid = (l + r)//2

            if mountainArr.get(mid) < mountainArr.get(mid + 1):
                l = mid + 1
            else:
                r = mid

        peak_index = l
        # peak_index contains the peak element
        # run two binary search (0 - peak_index) and (peak_index + 1, r - 1)  
        l = 0 
        r = peak_index
        while(l <= r):
            mid = (l + r)//2
            mid_term = mountainArr.get(mid)

            if mid_term == target:
                return mid
            elif mid_term > target: 
                r = mid - 1
            else:
                l = mid + 1
            
        l = peak_index + 1
        r = mountainArr.length() - 1
        while(l <= r):
            mid = (l + r)//2
            mid_term = mountainArr.get(mid)

            if mid_term == target:
                return mid
            elif mid_term > target: 
                l = mid + 1
            else:
                r = mid - 1

        return -1