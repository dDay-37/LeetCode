class Solution(object):
    def maxProduct(self, nums):
        nums.sort()                    # Sort the array in non-decreasing order
        return (nums[-1] - 1) * (nums[-2] - 1)   # Calculate the maximum product by subtracting 1 from the last two elements