class Solution(object):
    def countPairs(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort() # sort the vector nums
        count = 0 # variable to store the count
        left = 0 # variable to store the left
        right = len(nums)-1 # variable to store the right
        while(left < right): # loop until left is less than right
            if(nums[left] + nums[right] < target): # if nums[left] + nums[right] is less than target
                count += right-left # update the count
                left += 1 # increment the left
            else: # else
                right -= 1 # decrement the right
        return count # return the count