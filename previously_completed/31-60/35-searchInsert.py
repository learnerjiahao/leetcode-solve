class Solution:
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums) < 1 or target <= nums[0]:
            return 0
        if target > nums[len(nums) - 1]:
            return len(nums)
        if target == nums[len(nums) - 1]:
            return len(nums) - 1

        low, high = 0, len(nums) - 1
        mid = (low + high) // 2
        while high - low > 0:
            if nums[mid] < target:
                low = mid + 1
            elif nums[mid] > target:
                high = mid - 1
            else:
                return mid
            mid = (low + high) // 2

        if nums[mid] < target:
            return mid + 1
        else:
            return mid



if __name__ == '__main__':
    sol = Solution()
    print(sol.searchInsert([1,3,5,6], 2))
    print(sol.searchInsert([1,2,4,6,7], 3))