class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # Je to kar rakha hai
        vol=0
        l=0
        r=len(heights)-1
        while(r>l):
            vol=max(vol,(min(heights[l],heights[r])*(r-l)))
            if heights[l]<=heights[r]:
                l+=1
            elif heights[l]>heights[r]:
                r-=1
        return vol


