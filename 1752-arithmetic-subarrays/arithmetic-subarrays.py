class Solution(object):
    def checkArithmeticSubarrays(self, nums, l, r):
        """
        :type nums: List[int]
        :type l: List[int]
        :type r: List[int]
        :rtype: List[bool]
        """
        def ap(arr):
            arr.sort()
            diff = arr[1] - arr[0]
            for i in range(1, len(arr)):
                if arr[i] - arr[i-1] != diff:
                    return False
            return True

        res = []
        for i in range(len(l)):
            ar = nums[l[i]:r[i] + 1]
            res.append(ap(ar))

        return res