class Solution(object):
    def arrayStringsAreEqual(self, word1, word2):
        """
        :type word1: List[str]
        :type word2: List[str]
        :rtype: bool
        """
        s1=""
        s2=""
        for i in word1:
            s1 = s1+i
        for j in word2:
            s2 = s2+j
        return s1==s2