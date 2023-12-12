class Solution(object):
    def maxProduct(self, nums):
        m1 = float('-inf')
        m2 = float('-inf')

        for num in nums:
            if num >= m1:
                m2 = m1
                m1 = num
            elif num > m2:
                m2 = num

        return (m1 - 1) * (m2 - 1)