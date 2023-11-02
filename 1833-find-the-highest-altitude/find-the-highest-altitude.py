class Solution(object):
    def largestAltitude(self, gain):
        """
        :type gain: List[int]
        :rtype: int
        """
        alt = 0
        m = 0
        for i in range(len(gain)):
            alt += gain[i]
            m = max(m,alt)
        return m