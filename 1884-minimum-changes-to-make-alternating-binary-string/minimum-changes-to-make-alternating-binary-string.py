class Solution(object):
    def minOperations(self, s):
        """
        :type s: str
        :rtype: int
        """
        x=0
        y=0
        for i in range(len(s)):
            if i%2==0:
                if s[i]=='0':
                    x+=1
                else:
                    y+=1
            else:
                if s[i]=='0':
                    y+=1
                else:
                    x+=1
        return min(x,y)