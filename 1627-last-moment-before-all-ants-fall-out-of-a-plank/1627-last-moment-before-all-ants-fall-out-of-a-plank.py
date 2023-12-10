class Solution(object):
    def getLastMoment(self, n, left, right):
        """
        :type n: int
        :type left: List[int]
        :type right: List[int]
        :rtype: int
        """
        if len(left)==0:
            left.append(0)
        if len(right)==0:
            right.append(n)
        a=int(max(left))
        b=int(min(right))
        return max(a,n-b)