class Solution:
    def isMatch(self, text, pattern):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        # si, pi = 0, 0
        # while si < len(s) and pi < len(p):
        #     if s[si] != p[pi]:
        #         if p[pi] == '.':
        #             if pi+1<len(p) and p[pi+1] == '*':
        #                 si = len(s) - (len(p) - (pi+2))
        #                 pi = pi + 2
        #             else:
        #                 si += 1
        #                 pi += 1
        #             continue
        #         elif p[pi] == '*':
        #             s_jump = 0
        #             p_jump = 0
        #             while si+s_jump<len(s) and s[si+s_jump]==p[pi-1]:
        #                 s_jump += 1
        #             while pi+1+p_jump<len(p) and p[pi+1+p_jump]==p[pi-1]:
        #                 p_jump += 1
        #             si += s_jump
        #             pi += p_jump + 1
        #         else:
        #             break
        #     else:
        #         si += 1
        #         pi += 1
        #
        # return si == len(s) and pi == len(p)
        if not pattern:
            return not text

        first_match = bool(text) and pattern[0] in {text[0], '.'}

        if len(pattern) >= 2 and pattern[1] == '*':
            return (self.isMatch(text, pattern[2:]) or
                    first_match and self.isMatch(text[1:], pattern))
        else:
            return first_match and self.isMatch(text[1:], pattern[1:])

    def isMatch1(self, text, pattern):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        dp = [[False] * (len(pattern) + 1) for _ in range(len(text) + 1)]

        dp[-1][-1] = True
        for i in range(len(text), -1, -1):
            for j in range(len(pattern) - 1, -1, -1):
                first_match = i < len(text) and pattern[j] in {text[i], '.'}
                if j + 1 < len(pattern) and pattern[j + 1] == '*':
                    dp[i][j] = dp[i][j + 2] or first_match and dp[i + 1][j]
                else:
                    dp[i][j] = first_match and dp[i + 1][j + 1]

        return dp[0][0]

    def isMatch2(self, text, pattern):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """

        memo = {}

        def dp(i, j):
            if (i, j) not in memo:
                if j == len(pattern):
                    ans = i == len(text)
                else:
                    first_match = i < len(text) and pattern[j] in {text[i], '.'}
                    if j + 1 < len(pattern) and pattern[j + 1] == '*':
                        ans = dp(i, j + 2) or first_match and dp(i + 1, j)
                    else:
                        ans = first_match and dp(i + 1, j + 1)

                memo[i, j] = ans
            return memo[i, j]

        return dp(0, 0)

if __name__ == '__main__':
    soul = Solution()
    print(soul.isMatch('a', '.*..a*'))