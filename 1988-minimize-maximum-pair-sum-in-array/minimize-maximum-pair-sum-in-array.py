class Solution(object):
    def minPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)//2
        nums.sort()
        s=0
        for i in range(n):
            s=max(s,nums[i]+nums[-i-1])
        return s