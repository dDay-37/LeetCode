class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        x=dict(Counter(arr))
        c=0
        # print(x)
        for key in x:
            if x[key]==1:
                c+=1
                if c==k:
                    return key
        return ""