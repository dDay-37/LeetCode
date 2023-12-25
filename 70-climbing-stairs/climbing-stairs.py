class Solution(object):
    

    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        o=1
        t=1
        for i in range(n-1):
            o,t=o+t,o
        return o