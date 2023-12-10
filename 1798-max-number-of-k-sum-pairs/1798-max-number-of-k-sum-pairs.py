class Solution(object):
    def maxOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort()
        i=0
        j=len(nums)-1
        c=0
        while i<j:
            x = nums[i] + nums[j]
            if x==k:
                c+=1
                i+=1
                j-=1
            elif x<k:
                i+=1
            elif x>k:
                j-=1
        return c