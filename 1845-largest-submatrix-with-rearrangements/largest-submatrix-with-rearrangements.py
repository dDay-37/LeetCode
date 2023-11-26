class Solution(object):
    def largestSubmatrix(self, matrix):
        m, n = len(matrix), len(matrix[0])
        for i in range(1, m):
            for j in range(n):
                if matrix[i][j] == 1:
                    matrix[i][j] += matrix[i - 1][j]
        ans = 0
        for r in matrix:
            r.sort(reverse=True)
            for j in range(n):
                ans = max(ans, r[j] * (j + 1))
        
        return ans        