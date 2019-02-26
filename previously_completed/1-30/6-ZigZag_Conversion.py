class Solution:
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        rowNum = dict()
        rowResult = dict()
        res_str = ''
        if numRows == 1:
            return s
        for index in range(0, len(s)):
            if index <= numRows - 1:
                rowNum[index] = index + 1
            elif index < numRows + numRows - 2:
                rowNum[index] = numRows - (index - numRows + 1)
            if rowNum[index % (numRows + numRows - 2)] in rowResult.keys():
                rowResult[rowNum[index % (numRows + numRows - 2)]] += s[index]
            else:
                rowResult[rowNum[index % (numRows + numRows - 2)]] = s[index]
        for num in range(0, len(rowResult)):
            res_str += rowResult[num + 1]
        return res_str

if __name__ == '__main__':
    soul = Solution()
    print(soul.convert('A', 1))


