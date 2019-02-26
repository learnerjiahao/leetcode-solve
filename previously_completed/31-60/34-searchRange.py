class Solution:
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        def binary_search(start, end):
            low, high = start, end
            while low <= high:
                mid = (low + high) // 2
                if nums[mid] < target:
                    low = mid + 1
                elif nums[mid] > target:
                    high = mid - 1
                else:
                    return mid, low, high  #
            return -1, -1, -1

        start_poss_mid, start_poss_low, start_poss_high = binary_search(0, len(nums)-1)
        if start_poss_mid == -1:
            return [-1, -1]

        ret_min = ret_max = start_poss_mid

        poss_mid, poss_low = start_poss_mid, start_poss_low
        while True:
            poss_mid, poss_low, _ = binary_search(poss_low, poss_mid - 1)
            if poss_mid == -1:
                break
            ret_min = poss_mid

        poss_mid, poss_high = start_poss_mid, start_poss_high
        while True:
            poss_mid, _, poss_high = binary_search(poss_mid+1, poss_high)
            if poss_mid == -1:
                break
            ret_max = poss_mid

        return [ret_min, ret_max]


if __name__ == '__main__':
    sol = Solution()
    print(sol.searchRange([0,0,0,0,1,2,3,3,4,5,6,6,7,8,8,8,9,9,10,10,11,11], 0))