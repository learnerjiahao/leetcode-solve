class Solution:
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        abs_max_int32 = pow(2, 31) - 1
        abs_min_int32 = abs_max_int32 + 1

        flag = 1
        str = str.lstrip(' ')
        res_int = 0

        for i in range(0, len(str)):
            if i == 0:
                if str[i] == '-':
                    flag = -1
                    continue
                elif str[i] == '+':
                    flag = 1
                    continue
            if not str[i].isdigit():
                break
            digit = ord(str[i]) - ord('0')
            if (flag == 1 and (abs_max_int32 - digit) / 10.0 < res_int) \
                    or (flag == -1 and (abs_min_int32 - digit) / 10.0 < res_int):
                return abs_max_int32 if flag==1 else abs_min_int32*-1
            res_int = res_int * 10 + digit

        return res_int*flag


if __name__ == '__main__':
    soul = Solution()
    print(soul.myAtoi(' -a'))




