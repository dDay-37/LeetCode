class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums)<3:
            return False
        i=j=float('inf')
        for n in nums:
            if n<=i:
                i=n
            elif n<=j:
                j=n
            else:
                return True
        return False
