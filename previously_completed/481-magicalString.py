class Solution:
    def magicalString(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 1: return n
        
        magicalString = ['1', '2', '2']
        origin_i, produce_i = 2, 1
        count_1 = 1
        while True:
            if len(magicalString) >= n:
                break
            for i in range(int(magicalString[produce_i])):
                magicalString.append('2') if magicalString[origin_i] == '1' else magicalString.append('1')
            produce_i += 1
            origin_i += int(magicalString[produce_i])
        
        print(magicalString)

if __name__ == '__main__':
    sol = Solution()
    sol.magicalString(10)