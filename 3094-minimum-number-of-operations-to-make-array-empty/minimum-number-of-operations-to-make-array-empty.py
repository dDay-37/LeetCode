class Solution:
    def minOperations(self, nums: List[int]) -> int:
        nums.sort()
        cr=nums[0]
        c=1
        ans=0
        nums.append(-1)
        print(nums)
        for i in nums[1:]:
            if i == cr:
                c+=1
            else:
                if c==1:
                    return -1
                print(cr,c)
                cr=i
                if c%3==0:
                    ans+=(c//3)
                # elif c%3==2:
                #     ans+=(c//3) + 1
                # elif c%3==1:
                #     ans+=(c//3) + 1
                else:
                    ans+=(c//3)+1
                c=1
        
        return ans
        