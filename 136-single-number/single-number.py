class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        # print(nums)
        i=0
        f = 0
        while i<len(nums)-1:
            # print(i)
            if nums[i] == nums[i+1]:
                i += 2
            else:
                f = 1
                return nums[i]
        if f == 0:
            return nums[-1]