class Solution:
    def rob(self, nums: List[int]) -> int:
        # def f(i):
        #     if i==0:
        #         return nums[i]
        #     elif i<0:
        #         return 0
        #     pick = nums[i]+f(i-2)
        #     not_pick = f(i-1)
        #     return max(pick,not_pick)
        # return f(len(nums)-1)
        if len(nums)==0:
            return -1
        if len(nums)==1:
            return nums[0]
        dp=[0,nums[0]]
        for i in range(2,len(nums)+1):
            dp.append(max(nums[i-1]+dp[i-2],dp[i-1]))
        return dp[-1]