class Solution:
    def reversePairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ret_count = 0
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] > 2 * nums[j]:
                    ret_count += 1
        return ret_count

if __name__ == "__main__":
    sol = Solution()
    print(sol.reversePairs([2, 4, 3, 5, 1]))
