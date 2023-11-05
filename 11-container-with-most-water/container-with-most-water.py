class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        ans, i, j = 0, 0, len(height)-1
        while (i < j):
            if height[i] <= height[j]:
                res = height[i] * (j - i)
                i += 1
            else:
                res = height[j] * (j - i)
                j -= 1
            if res > ans: ans = res
        return ans
