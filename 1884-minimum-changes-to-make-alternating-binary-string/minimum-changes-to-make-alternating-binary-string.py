class Solution(object):
    def minOperations(self, s):
        """
        :type s: str
        :rtype: int
        """
        n=len(s)
        e0,e1,o0,o1=0,0,0,0
        for i in range(n):
            if i%2==0:
                if s[i]=='0':
                    e0+=1
                else:
                    e1+=1
            else:
                if s[i]=='0':
                    o0+=1
                else:
                    o1+=1
        return n-max(o1+e0,o0+e1)