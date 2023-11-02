class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        s = set(arr)
        c = []
        for i in s:
            c.append(arr.count(i))
        if len(c) == len(set(c)):
            return True
        return False