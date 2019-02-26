from math import ceil


class Solution:
    def getMoneyAmount(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 0
        if n == 2:
            return 1

        ret_money_sum = 0
        money = n
        while True:
            money = ceil((money + 1) // 2)
            if money <= 1:
                break
            ret_money_sum += money
            money -= 1

        return ret_money_sum

