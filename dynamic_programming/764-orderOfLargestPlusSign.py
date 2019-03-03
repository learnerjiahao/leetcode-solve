class Solution:
    def orderOfLargestPlusSign(self, N: int, mines: 'List[List[int]]') -> int:
        matrix = [[1] * N for _ in range(N)]
        for indecs in mines:
            matrix[indecs[0]][indecs[1]] = 0

        # method 1: brute force, time complexity: N ** 3
        def method_brute_force():
            max_res = 0
            for i in range(N):
                for j in range(N):
                    if not matrix[i][j]: continue
                    order = 1
                    while i + order < N and i - order >= 0 and j + order < N and j - order >= 0:
                        if matrix[i + order][j] and matrix[i][j - order] \
                                and matrix[i][j + order] and matrix[i - order][j]:
                            order += 1
                        else:
                            break
                    max_res = max(max_res, order)

            return max_res

        # method 2: dynamic programming
        def method_dp():
            dp = [[0] * N for _ in range(N)]

            # to down
            for c in range(N):
                count = 0
                for r in range(N-1, -1, -1):
                    count = 0 if not matrix[r][c] else count + 1
                    dp[r][c] = count

            # to up
            for c in range(N):
                count = 0
                for r in range(N):
                    count = 0 if not matrix[r][c] else count + 1
                    dp[r][c] = min(dp[r][c], count)

            # to left
            for r in range(N):
                count = 0
                for c in range(N):
                    count = 0 if not matrix[r][c] else count + 1
                    dp[r][c] = min(dp[r][c], count)

            res = 0
            # to right
            for r in range(N):
                count = 0
                for c in range(N-1, -1, -1):
                    count = 0 if not matrix[r][c] else count + 1
                    dp[r][c] = min(dp[r][c], count)
                    res = max(res, dp[r][c])
            return res

        return method_dp()

