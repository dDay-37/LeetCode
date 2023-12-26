class Solution(object):
    def numRollsToTarget(self, n, k, target):
        """
        :type n: int
        :type k: int
        :type target: int
        :rtype: int
        """
        #time = O(n*k*t)
        #space = O(n*t)
        mod= 10**9 + 7
        h={}
        def f(n,target):
            if n==0:
                return 1 if target==0 else 0
            if (n,target) in h:
                return h[(n,target)]
            res=0
            for val in range(1,k+1):
                res+=f(n-1,target-val)
                h[(n,target)]=res
            return res
        return f(n,target)%mod