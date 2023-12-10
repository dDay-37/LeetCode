class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        n=len(candies)
        m = max(candies)
        result = [False]*n
        for i in range(n):
            if candies[i]+extraCandies >= m:
                result[i] = True
        return result