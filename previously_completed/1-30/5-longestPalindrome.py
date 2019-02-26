class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """

        maxi, maxj = 0, 0
        max_len = 0

        for i in range(0, len(s)):
            if (len(s)-i) <= max_len:
                break
            for j in range(len(s) - 1, i, -1):
                if (j-i+1) <= max_len:
                    break
                if s[i] == s[j]:
                    k = 1
                    while ((i + k) < (j - k)) and (s[i + k] == s[j - k]):
                        k = k + 1

                    if (i + k) >= (j - k):
                        max_len = (j-i+1)
                        maxi = i
                        maxj = j


        return s[maxi:maxj+1]

    def longestPalindrome1(self, s):
        """
        :type s: str
        :rtype: str
        """

        maxi, maxj = 0, 0
        max_len = 1

        for out_i in range(0, len(s) - 1):
            i, j = out_i, out_i+1
            while i >= 0 and j < len(s) and s[i] == s[j]:
                i, j = i-1, j+1
            if j-1-(i+1)+1 > max_len:
                max_len = j-1-(i+1)+1
                maxi, maxj = i+1, j-1

            i, j = out_i, out_i + 2
            while i >= 0 and j < len(s) and s[i] == s[j]:
                i, j = i-1, j+1
            if j-1-(i+1)+1 > max_len:
                max_len = j-1-(i+1)+1
                maxi, maxj = i+1, j-1

        return s[maxi:maxj+1]


    def longestPalindrome2(self, s):
        """
        :type s: str
        :rtype: str
        """

        maxi, maxj = 0, 0
        max_len = 1

        result = [[False for j in range(0, i+1)] for i in range(0, len(s))]
        for i in range(0, len(s)):
            for j in range(0, i+1):
                if (i == j):
                    result[i][j] = True
                elif (i-1==j):
                    result[i][j] = s[i]==s[j]
                else:
                    result[i][j] = j<len(s)-1 and i>0 and result[i-1,j+1] and s[i]==s[j]

                if result[i][j] and max_len < i-j+1:
                    max_len = i-j+1
                    maxi = i
                    maxj = j
        return s[maxj:maxi+1]



if __name__ == '__main__':
    sou = Solution()
    # print(len(sou.longestPalindrome1('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'
    #                                 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabcaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'
    #                                 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa')))
    print((sou.longestPalindrome2('bb')))

