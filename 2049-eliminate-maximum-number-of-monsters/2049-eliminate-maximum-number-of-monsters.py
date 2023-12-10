class Solution(object):
    def eliminateMaximum(self, dist, speed):
        """
        :type dist: List[int]
        :type speed: List[int]
        :rtype: int
        """
        time=[]
        n=len(speed)
        for i in range(n):
            time.append(float(dist[i])/float(speed[i]))
        time.sort()
        # print(time)
        t=0
        while t<n and t<time[t]:
            # print(t,time[t])
            t+=1
        return t