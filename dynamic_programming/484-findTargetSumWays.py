class Solution:
    def findTargetSumWays(self, nums: 'List[int]', S: int) -> int:
        # nethod 1: recursion, time complexity: s^n
        def recusrion_method(start_i, left_s):
            if start_i == len(nums):
                if left_s == 0:
                    return 1
                else:
                    return 0
            return recusrion_method(start_i+1, left_s - nums[start_i]) + \
                recusrion_method(start_i+1, left_s + nums[start_i]) 
        # nethod 2: recursion with memo        
        def recursion_method_with_memo():
            memo = [[None] * (2*1000 +1) for _ in range(len(nums))]
            def recusrion_method(start_i, sub_s):
                if start_i == len(nums):
                        if sub_s == S:
                            return 1
                        else:
                            return 0
                elif memo[start_i][sub_s+1000] == None:
                    memo[start_i][sub_s+1000] = recusrion_method(start_i+1, sub_s - nums[start_i]) + \
                        recusrion_method(start_i+1, sub_s + nums[start_i])
                return memo[start_i][sub_s+1000]
            return recusrion_method(0, 0)
        
       # method 3: dp
        def dp_method():
            dp = [[0] * (2*1000 +1) for _ in range(len(nums))]
            dp[0][nums[0]+1000] = 1
            dp[0][-nums[0]+1000] += 1
            for i in range(1, len(nums)):
                for j in range(-1000, 1001):
                    if dp[i-1][j+1000] > 0:
                    # dp[i][j+nums[i]] = dp[i][j] + dp[i-1][j-nums[i]]
                    # dp[i][j-nums[i]] = dp[i][j] + dp[i-1][j+nums[i]]
                        dp[i][j+nums[i]+1000] += dp[i-1][j+1000]
                        dp[i][j-nums[i]+1000] += dp[i-1][j+1000]
                        
            return 0 if S > 1000 else dp[len(nums)-1][S+1000]
        
        return dp_method()

if __name__ == '__main__':
    sol = Solution()
    print(sol.findTargetSumWays([1,1,1,1,1], 3))
        
