class Solution(object):
    def findArray(self, pref):
        for i in range(len(pref)-1,0,-1):
            pref[i] = pref[i]^pref[i-1]
        return pref