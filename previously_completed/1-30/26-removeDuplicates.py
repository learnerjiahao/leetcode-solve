class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # lists = list()
        # lists.
        if len(nums) <= 1:
            return len(nums)

        num = nums[0]
        i = 0
        while i < len(nums):
            num = nums[i]
            while i + 1 < len(nums) and nums[i + 1] == num:
                nums.remove(nums[i + 1])
            i += 1
        return len(nums)


if __name__ == '__main__':
    soul = Solution()
    arr = [0,0,1,1,1,2,2,3,3,4]
    print(soul.removeDuplicates(arr), arr)

