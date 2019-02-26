class Solution:
    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if target <= 0:
            return 0
            
        dp = [1 if i == 0 else -1 for i in range(target + 1)]
        def helper(subtarget):
            if dp[subtarget] != -1:
                return dp[subtarget]
            sub_sum = 0
            for num in nums:
                if num <= subtarget:
                    sub_sum += helper(subtarget - num)
            dp[subtarget] = sub_sum
            return sub_sum

        return helper(target)


if __name__ == '__main__':
    sol = Solution()
    # print(sol.combinationSum4([1, 2, 3], 4))
    print(sol.combinationSum4([4, 2, 1], 32))
        
