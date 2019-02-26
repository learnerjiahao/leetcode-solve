class Solution:
    def canPartition(self, nums: 'List[int]') -> 'bool':
        
        all_sum = sum(nums)
        if all_sum % 2:
            return False
        sub_sum = all_sum / 2
        # find subset in nums whoes sum is equal to sub_sum
        nums.sort()

        # method one: backtracking
        def backtrack(nums, start, left_sum):
            for i in range(start, len(nums)):
                if nums[start] == left_sum:
                    return True
                if nums[start] > left_sum:
                    return False
                if backtrack(nums, i+1, left_sum-nums[start]):
                    return True 
            else:
                return False

        return backtrack(nums, 0, sub_sum)
                