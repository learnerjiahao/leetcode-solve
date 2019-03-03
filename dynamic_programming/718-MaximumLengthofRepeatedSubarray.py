class Solution:
    def findLength(self, A: 'List[int]', B: 'List[int]') -> int:
        l1, l2 = len(A), len(B)
        dp = [[0] * (l2 + 1) for _ in range(l1 + 1)]

        for i in range(l1 - 1, -1, -1):
            for j in range(l2 - 1, -1, -1):
                if A[i] == B[j]:
                    dp[i][j] = dp[i + 1][j + 1] + 1

        return max([max(row) for row in dp])
