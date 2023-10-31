class Solution(object):
    def findArray(self, pref):
        """
        :type pref: List[int]
        :rtype: List[int]
        """
        res = []
        if len(pref)!=0:
            res.append(pref[0])
            for i in range(1,len(pref)):
                res.append(pref[i-1] ^ pref[i])
            
        return res