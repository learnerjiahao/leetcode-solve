class Solution:
    def findNumberOfLIS(self, nums: 'List[int]') -> int:
        if len(nums) <= 0: return 0

        dp = [1] * len(nums)
        cnt = [1] * len(nums)
        for i in range(len(nums)):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j]+1)
            tmp_cnt = 0        
            for j in range(i):
                 if nums[j] < nums[i] and dp[j]+1 == dp[i]:
                    tmp_cnt += cnt[j]
            cnt[i] = max(tmp_cnt, cnt[i])
        print(dp, cnt)
        res = 0
        max_len = max(dp)
        for i, ln in enumerate(dp):
            if ln == max_len:
                res += cnt[i]
        return res

if __name__ == '__main__':
    sol = Solution()
    sol.findNumberOfLIS([1,2,4,3,5,4,7,2])