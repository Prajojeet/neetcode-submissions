class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s) - 1
        s = s.lower()
        while(l <= r):
            print(s[l], s[r])
            if s[l].isalnum() and s[r].isalnum():
                if s[l] != s[r]:
                    return False

            if not s[l].isalnum():
                l += 1
            
            elif not s[r].isalnum():
                r -= 1

            else:
                l += 1
                r -= 1

        return True