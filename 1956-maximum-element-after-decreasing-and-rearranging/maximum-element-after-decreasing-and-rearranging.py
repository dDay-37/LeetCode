class Solution(object):
    def maximumElementAfterDecrementingAndRearranging(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        arr.sort()
        arr[0] = 1
        n = len(arr)
        for i in range(1, n):
            if arr[i] - arr[i - 1] > 1:
                arr[i] = arr[i - 1] + 1

        return arr[n-1]
        