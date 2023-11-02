class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return 0
        l=0
        r=sum(nums)
        for i in range(len(nums)):
            if i>0:
                l += nums[i-1]
            r -= nums[i]
            if l==r:
                return i
        return -1