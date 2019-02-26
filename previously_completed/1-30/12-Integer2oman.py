class Solution:
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        s1 = ['I', 'X', 'C', 'M']
        s5 = ['V', 'L', 'D']
        def oneNum2Roman(n, i):
            if n <= 0:
                return ''
            if n <= 3:
                return s1[i] + oneNum2Roman(n-1, i)
            if n == 4:
                return s1[i]+s5[i]
            elif n == 5:
                return s5[i]
            elif n >= 6 and n < 9:
                return oneNum2Roman(n-1, i)+s1[i]
            elif n == 9:
                return s1[i]+s1[i+1]


        tmp_num = num
        loc = 0
        res_str = ''
        while tmp_num > 0:
            res_str = oneNum2Roman(tmp_num%10, loc) + res_str
            tmp_num //= 10
            loc += 1

        return res_str

if __name__ == '__main__':
    soul = Solution()
    print(soul.intToRoman(3))
    print(soul.intToRoman(4))
    print(soul.intToRoman(9))
    print(soul.intToRoman(58))
    print(soul.intToRoman(1994))