import sys


class Solution:
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # if len(nums) < 3: # error
        #     raise ValueError
        #
        # nums.sort()
        # i = 0
        # while nums[i]<target:
        #     i += 1
        #
        # if i<=2:
        #     return nums[0]+nums[1]+nums[2]
        # else:
        #     return nums[i-1]+nums[i-2]+nums[i-3]

        if len(nums) < 3:
            raise ValueError
        diff = sys.maxsize
        nums.sort()
        for i in range(0, len(nums)-1):
            j, k = i+1, len(nums)-1
            while j < k:
                if nums[i]+nums[j]+nums[k] == target:
                    return target
                if abs(nums[i]+nums[j]+nums[k]-target) < diff:
                    diff = abs(nums[i]+nums[j]+nums[k]-target)
                    res = nums[i]+nums[j]+nums[k]
                if nums[i]+nums[j]+nums[k] > target:
                    k -= 1
                else:
                    j += 1
        return res






