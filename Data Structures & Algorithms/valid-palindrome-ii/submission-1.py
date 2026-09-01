class Solution:

    def validPalindrome(self, s: str) -> bool:
        counter=0
        l=0
        r=len(s)-1


        # Helper function
        def palin(l, r):
            while(l<r):
                if s[l]!=s[r]:
                    return False
                l+=1
                r-=1
            return True

        while(l<r):
            if s[l]!=s[r]:
                if counter>0:
                    return False
                else:
                    counter+=1
                    return palin(l+1,r) or palin(l,r-1)
            l+=1
            r-=1
        
        return True