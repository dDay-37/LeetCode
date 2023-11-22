class Solution(object):
    def findDiagonalOrder(self, nums):
        m = len(nums)
        a, b, c = 0, 0, 0
        d = [[] for _ in range(100001)]

        for i in range(m):
            b += len(nums[i])
            for j in range(len(nums[i])):
                e = i + j
                d[e].append(nums[i][j])
                a = max(a, e)

        res = [0] * b
        for i in range(a + 1):
            f = d[i]
            for j in range(len(f) - 1, -1, -1):
                res[c] = f[j]
                c += 1

        return res
        