class Solution(object):
    def minTimeToVisitAllPoints(self, points):
        return sum(max(abs(n[0] - c[0]), abs(n[1] - c[1])) for c, n in zip(points[0:-1], points[1:]))

        