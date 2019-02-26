class Solution:
    def sumSubseqWidths(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        A.sort()
        max_sum = pow(10, 9) + 7

        from scipy.special import comb
        ret_sum = 0
        # low, high = 0, 0
        for num_count in range(2, len(A) + 1):   # start with 2 num because the sum is 0 when there is 1 num
            for low in range(0, len(A) - num_count + 1):
                for high in range(low + num_count - 1, len(A)):
                    ret_sum += (A[high] - A[low]) * comb(high-low-1, num_count-2)
                    # if ret_sum >= max_sum: ret_sum -= max_sum

        return int(ret_sum) % max_sum

if __name__ == "__main__":
    sol = Solution()
    print(sol.sumSubseqWidths([2,1,3]))
    print(sol.sumSubseqWidths([5,69,89,92,31,16,25,45,63,40,16,56,24,40,75,82,40,12,50,62,92,44,67,38,92,22,91,24,26,21,100,42,23,56,64,43,95,76,84,79,89,4,16,94,16,77,92,9,30,13]))


