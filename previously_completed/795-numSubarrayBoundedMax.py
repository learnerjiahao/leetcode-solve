class Solution:
    def numSubarrayBoundedMax(self, A, L, R):
        """
        :type A: List[int]
        :type L: int
        :type R: int
        :rtype: int
        """

        # # first sort A
        # A.sort()
        # # second, find the index of L, R in A
        # index_L, index_R = 0, 0
        # for i in range(len(A)):
        #     if A[i] >= L:
        #         index_L = i
        #         break
        # else:
        #     return 0
        # for i in range(len(A) - 1, -1, -1):
        #     if A[i] <= R:
        #         index_R = i
        #         break
        # else:
        #     return 0

        # all = (index_R - index_L) ** 2
        # return all - (all - (index_R - index_L)) / 2

        # max = [[A[i] if j == i else -1 for j in range]]
        ret_count = 0
        max = [[-1] * len(A) for _ in range(len(A))]
        for i in range(len(A)):
            for j in range(i, len(A)):
                    
                max[i][j] = A[i]

                


if __name__ == '__main__':
    sol = Solution()
    print(sol.numSubarrayBoundedMax([2, 1, 4, 3], 2, 3))
