class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        n=len(s)
        for i in range(n//2):
            temp=s[len(s)-1-i]
            s[len(s)-1-i]=s[i]
            s[i]=temp
        return s

        