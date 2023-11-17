class Solution(object):
    def minPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        s=0
        for i in range(len(nums)//2):
            s=max(s,nums[i]+nums[-i-1])
        return s