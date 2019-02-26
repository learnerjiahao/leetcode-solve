class Solution:
    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if len(nums) == 1:
            return 0
        elif len(nums) == 0:
            return -1

        import sys
        maxest, second_max = -sys.maxsize, -sys.maxsize-1
        # maxest_index = -1
        for i, num in enumerate(nums):
            if num > maxest:
                second_max, maxest = maxest, num
                maxest_index = i
            elif num > second_max:
                second_max = num
            # elif num < minest:
            #     num = minest

        if second_max == 0 or maxest / second_max >= 2:
            return maxest_index
        else:
            return -1


sol = Solution()
sol.dominantIndex([0, 1])