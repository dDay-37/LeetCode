class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        arr.sort()
        cnt=[]
        c=arr[0]
        arr.append('a')
        l=1
        for i in range(1,len(arr)):
            if arr[i]!=c:
                cnt.append(l)
                c=arr[i]
                l=1
            else:
                l+=1
        # print(cnt)
        if len(cnt)==len(set(cnt)):
            return True
        else:
            return False
