class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        m=nums[0]
        c=1
        for i in nums[1:]:
            if m==i:
                c+=1
            else:
                c-=1
            if c==0:
                c=1
                m=i
        # c=0
        # for i in nums:
        #     if i == m:
        #         c+=1
        # if c>len(nums)//2:
        #     return m
        # else:
        #     return 
        return m