class Solution:
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        low, high = 0, len(nums) - 1
        mid = (len(nums) - 1) // 2

        while low < high:
            if nums[mid] == nums[mid - 1]:
                if (mid + 1) % 2 == 0:
                    low = mid + 1
                else:
                    high = mid - 2
            elif nums[mid] == nums[mid + 1]:
                if (len(nums)-mid) % 2 == 0:
                    high = mid - 1
                else:
                    low = mid + 2
            else:
                break

            mid = (high + low) // 2

        return nums[mid]


if __name__ == "__main__":
    sol = Solution()
    print(sol.singleNonDuplicate([0,1,1]))
    print(sol.singleNonDuplicate([1, 1, 2, 2, 4, 4, 5, 5,9]))

        


        
        
        
        