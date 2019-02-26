class Solution:
    def cherryPickup(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        new_grid = [[-1 for j in range(len(grid) + 2)]
                    for i in range(len(grid) + 2)]
        for index in range(1, len(grid) + 1):
            new_grid[index][1:len(grid) + 1] = grid[index - 1]

        cherry_count1, cherry_count2 = 0, 0

        def fromStart2End(start_row, start_col):

            if start_row == len(grid) and start_col == len(grid): return new_grid[start_row][start_col]

            if new_grid[start_row][start_col] == -1: return -1

            right_cherry, down_cherry = new_grid[start_row][start_col-1], new_grid[start_row-1][start_col]

            if right_cherry == -1 and down_cherry == -1: return -1

            # if down_cherry 

            if right_cherry != -1 and down_cherry == -1:
                tmp_ret = new_grid[start_row][start_col]
                new_grid[start_row][start_col] = 0
                return tmp_ret + right_cherry
        
            if right_cherry == -1 and down_cherry != -1:
                tmp_ret = new_grid[start_row][start_col]
                new_grid[start_row][start_col] = 0
                return tmp_ret + down_cherry
            

                
            

        print(grid, new_grid)


if __name__ == "__main__":
    sol = Solution()
    sol.cherryPickup([[0, 1, -1],
                      [1, 0, -1],
                      [1, 1,  1]])

