class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False

        reser_num = 0
        num = x
        while num > 0:
            reser_num = (reser_num + num % 10) * 10
            num = num // 10

        reser_num = reser_num // 10

        return reser_num==x



if __name__ == '__main__':
    soul = Solution()
    print(soul.isPalindrome(2))