class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        nums_dict = dict()
        result = list()
        for i, val in enumerate(nums):
            if (target - val) in nums_dict.keys():
                result.append(nums_dict[target - val])
                result.append(i)
                return result
            nums_dict[val] = i




if __name__ == '__main__':
    solution = Solution()
    print(solution.twoSum([2, 7, 11, 15], 9))