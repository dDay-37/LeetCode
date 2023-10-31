class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        x = []
        n = len(word1)
        m = len(word2)
        for i in range(min(n,m)):
            x.append(word1[i])
            x.append(word2[i])

        if n>m:
            x += word1[i+1:]
        if m>n:
            x += word2[i+1:]
        
        return "".join(x)