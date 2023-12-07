class Solution(object):
    def largestOddNumber(self, num):
        """
        :type num: str
        :rtype: str
        """
        a=["1","3","5","7","9"]
        for i in range(len(num)-1,-1,-1):
            if num[i] in a:
                return num[:i+1]
        return ""