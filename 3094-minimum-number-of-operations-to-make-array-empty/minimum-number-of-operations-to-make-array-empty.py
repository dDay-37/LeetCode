class Solution:
    def minOperations(self, nums: List[int]) -> int:
        mp =Counter(nums)
        res =0 
        for v in mp.values():
            if v==1:return -1 
            res +=math.ceil(v/3) 
        return res 