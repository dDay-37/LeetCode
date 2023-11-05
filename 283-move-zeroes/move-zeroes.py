class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        i=0
        c=0
        while c<len(nums):
            if nums[i] == 0:
                nums.pop(i)
                nums.append(0)
            else:
                i+=1
            c+=1
        