class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        digits = list()
        abs_max_int32 = pow(2, 31) - 1
        abs_min_int32 = abs_max_int32 + 1
        x_abs = abs(x)
        while True:
            digits.append(x_abs % 10)
            x_abs //= 10
            if x_abs == 0:
                break

        r_abs = 0
        for i in range(0, len(digits)):
            if ((abs_min_int32 - digits[i]) / 10.0 < r_abs and x < 0) or ((abs_max_int32 - digits[i]) / 10.0 < r_abs and x > 0):
                return 0
            r_abs = r_abs * 10 + digits[i]

        return r_abs if x > 0 else r_abs*-1




if __name__ == '__main__':
    soul = Solution()
    print(soul.reverse(pow(2, 31)))