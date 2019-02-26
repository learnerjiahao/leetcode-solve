class Solution:
    def findDiagonalOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if len(matrix) <= 0:
            return []

        if len(matrix[0]) <= 0:
            return []

        low_i, low_j = 0, 0
        high_i, high_j = 0, 0

        result_list = []

        row_count, column_count = len(matrix), len(matrix[0])

        for num in range(row_count + column_count):

            if num % 2 == 0:
                for column in range(low_j, high_j + 1):
                    result_list.append(matrix[num - column][column])
            else:
                for column in range(high_j, low_j - 1, -1):
                    result_list.append(matrix[num - column][column])

            if high_j < column_count - 1:
                high_j += 1
            else:
                high_i += 1

            if low_i < row_count - 1:
                low_i += 1
            else:
                low_j += 1

        return result_list


if __name__ == "__main__":
    sol = Solution()
    print(sol.findDiagonalOrder([[1, 2, 3],[ 4, 5, 6 ],[ 7, 8, 9 ]]))

