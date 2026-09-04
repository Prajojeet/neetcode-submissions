class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        ans=0
        l,r=0,len(people)-1
        while(l<=r):
            if l==r:
                ans+=1
                return ans
            if people[l]+people[r]<=limit:
                l+=1
            ans+=1
            r-=1
        return ans