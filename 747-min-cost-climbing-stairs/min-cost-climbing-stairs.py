class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        m = [0]*(len(cost)+1)
        m[0] = 0
        m[1] = 0
        for i in range(2,len(m)):
            m[i] = min(m[i-1]+cost[i-1],m[i-2]+cost[i-2])
        return m[len(cost)]