class Solution(object):
    def getSumAbsoluteDifferences(self, nums):
        s = sum(nums)
        l, r = 0, s
        res = []

        for i, n in enumerate(nums):
            r -= n
            res.append(n * i - l + r - n * (len(nums) - i - 1))
            l += n

        return res