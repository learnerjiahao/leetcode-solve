class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:

        # dynamics programming
        l1, l2 = len(s1), len(s2)
        dp = [[0] * (l2 + 1) for _ in range(l1 + 1)]

        for i in range(l1 - 1, -1, -1):
            dp[i][l2] = dp[i+1][l2] + ord(s1[i])

        for j in range(l2 - 1, -1, -1):
            dp[l1][j] = dp[l1][j+1] + ord(s2[j])

        for i in range(l1 - 1, -1, -1):
            for j in range(l2 - 1, -1, -1):
                if (s1[i] == s2[j]):
                    dp[i][j] = dp[i+1][j+1]
                else:
                    dp[i][j] = min(dp[i+1][j] + ord(s1[i]), dp[i][j+1] + ord(s2[j]))

        return dp[0][0]