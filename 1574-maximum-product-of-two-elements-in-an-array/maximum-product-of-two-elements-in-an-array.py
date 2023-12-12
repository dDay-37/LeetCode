import heapq as heap

class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        heap.heapify(nums)
        maxi = heap.nlargest(2, nums)
        return (maxi[0]-1) * (maxi[1]-1)   