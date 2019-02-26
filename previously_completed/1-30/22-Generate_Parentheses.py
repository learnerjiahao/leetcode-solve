from numpy.core.tests.test_mem_overlap import xrange


class Solution:
    def generateParenthesis(self, n): # todo err
        """
        :type n: int
        :rtype: List[str]
        """
        result = []
        if n == 0:
            return ['']
        if n == 1:
            return ['()']
        result += filter(lambda x: x not in result, (['(' + elem + ')' for elem in self.generateParenthesis(n-1)]))
        result += filter(lambda x: x not in result, ['(' + elem + ')()' for elem in self.generateParenthesis(n-2)])
        result += filter(lambda x: x not in result, ['()(' + elem + ')' for elem in self.generateParenthesis(n-2)])
        result += filter(lambda x: x not in result, ['()' + elem + '()' for elem in self.generateParenthesis(n-2)])
        return result

    def generateParenthesis1(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        result = []
        if n == 0:
            return ['']
        for i in range(0, n):
            for left in self.generateParenthesis1(i):
                for right in self.generateParenthesis1(n - i - 1):
                    result.append('({}){}'.format(left, right))
        return result

    def generateParenthesis2(self, N):
        if N == 0: return ['']
        ans = []
        for c in xrange(N):
            for left in self.generateParenthesis(c):
                for right in self.generateParenthesis(N - 1 - c):
                    ans.append('({}){}'.format(left, right))
        return ans

if __name__ == '__main__':
    soul = Solution()
    print(soul.generateParenthesis1(3))
    print(soul.generateParenthesis2(3))