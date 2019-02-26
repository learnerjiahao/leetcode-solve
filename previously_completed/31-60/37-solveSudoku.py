import collections


class Solution:
    def solveSudoku_wrong(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """

        maxCount = max(collections.Counter(
            x
            for irow, row in enumerate(board)
            for icolumn, column in enumerate(row)
            if column != '.'
            for x in ((irow, column), (column, icolumn), (irow//3, icolumn//3, column))
        ).values())
        if maxCount > 1:
            raise ValueError

        # first solve in each row, left valid num which can be filled
        row_left_num_list = []
        for ir, row in enumerate(board):
            row_left_num = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
            for ic, ch in enumerate(row):
                if ch != '.':
                    row_left_num.remove(ch)
            row_left_num_list.append(row_left_num)

        # second solve in each column, left valid num which can be filled
        column_left_num_list = []
        for ic in range(0, 9):
            column_left_num = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
            for ir in range(0, 9):
                if board[ir][ic] != '.':
                    column_left_num.remove(board[ir][ic])
            column_left_num_list.append(column_left_num)

        # third solve in each sub, left valid num which can be filled
        sub_left_num_map = {}
        for irow in range(1, 8, 3):
            for icolumn in range(1, 8, 3):
                digits = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
                if board[irow - 1][icolumn - 1] != '.':
                    digits.remove(board[irow - 1][icolumn - 1])
                if board[irow - 1][icolumn] != '.':
                    digits.remove(board[irow - 1][icolumn])
                if board[irow - 1][icolumn + 1] != '.':
                    digits.remove(board[irow - 1][icolumn + 1])
                if board[irow][icolumn - 1] != '.':
                    digits.remove(board[irow][icolumn - 1])
                if board[irow][icolumn] != '.':
                    digits.remove(board[irow][icolumn])
                if board[irow][icolumn + 1] != '.':
                    digits.remove(board[irow][icolumn + 1])
                if board[irow + 1][icolumn - 1] != '.':
                    digits.remove(board[irow + 1][icolumn - 1])
                if board[irow + 1][icolumn] != '.':
                    digits.remove(board[irow + 1][icolumn])
                if board[irow + 1][icolumn + 1] != '.':
                    digits.remove(board[irow + 1][icolumn + 1])
                sub_left_num_map[(irow, icolumn)] = digits

        # forth solve for each cell, left valid num can be filled
        cell_left_num_map = {}
        for ir in range(0, 9):
            for ic in range(0, 9):
                if board[ir][ic] != '.':
                    continue
                cell_left_num_map[(ir, ic)] = set(row_left_num_list[ir]) & \
                                              set(column_left_num_list[ic]) & \
                                              set(sub_left_num_map[(3*(ir//3)+1, 3*(ic//3)+1)])

        # final solve answer
        # for ir, ic in cell_left_num_map.keys():

    def getCandidates(self, board, irow, icolumn):
        all_num_set = set()
        for index in range(0, len(board)):
            all_num_set.add(board[irow][index])
            all_num_set.add(board[index][icolumn])
        for i in range(3 * (irow // 3), 3 * (irow // 3) + 3):
            for j in range(3 * (icolumn // 3), 3 * (icolumn // 3) + 3):
                all_num_set.add(board[i][j])
        num_set = {'1', '2', '3', '4', '5', '6', '7', '8', '9', '.'}
        res_num_set = num_set - all_num_set
        return res_num_set

    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        self.helper(board)

    def helper(self, board):
        for ir in range(0, len(board)):
            for ic in range(0, len(board)):
                if board[ir][ic] != '.':
                    continue
                reminder_poss_num = self.getCandidates(board, ir, ic)
                if len(reminder_poss_num) == 0:
                    return False
                for ch in reminder_poss_num:
                    board[ir][ic] = ch
                    if self.helper(board):
                        return True
                    board[ir][ic] = '.'
                return False
        return True


if __name__ == '__main__':
    sol = Solution()
    print(sol.solveSudoku([
        ["5", "3", ".", ".", "7", ".", ".", ".", "."],
        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"]
    ]))
