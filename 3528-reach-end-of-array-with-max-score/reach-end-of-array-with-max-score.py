class Solution:
    def findMaximumScore(self, nums: List[int]) -> int:
        sc=0
        i=0
        j=1
        while i<len(nums)-1:
            if j==len(nums)-1 or nums[j]>nums[i]:
                sc+=(j-i)*nums[i]
                print(i,j,sc)
                i=j
                j+=1
            else:
                j+=1

        return sc