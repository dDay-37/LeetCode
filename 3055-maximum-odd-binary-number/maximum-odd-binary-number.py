class Solution(object):
    def maximumOddBinaryNumber(self, s):
        """
        :type s: str
        :rtype: str
        """
        c=s.count("1")
        return '1'*(c-1)+'0'*(len(s)-c)+'1'