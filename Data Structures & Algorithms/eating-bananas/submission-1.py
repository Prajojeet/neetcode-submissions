class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # Binary search on values between 0 and greatest number in the list

        hi=max(piles)
        lo=1

        while(hi>lo):
            mid=(hi+lo)//2
            sum=0
            for i in range(len(piles)):
                sum+=(piles[i]+mid-1)//mid
            if sum>h:
                lo=mid+1
            else:
                hi=mid
        
        return lo