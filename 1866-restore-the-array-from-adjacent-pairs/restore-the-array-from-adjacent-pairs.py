class Solution(object):
    def restoreArray(self, adjacentPairs):
        """
        :type adjacentPairs: List[List[int]]
        :rtype: List[int]
        """
        d = {}
        ans = []
        for p in adjacentPairs:
            d.setdefault(p[0], []).append(p[1])
            d.setdefault(p[1], []).append(p[0])
        for key in d:
            if len(d[key]) == 1:
                ans.append(key)
                ans.append(d.pop(key)[0])
                break
        while d:
            p = d.pop(ans[-1])
            if p[0] in d: 
                ans.append(p[0])
            elif len(p) > 1 and p[1] in d: 
                ans.append(p[1])
        return ans
        