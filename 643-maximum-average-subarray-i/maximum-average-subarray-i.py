class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        l = len(nums)
        if l == k:
            return float(sum(nums))/k
        s1 = sum(nums[:k])
        pos = 0
        val = sum(nums[:k])
        m = val
        for i in range(l-k):
            val = val - nums[i] + nums[k+i]
            m = max(m,val)
        return float(m)/k