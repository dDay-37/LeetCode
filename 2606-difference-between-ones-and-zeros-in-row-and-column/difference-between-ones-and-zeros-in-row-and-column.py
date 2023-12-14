class Solution(object):
    def onesMinusZeros(self, grid):
        m, n = len(grid), len(grid[0])

        r1 = [0] * m
        c1 = [0] * n
        for i in range(m):
            for j in range(n):
                r1[i] += grid[i][j]
                c1[j] += grid[i][j]

        for i in range(m):
            for j in range(n):
                grid[i][j] = 2 * (r1[i] + c1[j]) - m - n

        return grid