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
        d = [0] * (len(nums)+1)
        d[1] = nums[0]
        for i in range(2, len(nums)+1):
            d[i] = max(d[i-1], d[i-2]+nums[i-1])
        return d[-1]