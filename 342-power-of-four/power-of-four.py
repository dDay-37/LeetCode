class Solution(object):
    def isPowerOfFour(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n == 0:
            return False
        m = n
        one = 0
        one2 = 0
        for i in range(64):
            x = n & 1
            one += x
            n = n >> 1
            y = m & 1
            one2 += y
            m = m >> 2
        if one == 1 and one2 == 1:
            return True
        else:
            return False
