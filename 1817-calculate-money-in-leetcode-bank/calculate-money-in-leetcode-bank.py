class Solution(object):
    def totalMoney(self, n):
        """
        :type n: int
        :rtype: int
        """
        i=n//7
        d=n%7
        return 28*(i) + 7*((i*(i-1))//2) + i*d + (d*(d+1))//2
