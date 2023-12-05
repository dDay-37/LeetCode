class Solution(object):
    def numberOfMatches(self, n):
        """
        :type n: int
        :rtype: int
        """
        m=0
        while n!=1:
            m+=n//2
            if n%2==1: n= (n+1)/2
            else: n=n/2
        return m