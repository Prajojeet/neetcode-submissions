class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        vol = 0

        while(l < r):
            vol = max(vol, min(heights[r], heights[l])*(r - l))
            if heights[l] < heights[r]:
                l += 1
            elif heights[l] > heights[r]:
                r -= 1
            else: # otherwise the vol will decrease only
                l += 1
                r -= 1
        return vol