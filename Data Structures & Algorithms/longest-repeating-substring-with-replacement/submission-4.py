class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l,r,maxx=0,0,0

        # Frequency of letters in that particular window
        hashmap={}
        
        while(r<len(s)):

            # Adding to the hashmap
            if s[r] not in hashmap:
                hashmap[s[r]]=1
            else: 
                hashmap[s[r]]+=1

            
            # Condition
            condition=(r-l+1)-max(hashmap.values())
            if condition<=k:
                maxx=max(maxx,(r-l+1))
            else:
                if hashmap[s[l]]==1:
                    hashmap.pop(s[l])
                else:
                    hashmap[s[l]]-=1
                l+=1
            r+=1
            
        return maxx
            