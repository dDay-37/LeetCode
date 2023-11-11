class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        zipped_set = set(zip(s, t))
        return len(zipped_set) == len(set(s)) == len(set(t))