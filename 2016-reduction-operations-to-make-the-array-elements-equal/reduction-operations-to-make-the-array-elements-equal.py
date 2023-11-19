class Solution(object):
    def reductionOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        freq = [0] * 50001
        for num in nums:
            freq[num] += 1
        result, operations = 0, 0
        for i in range(50000, 0, -1):
            if freq[i] > 0:
                operations += freq[i]
                result += operations - freq[i]
        return result