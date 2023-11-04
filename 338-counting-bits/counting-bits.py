class Solution(object):
    def countBits(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        res=[]
        for s in range(n+1):
            x = 0
            while s!=0:
                if s&1:
                    x+=1
                s=s>>1
            res.append(x)
        return res