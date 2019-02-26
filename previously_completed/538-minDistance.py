class Solution:
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        if len(word1) == 0:
            return len(word2)
        if len(word2) == 0:
            return len(word1)

        dpContainer = [[0 for j in range(len(word2))] for i in range(len(word1))]

        for i in range(len(word1)):
            for j in range(len(word2)):
                if i == 0 and j == 0:
                    dpContainer[i][j] = 1 if word1[i] == word2[j] else 0
                elif i == 0:
                    dpContainer[i][j] = 1 if (dpContainer[i][j-1] == 1 or word1[i] == word2[j]) else 0
                elif j == 0:
                    dpContainer[i][j] = 1 if (dpContainer[i-1][j] == 1 or word1[i] == word2[j]) else 0
                elif word1[i] == word2[j]:
                    dpContainer[i][j] = 1 + dpContainer[i-1][j-1]
                else:
                    dpContainer[i][j] = max(dpContainer[i-1][j], dpContainer[i][j-1])

        return len(word1) + len(word2) - 2 * dpContainer[len(word1)-1][len(word2)-1]
                    
        # dp[0][0] = 1 if word1[0]==word2[0] else 0
        # dp[0][1] = 1 if dp[0][0] == 1 or word1[0]==word2[1] else 0
        # dp[1][0] = 1 if dp[0][0] == 1 or word1[1]==word2[0] else 0

        # def lcss_dp(index1, index2):
            
        #     if word1[index1] == word2[index2]:
        #         dpContainer[index1][index2] = 1 + dpContainer[]
            

        def lcss_recursion(word1_sub, word2_sub):

            len1, len2 = len(word1_sub), len(word2_sub)

            if len1 == 0 or len2 == 0:
                return 0

            if word1_sub[len1-1] == word2_sub[len2-1]:
                return 1 +  lcss_recursion(word1_sub[:len1-1], word2_sub[:len2-1])

            return max(lcss_recursion(word1_sub, word2_sub[:len2-1]), lcss_recursion(word1_sub[:len1-1], word2_sub))

        return len(word1) + len(word2) - 2 * lcss_recursion(word1, word2)      


if __name__ == '__main__':
    sol = Solution()
    print(sol.minDistance('abc', 'ebc'))
        