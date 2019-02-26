class Solution:
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """

        MIN_INT = -(1<<31)
        AXM_INT = (1<<31) - 1

        if divisor == 0 :
            raise ValueError

        if divisor == MIN_INT :
            if dividend == MIN_INT:
                return 1
            return 0

        if dividend == MIN_INT:
            if divisor == -1:
                return AXM_INT

        residue_dividend = abs(dividend)
        shift_left_divisor = abs(divisor)
        shift_left_count = 0
        ret_vaule = 0

        while residue_dividend >= abs(divisor) :
            while True :
                if (shift_left_divisor << 1) > residue_dividend :
                    break
                shift_left_divisor = shift_left_divisor << 1
                shift_left_count = shift_left_count + 1
            ret_vaule = ret_vaule + (1 << shift_left_count)
            residue_dividend = residue_dividend - shift_left_divisor
            shift_left_divisor = abs(divisor)
            shift_left_count = 0

        return ret_vaule if (dividend >=0 and divisor > 0) or (dividend < 0 and divisor < 0) else -ret_vaule




if __name__ == '__main__':
    solu =  Solution()
    # print(solu.divide(1, 2))
    # print(solu.divide(3, 2))Î
    print(solu.divide(-10000, 333))
    print((10000//333))
    print(solu.divide(10, 3))
    print(solu.divide(11212, 221))
    print((11212 // 221))

