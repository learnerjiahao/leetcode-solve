class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        def get_permutation_count(n):
            count = 1
            for i in range(n):
                count *= (i + 1)
            return count

        n_permutation_count = get_permutation_count(n)
        nums = [(i+1) for i in range(n)]

        if k > n_permutation_count:
            raise ValueError

        res_str = ''

        left_permutation_count = n_permutation_count

        k -= 1

        for i in range(n - 1, -1, -1):

            left_permutation_count = left_permutation_count // (i + 1)

            num_index = k // left_permutation_count

            res_str += str(nums[num_index])

            k = k % left_permutation_count

            nums.remove(nums[num_index])

        return res_str

if __name__ == '__main__':
    sol = Solution()
    print(sol.getPermutation(3, 3))

