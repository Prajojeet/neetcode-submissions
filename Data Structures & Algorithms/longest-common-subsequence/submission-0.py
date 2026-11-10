class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # top down
        l1 = len(text1)
        l2 = len(text2)

        dp = [[0] * (l2 + 1) for _ in range(l1 + 1)]
        print(dp)
        for m in range(1, l1 + 1):
            for n in range(1, l2 + 1):
                if text1[m - 1] == text2[n - 1]:
                    dp[m][n] = 1 + dp[m - 1][n - 1]
                else:
                    dp[m][n] = max(dp[m - 1][n], dp[m][n - 1])

        return dp[l1][l2]