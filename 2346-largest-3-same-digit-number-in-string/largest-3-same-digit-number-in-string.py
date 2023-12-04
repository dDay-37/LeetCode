class Solution(object):
    def largestGoodInteger(self, num):
        """
        :type num: str
        :rtype: str
        """
        m=""
        n=-1
        for i in range(len(num)-2):
            if num[i] == num[i+1] and num[i] == num[i+2] and num[i]>n:
                n=num[i]
                m=str(num[i:i+3])
        return m