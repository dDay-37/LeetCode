class Solution(object):
    def maxWidthOfVerticalArea(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        a=[]
        n=0
        for i in points:
            n+=1
            a.append(i[0])
        a.sort()
        d=0
        for j in range(n-1):
            d=max(d,a[j+1]-a[j])
        return d

