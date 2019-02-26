class Solution:
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        import math
        N = len(matrix)
        iter = math.ceil(N / 2)
        def rotateOneCircle(start_i, sub_N):
            for i in range(sub_N - 1):
                now_value = matrix[start_i + i][start_i]
                next_x, next_y = start_i, start_i + i
                for _ in range(4):
                    next_x, next_y = N - 1 - next_y, next_x
                    matrix[next_y][next_x], now_value = now_value, matrix[next_y][next_x]
                    next_x, next_y = next_x, next_y

        for i in range(iter):
            rotateOneCircle(i, N - 2 * i)

        # print(matrix)
        

if __name__ == '__main__':
    sol = Solution()
    matrix1 = [[1,2,3], [4,5,6], [7,8,9]]
    sol.rotate(matrix1)
    # print(matrix1)
    print(matrix1[::-1])

    matrix2 = [[ 5, 1, 9,11], [ 2, 4, 8,10], [13, 3, 6, 7],[15,14,12,16]]
    sol.rotate(matrix2)

    # print(matrix2)

        

            
            