class Solution:
    def longestPalindromeSubseq(self, str: 'str') -> int:
    
        # method 1: recursion with memo
        memo = [[-1] * len(str) for _ in range(len(str))] 
        def recursion(s, e):
            if memo[s][e] != -1:
                return memo[s][e]
            if s == e: return 1
            if s > e: return 0       
            if str[s] == str[e]:
                memo[s][e] = 2 + recursion(s+1, e-1) 
            else:
                memo[s][e] = max(recursion(s, e-1), recursion(s+1, e))

            return memo[s][e]

        return recursion(0, len(str)-1)

if __name__ == '__main__':
    sol = Solution()
    print(sol.longestPalindromeSubseq("bbbab"))