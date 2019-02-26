import collections


class Solution:

    def simple_method(self, board):

        if len(board) != 9:
            raise ValueError

        # first check whether each row is valid
        for row in board:
            digits = {'1', '2', '3', '4', '5', '6', '7', '8', '9'}
            if len(row) != 9:
                raise ValueError
            for digit in row:
                if digit != '.':
                    if digit not in digits:
                        return False
                    digits.remove(digit)

        # second check whether each column is valid
        for icolumn in range(0, 9):
            digits = {'1', '2', '3', '4', '5', '6', '7', '8', '9'}
            for irow in range(0, 9):
                if board[irow][icolumn] != '.':
                    if board[irow][icolumn] not in digits:
                        return False
                    digits.remove(board[irow][icolumn])

        # third check whether each sub board is valid
        for irow in range(1, 8, 3):
            for icolumn in range(1, 8, 3):
                digits = {'1', '2', '3', '4', '5', '6', '7', '8', '9'}

                if board[irow-1][icolumn-1] != '.':
                    digits.remove(board[irow-1][icolumn-1])
                if board[irow-1][icolumn] != '.':
                    digits.remove(board[irow-1][icolumn])
                if board[irow-1][icolumn+1] != '.':
                    digits.remove(board[irow-1][icolumn+1])

                if board[irow][icolumn-1] != '.':
                    if board[irow][icolumn-1] not in digits:
                        return False
                    digits.remove(board[irow][icolumn-1])

                if board[irow][icolumn] != '.':
                    if board[irow][icolumn] not in digits:
                        return False
                    digits.remove(board[irow][icolumn])

                if board[irow][icolumn+1] != '.':
                    if board[irow][icolumn+1] not in digits:
                        return False
                    digits.remove(board[irow][icolumn+1])

                if board[irow+1][icolumn-1] != '.':
                    if board[irow+1][icolumn-1] not in digits:
                        return False
                    digits.remove(board[irow+1][icolumn-1])

                if board[irow+1][icolumn] != '.':
                    if board[irow+1][icolumn] not in digits:
                        return False
                    digits.remove(board[irow+1][icolumn])

                if board[irow+1][icolumn+1] != '.':
                    if board[irow+1][icolumn+1] not in digits:
                        return False
                    digits.remove(board[irow+1][icolumn+1])

        return True

    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        # return self.simple_method(board)
        print(list(
            x
            for i, row in enumerate(board)
            for j, c in enumerate(row)
            if c != '.'
            for x in ((c, i), (j, c), (i // 3, j // 3, c))
        ))

        seen = sum(([(c, i), (j, c), (i // 3, j // 3, c)]
                    for i, row in enumerate(board)
                    for j, c in enumerate(row)
                    if c != '.'), [])
        print(seen)
        # return len(seen) == len(set(seen))

        seen = set()
        return not any(x in seen or seen.add(x)
                       for i, row in enumerate(board)
                       for j, c in enumerate(row)
                       if c != '.'
                       for x in ((c, i), (j, c), (i / 3, j / 3, c)))

        seen = sum(([(c, i), (j, c), (i / 3, j / 3, c)]
                    for i in range(9) for j in range(9)
                    for c in [board[i][j]] if c != '.'), [])
        return len(seen) == len(set(seen))

if __name__ == '__main__':
    sol = Solution()
    print(sol.isValidSudoku([["5","3",".",".","7",".",".",".","."],
                             ["6",".",".","1","9","5",".",".","."],
                             [".","9","8",".",".",".",".","6","."],
                             ["8",".",".",".","6",".",".",".","3"],
                             ["4",".",".","8",".","3",".",".","1"],
                             ["7",".",".",".","2",".",".",".","6"],
                             [".","6",".",".",".",".","2","8","."],
                             [".",".",".","4","1","9",".",".","5"],
                             [".",".",".",".","8",".",".","7","9"]
                            ]))