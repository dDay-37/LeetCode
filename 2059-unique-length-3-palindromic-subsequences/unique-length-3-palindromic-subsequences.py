class Solution(object):
    def countPalindromicSubsequence(self, s):
        """
        :type s: str
        :rtype: int
        """
        sq = 0

        for a in ascii_lowercase:
            l, r = s.find(a), s.rfind(a)
            if l != r:
                sq += len(set(s[l + 1:r]))

        return sq
