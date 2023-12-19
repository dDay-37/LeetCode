class Solution(object):
    def imageSmoother(self, img):
        m, n = len(img), len(img[0])
        res = [[0] * n for _ in range(m)]

        for i in range(m):
            for j in range(n):
                res[i][j] = self.f(img, i, j)

        return res

    def f(self, img, x, y):
        m, n = len(img), len(img[0])
        s, c = 0, 0

        for i in range(-1, 2):
            for j in range(-1, 2):
                nx, ny = x + i, y + j
                if 0 <= nx < m and 0 <= ny < n:
                    s += img[nx][ny]
                    c += 1

        return s // c
        
        