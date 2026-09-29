class Solution:
    def validPalindrome(self, s: str) -> bool:
        l = 0 
        r = len(s) - 1
        flag = False

        def Palindrome(l, r):
            while(l < r):
                if s[l] == s[r]:
                    l += 1
                    r -= 1
                else: 
                    return False
            return True
              
        while(l < r):
            if s[l] == s[r]:
                l += 1
                r -= 1
            else:
                if flag == False: 
                    flag = True
                    return Palindrome(l + 1, r) or Palindrome(l, r - 1)
                else: 
                    return False
        return True