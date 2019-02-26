class Solution:
    def findLongestChain(self, pairs):
        """
        :type pairs: List[List[int]]
        :rtype: int
        """
        sorted_pairs = sorted(pairs, key=lambda pair: pair[0])
        max_length = 1

        for i in range(len(sorted_pairs)):
            now_length = 1
            for j in range(i + 1, len(sorted_pairs)):
                print("ssss")
                



if __name__ == '__main__':
    sol = Solution()
    sol.findLongestChain([[1, 2], [2, 3], [3, 4]])
