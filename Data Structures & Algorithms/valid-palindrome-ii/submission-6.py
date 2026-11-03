class Solution:
    def validPalindrome(self, s: str) -> bool:
        # whenever we ignore, either from left or right, we have to check from both sides. And return what both say

        def palin(sub):
            print(sub)
            l = 0
            r = len(sub) - 1
            while(l <= r):
                if sub[l] == sub[r]:
                    l += 1
                    r -= 1
                else:
                    return False
            return True

        le = 0
        ri = len(s) - 1
        flag = 0
        while(le <= ri):
            if s[le] == s[ri]:
                le += 1
                ri -= 1
            
            else:
                if flag < 1:
                    flag += 1
                    return palin(s[le + 1:ri + 1]) or palin(s[le:ri])
                else:
                    return False
        return True