class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        sm=0
        ar=[]
        ere=[]
        for i in range(n):
            sm+=nums[i]
            ar.append(sm)
            ere.append(sm)
        # print(ere)
        for j in range(n-1):
            for x in ere:
                # print(x)
                # print(ere[j])
                q=x-ere[j]
                if q>0:
                    ar.append(q)
            # print(ar)
        ar.sort()
        # print(ar)
        MOD=10**9+7
        s=0
        for d in range(left-1,right):
            s+=ar[d]
            s%=MOD
        return s

