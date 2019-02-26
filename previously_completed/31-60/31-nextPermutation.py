class Solution:
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """

        low, high = 0, len(nums) - 1
        for i in range(len(nums)-1, 0, -1):
            if nums[i-1] < nums[i]:
                for j in range(len(nums)-1, i-1, -1):
                    if nums[j] > nums[i-1]:
                        nums[i-1], nums[j] = nums[j], nums[i-1]
                        break
                low = i
                break

        while low < high:
            nums[low], nums[high] = nums[high], nums[low]
            low = low + 1
            high = high - 1

if __name__ == "__main__":
    sol = Solution()
    # nums = [1,2,3,4]
    nums = [1,3,2]
    sol.nextPermutation(nums)
    print(nums)


