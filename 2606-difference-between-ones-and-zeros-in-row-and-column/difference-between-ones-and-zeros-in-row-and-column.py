class Solution(object):
    def onesMinusZeros(self, grid):
        row_count = len(grid)
        col_count = len(grid[0])
        row = [0]*row_count
        col = [0]*col_count
        i = 0
        j = 0
        for i in range(row_count):
            row[i]=grid[i].count(1)
        i = 0
        j = 0
        for i in range(col_count):
            for j in range(row_count):
                col[i]+=grid[j][i]
        i = 0
        j = 0
        for i in range(row_count):
            for j in range(col_count):
                grid[i][j] = (2 * row[i] + 2 * col[j] - (row_count + col_count))
        return grid