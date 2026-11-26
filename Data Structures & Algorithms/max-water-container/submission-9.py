class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1

        maxi = 0

        while(l <= r):
            maxi = max(maxi, (r - l) * min(heights[l], heights[r]))
            print(heights[l], heights[r])

            if heights[l] > heights[r]:
                r -= 1
            elif heights[l] < heights[r]:
                l += 1
            else:
                l += 1
                r -= 1
        return maxi
