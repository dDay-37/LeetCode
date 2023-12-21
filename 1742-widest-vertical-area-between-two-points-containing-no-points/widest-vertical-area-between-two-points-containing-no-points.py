class Solution(object):
    def maxWidthOfVerticalArea(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        x=[i[0] for i in points]
        x.sort()
        max=0
        for i in range(len(x)-1,0,-1):
            if (x[i]-x[i-1])>max:
                max=x[i]-x[i-1]
        return max