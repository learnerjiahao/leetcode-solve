class Solution:
    def knightProbability(self, N: int, K: int, r: int, c: int) -> float:
        # method 1: recursion with memo
        memo = [[[None for _ in range(N)] for _ in range(N)] for _ in range(K+1)]
        moves = [(1, 2), (-1, 2), (1, -2), (-1, -2), (2, 1), (-2, 1), (2, -1), (-2, -1)]

        def recursion_method(left_K, new_r, new_c):
            if new_r < 0 or new_r >= N or new_c < 0 or new_c >= N:
                return 0
            if left_K <= 0:
                return 1

            if memo[left_K][new_r][new_c] != None:
                return memo[left_K][new_r][new_c]

            res = 0
            for item in moves:
                res += (recursion_method(left_K-1, new_r+item[0], new_c+item[1]) / 8)

            memo[left_K][new_r][new_c] = res
            return res

        return recursion_method(K, r, c)


if __name__ == '__main__':
    sol = Solution()
    print(sol.knightProbability(8, 4, 6, 4))
