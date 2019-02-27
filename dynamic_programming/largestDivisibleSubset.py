class Solution:
    '''
    Given a set of distinct positive integers, find the largest subset such that every pair (Si, Sj) of elements in this subset satisfies:
    Si % Sj = 0 or Sj % Si = 0.
    If there are multiple solutions, return any subset is fine.
    '''
    def largestDivisibleSubset(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        if not nums: return []
        # 思路：
        # 1、先从小到大排序，保证 only if i > j下才有可能 Si % Sj = 0 
        nums_sorted = sorted(nums)
        # 2. dp[i] = max(1 + dp[j] if i%j==0 else 1)
        dp = [0] * len(nums_sorted)
        divided = [0] * len(nums_sorted)
        max_i, max_len = 0, 0
        for i in range(len(nums_sorted)):
            dp[i], divided[i] = 1, i
            for j in range(0, i):
                if (nums_sorted[i]%nums_sorted[j] == 0 and dp[j]+1 > dp[i]):
                    divided[i] = j
                    dp[i] = dp[j]+1
            if dp[i] > max_len:
                max_len, max_i = dp[i], i

        res = []
        i = max_i
        while True:
            res.append(nums_sorted[i])
            if i == divided[i]:
                break
            i = divided[i]

        return res
        