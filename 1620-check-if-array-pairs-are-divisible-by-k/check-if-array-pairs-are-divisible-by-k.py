from collections import Counter
class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        for i in range(len(arr)):
            arr[i]=arr[i]%k
        c=Counter(arr)
        # print(c)
        for v in c:
            # print(v,c[v])
            # print(k-v,c[k-v])
            if v!=0:
                if v!=k-v:
                    # print("okok")
                    if c[v]!=c[k-v]:
                        return False
                elif c[v]%2==1:
                    # print("lala")
                    return False

        return True