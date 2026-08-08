class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s)==1 or len(s)==0:
            return len(s)
        l=0
        r=1
        long=0
        counter={}
        counter[s[l]]=l # First element saved
        while(r<len(s)):
            if s[r] not in counter:
                counter[s[r]]=r
                long=max(long,r-l+1)
                r+=1
            else:
                if counter[s[r]]<l:
                    counter[s[r]]=r
                    long=max(long,r-l+1)
                    r+=1
                else:
                    l=counter[s[r]]+1
                    counter[s[r]]=r
                    long=max(long,r-l+1)
                    r+=1
        return long
        