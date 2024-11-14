class Solution:
    def minimizedMaximum(self, n, Q):
        beg, end = 0, max(Q)
        
        while beg + 1 < end:
            mid = (beg + end)//2
            if sum(ceil(i/mid) for i in Q) <= n:
                end = mid
            else:
                beg = mid
        
        return end