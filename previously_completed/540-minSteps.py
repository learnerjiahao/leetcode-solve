from math import sqrt, floor


class Solution(object):
    def minSteps1(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 0

        res_sqrt = floor(sqrt(n))

        for factor in range(res_sqrt, 0, -1):

            if n % factor == 0:
                another_factor = n / factor
                return min(self.minSteps(another_factor) + factor - 1,
                           self.minSteps(factor) + another_factor - 1)

    def minSteps(self, n):
        ans = 0
        d = 2
        while n > 1:
            while n % d == 0:
                ans += d
                n /= d
            d += 1
        return ans


if __name__ == '__main__':
    sol = Solution()
    print(sol.minSteps(16))