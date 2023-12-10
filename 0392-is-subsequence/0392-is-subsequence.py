class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        i,j,n,m=0,0,len(s),len(t)
        if n == 0:
            return True
        if m == 0:
            return False
        while i<n and j<m:
            if s[i] in t:
                j = t.index(s[i])
                t = t[j+1:]
                i+=1
            else:
                return False
        return True