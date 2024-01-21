class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = [0] * (len(nums) +1)
        memo[0] = 0
        memo[1] = nums[0]
        for i in range(1,len(nums)):
            val = nums[i]
            memo[i+1] = max(memo[i],memo[i-1] + val)
        return memo[len(nums)]