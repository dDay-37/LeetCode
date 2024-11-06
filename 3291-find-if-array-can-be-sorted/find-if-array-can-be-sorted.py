class Solution:
    def canSortArray(self, nums: List[int]) -> bool:
        def  c(n):
            count = 0
            while (n):
                count += n & 1
                n >>= 1
            return count
        bits=[]
        x=sorted(nums)
        for j in nums:
            bits.append(c(j))
        bits.append(0)
        i=0
        n=len(nums)
        nums.append(-1)
        while i<n:
            if nums[i]>nums[i+1] and bits[i]==bits[i+1]:
                nums[i],nums[i+1]=nums[i+1],nums[i]
                i=0
            else:
                i+=1
        return nums[:-1]==x
                