class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        prod = 1
        if nums.count(0)>1:
            # print("zeroes")
            return [0]*len(nums)
        for n in nums:
            prod *=n
        res = []
        for i in range(len(nums)):
            if nums[i]!=0:
                res.append(prod//nums[i])
            else:
                d=1
                for a in nums:
                    if a != 0:
                        d*=a
                res.append(d)

        return res