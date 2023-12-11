class Solution(object):
    def findSpecialInteger(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        n=len(arr)//4
        c=1
        print(n)
        if len(arr)==1:
            return arr[0]
        for i in range(1,len(arr)):
            if arr[i] == arr[i-1]:
                c+=1
                if c==n+1:
                    return arr[i]
            else:
                c=1
        return arr[-1]