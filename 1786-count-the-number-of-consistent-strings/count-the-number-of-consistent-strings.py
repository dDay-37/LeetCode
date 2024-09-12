class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        a=set(allowed)
        # print(a)
        c=0
        for i in words:
            f=True
            for l in i:
                if l not in a:
                    f=False
            if f:
                c+=1
        return c