class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        def count(say):

            index, count = 0, 0
            resStr = ''

            while index < len(say):

                ch = say[index]

                while index + count < len(say) and say[index + count] == ch:
                    count += 1

                resStr = resStr + str(count) + ch

                index += count
                count = 0

            return resStr

        if n == 1:
            return '11'

        return count(self.countAndSay(n - 1))



if __name__ == '__main__':
    sol = Solution()
    print(sol.countAndSay(5))