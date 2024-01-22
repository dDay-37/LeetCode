class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        nums.sort()
        nums.append("-1")
        x,y=-1,1
        for i in range(len(nums)-1):
            if nums[i]==nums[i+1]:
                x=nums[i]
            if y==nums[i]:
                y+=1
        return [x,y]