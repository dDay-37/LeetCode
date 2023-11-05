class Solution(object):
    def getWinner(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: int
        """
        m=max(arr)
        if k>=len(arr):
            return m
        w=0
        i=0
        j=1
        while w < k:
            if arr[i] == m:
                break
            if arr[i]>arr[j]:
                j+=1
                w+=1
            else:
                i=j
                j+=1
                w=1
            
        return arr[i]