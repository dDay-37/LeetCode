class Solution(object):
    def numberOfWays(self, corridor):
        """
        :type corridor: str
        :rtype: int
        """
        s = 0
        p = 0
        d = 1
        m = 1000000007
        
        for i in corridor:
            if i == 'S':
                s += 1
            if s == 2 and i == 'P':
                p += 1
            if s == 3:
                d *= (p + 1)
                d %= m
                s = 1
                p = 0
        
        if s < 2: return 0
        return d