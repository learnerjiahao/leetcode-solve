class Solution:
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        DP = [1 if i == 0 else 0 for i in range(n)]

        # def subTree(lo, hi):
        #     sum = 0
        #     if lo == hi:
        #         return 1
        #     for i in range(lo, hi + 1):
        #         if i == lo:
        #             sum += subTree(i + 1, hi)
        #         elif i == hi:
        #             sum += subTree(lo, i - 1)
        #         else:
        #             sum += (subTree(i + 1, hi) * subTree(lo, i - 1))
        #     return sum
        # return subTree(0, n - 1)

        def subTree(sub_n):
            if DP[sub_n - 1] != 0:
                return DP[sub_n - 1]
            for i in range(sub_n):
                if i == 0 or i == sub_n - 1:
                    DP[sub_n - 1] += subTree(sub_n - 1)
                else:
                    DP[sub_n - 1] += (subTree(i) * subTree(sub_n - 1 - i))
            return DP[sub_n - 1]

        return subTree(n)
                
                




if __name__ == "__main__":
    sol = Solution()
    print(sol.numTrees(4))
