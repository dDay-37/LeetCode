class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        ans=[]
        for i in range(1,len(arr)):
            arr[i]^=arr[i-1]
        for i in queries:
            if i[0]==0:
                ans.append(arr[i[1]])
            else:
                ans.append(arr[i[1]]^arr[i[0]-1])
        return ans
