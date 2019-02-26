class Solution:
    def threeSum(self, nums, target, first_num, result):
        """
                :type nums: List[int]
                :rtype: List[List[int]]
                """
        for iout in range(0, len(nums) - 2):
            if iout>0 and nums[iout-1]==nums[iout]:
                continue
            j, k = iout+1, len(nums)-1
            while j < k:
                if nums[iout]+nums[j]+nums[k]==target-first_num:
                    numj,numk = nums[j],nums[k]
                    while j<k and numj==nums[j]:
                        j += 1
                    while j<k and numk==nums[k]:
                        k -= 1
                    result.append([first_num, nums[iout], numj, numk])
                elif nums[iout]+nums[j]+nums[k] > target-first_num:
                    k -= 1
                else:
                    j += 1

    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        if len(nums) < 4:
            return []
        nums.sort()
        result = []
        for ifirst in range(0, len(nums)-3):
            if ifirst>0 and nums[ifirst-1]==nums[ifirst]:
                continue
            self.threeSum(nums[ifirst+1:], target, nums[ifirst], result)
        return result

if __name__ == '__main__':
    soul = Solution()
    print(soul.fourSum([0, 0, 0, 0], 0))

    print([1,2]+[3,4])