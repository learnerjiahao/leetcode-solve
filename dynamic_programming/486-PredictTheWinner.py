class Solution:
    def PredictTheWinner(self, nums: 'List[int]') -> bool:
        # method 1: recursion
        def method_one():
            # memo = [[0 for i in range(len(nums))] for j in range(len(nums))]
            memo = [[None] * len(nums) for j in range(len(nums))]

            def recursion(start_i, end_i):
                # todo start_i and end_i is valid
                if (start_i > end_i):
                    return
                if start_i == end_i:
                    return nums[start_i];
                if memo[start_i][end_i] != None:
                    return memo[start_i][end_i];
                left_score = nums[start_i] - recursion(start_i + 1,
                                                     end_i)  # player 1 choose start_i and - player's max score in range(start_i + 1, end_i)
                right_score = nums[end_i] - recursion(start_i, end_i - 1)
                memo[start_i][end_i] = max(left_score, right_score)

                return memo[start_i][end_i]

            return recursion(0,len(nums) - 1) >= 0


        def dp_method():
            dp = memo = [[0] * len(nums) for j in range(len(nums))]
            for s in range(len(nums)-1, -1, -1):
                for e in range(s, len(nums)):
                    if s == e:
                        dp[s][e] = nums[s]
                    else:
                        left_s = nums[s] - dp[s+1][e]
                        right_e = nums[e] - dp[s][e-1]
                        dp[s][e] = max(left_s, right_e)
            return dp[0][len(nums)-1] >= 0

        return dp_method()


if __name__ == '__main__':
    sol = Solution()
    print(sol.PredictTheWinner([1,5,2]))