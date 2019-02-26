class Solution:
    def combine1(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        ret = []

        def helper(left_nums, k):


            if k <= 1:
                return [[num] for num in left_nums]

            left_ret = []
            for i in range(len(left_nums)):
                now_num = left_nums[i]
                nums_backup = [num for num in left_nums]
                left_nums.remove(now_num)
                for nums in helper(left_nums, k-1):
                    nums.append(now_num)
                    left_ret.append(nums)
                left_nums = nums_backup

            return left_ret

        nums = [i+1 for i in range(n)]
        return helper(nums, k)


    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        if k > n:
            raise ValueError("k can not larger than n")

        if n == k:
            return [[num+1 for num in range(n)]]

        if k == 1:
            return [[num+1] for num in range(n)]


        return self.combine(n - 1, k) + [([n] + nums) for nums in self.combine(n - 1, k - 1)]



if __name__ == "__main__":
    num1 = [1, 2]
    num2 = [3, 4]
    #
    num2 = num1
    num1.remove(2)
    print(num2)

    sol = Solution()
    print(sol.combine(4, 2))

