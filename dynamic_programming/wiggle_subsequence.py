class Solution:
    def wiggleMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        """
        暴力递归
        """
        def brute_force(nums):
            if len(nums) < 2:
                return len(nums)
            def caluate_max_len(index, is_up):
                max_len = 0
                for i in range(index+1, len(nums)):
                    if (nums[i] > nums[index] and is_up) or (nums[i] < nums[index] and not is_up):
                        max_len = max(max_len, 1 + caluate_max_len(i, not is_up))
                        
                return max_len
            
            return 1 + max(caluate_max_len(0, True), caluate_max_len(0, False))
        
        """
        动态规划，down[i] and up[i]: 从0到i的子序列中的最长wiggle subsequence
        """
        def dp_n2(nums):
            if len(nums) < 2:
                return len(nums)
            up, down = [0] * len(nums), [0] * len(nums)

            for i in range(len(nums)):
                for j in range(i):
                    if nums[i] > nums[j]:
                        up[i] = max(up[i], down[j] + 1)
                    elif nums[i] < nums[j]:
                        down[i] = max(down[i], up[j] + 1)


            return 1 + max(down[len(nums) - 1], up[len(nums) - 1])

        
        def dp_n(nums):
            if len(nums) < 2:
                return len(nums)
            up, down = [0] * len(nums), [0] * len(nums)
            up[0] = down[0] = 1

            for i in range(1, len(nums)):
                if nums[i] > nums[i-1]:
                    up[i] = down[i-1] + 1
                    down[i] = down[i-1]
                elif nums[i] < nums[i-1]:
                    down[i] = up[i-1] + 1
                    up[i] = up[i-1]
                else:
                    down[i] = down[i-1]
                    up[i-1] = up[i-1]

            return max(down[len(nums) - 1], up[len(nums) - 1])
            
        # return brute_force(nums)
        return dp_n2(nums)