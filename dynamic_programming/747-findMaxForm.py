class Solution:
    def findMaxForm(self, strs: 'List[str]', m: 'int', n: 'int') -> 'int':

        # prehand
        counts = [[0, 0] for i in range(len(strs))]
        for i, str in enumerate(strs):
            for ch in str:
                if ch == '0':
                    counts[i][0] += 1
                elif ch == '1':
                    counts[i][1] += 1
                else:
                    raise ValueError(str + " is invalid")
        print(counts)
        # method one greedy, wrong method!!!!!!!!
        def greedy_method(count, m, n):
            # sort count by the number of zero
            sorted_by_zero = sorted(counts, key=lambda item:item[0])
            # sort count by the number of one
            sorted_by_one = sorted(counts, key=lambda item:item[1])

            max_by_zero, max_by_one = 0, 0
            for item in sorted_by_zero:
                pass

        # method 2: recursion, time complexity is n!
        def recusrion_method(new_start, left_m, left_n):
            # if left_n < 0 or left_m < 0: return -1
            # if len(counts) <= new_start: return 0
            # return 1 + max([-1] + [recusrion_method(counts, i+1, left_m - counts[new_start][0], left_n - counts[new_start][1]) for i in
            #                 range(new_start+1, len(counts))])
            max_deep = 0
            for i in range(new_start, len(counts)):
                print(len(counts), i)
                if left_m - counts[i][0] < 0 or left_n - counts[i][1] < 0:
                    continue
                max_deep = max(max_deep, 1 + recusrion_method(i+1, left_m - counts[i][0], left_n - counts[i][1]))
            return max_deep

        # knapsack problem
        def dp_method():
            dp = [None] * (len(counts))
            for i in range(len(counts)):
                dp[i] = [None] * m
                for j in range(m):
                    dp[i][j] = [0] * n
                    for k in range(n):
                        if i == 0:
                            if j+1 >= counts[i][0] and k+1 >= counts[i][1]:
                                dp[i][j][k] = 1
                            else:
                                dp[i][j][k] = 0
                        else:
                            if j+1 >= counts[i][0] and k+1 >= counts[i][1]:
                                dp[i][j][k] = max(dp[i - 1][j - counts[i][0]][k - counts[i][1]] + 1, dp[i - 1][j][k])
                            else:
                                dp[i][j][k] = dp[i - 1][j][k]

            return dp[len(counts) - 1][m - 1][n - 1]

        return dp_method()

if __name__ == '__main__':
    sol = Solution()
    # print(sol.findMaxForm(["0","11","1000","01","0","101","1","1","1","0","0","0","0","1","0","0110101","0","11","01","00","01111","0011","1","1000","0","11101","1","0","10","0111"], 9,80))
    print(sol.findMaxForm(["10","0001","111001","1","0"], 5, 3))




