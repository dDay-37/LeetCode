class Solution(object):
    def maximumOddBinaryNumber(self, s):
        """
        :type s: str
        :rtype: str
        """
        c=s.count("1")
        a=''
        a+='1'*(c-1)
        a+='0'*(len(s)-c)
        a+='1'
        return a