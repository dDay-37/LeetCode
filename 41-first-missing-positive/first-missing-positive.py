class Solution(object):
    def firstMissingPositive(self, nums):
        for i in range(len(nums)):
            if nums[i]<0:
                nums[i]=0
        print("get rid of all neg and 0")
        print(nums)
        for i in range(len(nums)):
            if nums[i]!=0:
                id = abs(nums[i])-1
                if id<len(nums):
                    if nums[id]==0:
                        nums[id]=float('-inf')
                    else:
                        nums[id]=-abs(nums[id])
        mn=min(nums)
        print("mark pos val, in range len(nums) as neg")
        print(nums)
        for i in range(len(nums)):
            if nums[i]>=0:
                return i+1
        return -mn+1