class Solution(object):
    def customSortString(self, order, s):
        """
        :type order: str
        :type s: str
        :rtype: str
        """
        a=''
        s=list(s)
        for i in order:
            while i in s:
                a+=i
                s.remove(i)
        return a+"".join(s)