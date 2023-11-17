class Solution(object):
    def minPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)//2
        num=sorted(nums)
        s=0
        for i in range(n):
            s=max(s,num[i]+num[-(i+1)])
        return s