class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        rev = s[::-1]
        l = len(s)
        dp = [[0] * (l + 1) for _ in range(l + 1)]

        for m in range(1, l + 1):
            for n in range(1, l + 1):
                if m == 0 or n == 0:
                    return 0
                if s[m - 1] == rev[n - 1]:
                    dp[m][n] = 1 + dp[m - 1][n - 1]
                else:
                    dp[m][n] = max(dp[m - 1][n], dp[m][n - 1])

        return dp[l][l]