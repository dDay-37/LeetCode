class Solution(object):
    def isUgly(self, num):
        """
        :type n: int
        :rtype: bool
        """
        for p in 2, 3, 5:
            while num % p == 0 < num:
                num /= p
        return num == 1