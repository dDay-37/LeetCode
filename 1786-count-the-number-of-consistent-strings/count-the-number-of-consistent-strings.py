class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        a=set(allowed)
        print(a)
        c=0
        for i in words:
            f=1
            for l in i:
                if l not in a:
                    f=0
            if f:
                c+=1
        return c