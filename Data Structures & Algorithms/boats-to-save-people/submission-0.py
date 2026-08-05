class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        output=0
        l=0
        r=len(people)-1
        while(l<=r):
            if l==r:
                output+=1
                return output
            if people[l]+people[r]>limit:
                output+=1
                r-=1
            else:
                output+=1
                l+=1
                r-=1
        return output