class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if len(nums) == 0: return

        true_offset = k % len(nums)

        tmp_list = nums[0:len(nums) - true_offset]
        nums[0:true_offset] = nums[len(nums) - true_offset:]
        nums[true_offset:] = tmp_list



if __name__ == '__main__':
    sol = Solution()
    nums = [-1,-100,3,99]
    sol.rotate(nums, 2)
    print(nums)