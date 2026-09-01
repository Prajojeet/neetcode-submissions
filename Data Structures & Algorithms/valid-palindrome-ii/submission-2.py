class Solution:
    def validPalindrome(self, s: str) -> bool:
        def dfs(l,r):
            while l < r:
                if s[l] != s[r]:
                    return False
                else:
                    l+=1
                    r-=1
            return True

        left,right = 0, len(s)-1
        while left < right:
            if s[left] != s[right]:
                return dfs(left+1,right) or dfs(left,right-1)

            left+=1
            right-=1
        return True