from collections import defaultdict
class Solution(object):
    def maxSubarrayLength(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n=len(nums)
        d={}
        ans=0
        l=0
        for r in range(n):
            d[nums[r]]=d.get(nums[r],0)+1
            if d[nums[r]]>k:
                while nums[l]!=nums[r]:
                    d[nums[l]]-=1
                    l+=1
                d[nums[l]]-=1
                l+=1
            if r-l+1>ans: ans=r-l+1 
        return ans