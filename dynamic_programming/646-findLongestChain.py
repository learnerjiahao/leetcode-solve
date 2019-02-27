class Solution:
    def findLongestChain(self, pairs: 'List[List[int]]') -> int:
        
        def dp_method(sorted_pairs):
            len_p = len(sorted_pairs)
            dp = [1] * len_p
            for i in range(1, len_p):
                for j in range(i):
                    if sorted_pairs[j][1] < sorted_pairs[i][0]:
                        dp[i] = max(dp[i], dp[j]+1)
            return max(dp)

        # 1.sorted pairs 
        sorted_pairs = sorted(pairs, key=lambda item: item[0])
        return dp_method(sorted_pairs)
                
if __name__ == '__main__':
    sol = Solution()
    print(sol.findLongestChain([[1,2], [2,3], [3,4]]))