class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # sliding window baklolwa problem

        l,r,maxx=0,0,0
        hashmap={}
        while(r<len(s)):
            # Add the entry to the dictionary for the number
            if s[r] not in hashmap:
                hashmap[s[r]]=1
            else:
                hashmap[s[r]]+=1

            length=r-l+1

            if length-max(value for value in hashmap.values())>k:
                hashmap[s[l]]-=1
                l+=1
            
            maxx=max(maxx,r-l+1)
            r+=1
        
        return maxx