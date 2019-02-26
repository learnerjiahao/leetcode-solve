class Solution:
    def binary_search(self, nums, target):
        if len(nums) < 1:
            return -1
        if target < nums[0] or target > nums[len(nums) - 1]:
            return -1
        if target == nums[0]:
            return 0
        if target == nums[len(nums) - 1]:
            return len(nums) - 1

        low, high = 0, len(nums) - 1
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] < target:
                low = mid + 1
            elif nums[mid] > target:
                high = mid - 1
            else:
                return mid
        return -1

    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        low, high = 0, len(nums) - 1
        pivot = 0
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] > nums[high]:
                ret = self.binary_search(nums[low:mid+1], target)
                if ret != -1:
                    return low+ret
                low = mid + 1
            elif nums[mid] < nums[low]:
                ret = self.binary_search(nums[mid:high+1], target)
                if ret != -1:
                    return mid + ret
                high = mid - 1
            else:  # todo
                ret = self.binary_search(nums[low:high + 1], target)
                if ret != -1:
                    return low + ret
                break
        return -1



if __name__ == '__main__':
    sol = Solution()
    # print(sol.search([4,5,6,7,0,1,2], 0))
    # print(sol.search([5,1,3], 1))
    print(sol.search([4,5,6,7,0,1,2], 6))