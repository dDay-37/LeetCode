class Solution(object):
    def differenceOfSums(self, n, m):
        """
        :type n: int
        :type m: int
        :rtype: int
        """
        nums1 = []
        nums2 = []
        for i in range(1, n + 1):
            if i % m == 0:
                nums2.append(i)
            else:
                nums1.append(i)
        return sum(nums1) - sum(nums2)