class Solution:
    def findPaths(self, m: int, n: int, N: int, x: int, y: int) -> int:
        # method 1: recursion without memo
        def recursion_method(now_i, now_j, now_N):
            if now_i < 0 or now_i >= m or now_j < 0 or now_j >= n:
                if now_N == 0:
                    return 1
                else:
                    return 0
            else:
                return recursion_method(now_i, now_j-1, now_N-1) + recursion_method(now_i, now_j+1, now_N-1) + recursion_method(now_i-1, now_j, now_N-1) + recursion_method(now_i+1, now_j, now_N-1)

        # method 2: recursion with memo
        memo = [[[-1] * n for _ in range(m)] for _ in range(N+1)]
        def recursion_method_with_memo(now_i, now_j, now_N):
            if memo[now_N][now_i][now_j] != -1:
                return memo[now_N][now_i][now_j]
            if now_i < 0 or now_i >= m or now_j < 0 or now_j >= n:
                return 1
            if now_N == 0:
                memo[now_N][now_i][now_j] = 0
                return memo[now_N][now_i][now_j]
            memo[now_N][now_i][now_j] = recursion_method(now_i, now_j-1, now_N-1) + recursion_method(now_i, now_j+1, now_N-1) + recursion_method(now_i-1, now_j, now_N-1) + recursion_method(now_i+1, now_j, now_N-1)
            return memo[now_N][now_i][now_j]

        Mod = 10 ** 9 + 7
        # method 3: dp
        def dp_method():
            pre_dp = [[0] * n for _ in range(m)]
            pre_dp[x][y] = 1
            result = 0
            for k in range(1, N+1):
                now_dp = [[0] * n for _ in range(m)]
                for i in range(m):
                    for j in range(n):
                        if i == 0: 
                            result = (result + pre_dp[i][j])
                        if i == m-1:
                            result = (result + pre_dp[i][j])
                        if j == 0:
                            result = (result + pre_dp[i][j])
                        if j == n-1:
                            result = (result + pre_dp[i][j])

                        now_dp[i][j] = ((0 if i == 0 else pre_dp[i-1][j]) + \
                                        (0 if i == m-1 else pre_dp[i+1][j]) + \
                                        (0 if j == 0 else pre_dp[i][j-1]) + \
                                        (0 if j == n-1 else pre_dp[i][j+1]))
                pre_dp = now_dp
            return result % Mod

        # return recursion_method_with_memo(i, j, N)
        return dp_method()



if __name__ == '__main__':
    sol = Solution()
    print(sol.findPaths(1,2,50,0,0))