class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l, poi, r = 0, 0, len(nums) - 1
        while(poi <= r):
            if nums[poi] == 0:
                # replace with left and move the left pointer forward
                nums[poi], nums[l] = nums[l], nums[poi]
                poi += 1
                l += 1

            elif nums[poi] == 2:
                # replace with right pointer
                nums[poi], nums[r] = nums[r], nums[poi]
                r -= 1
            
            else:
                poi += 1