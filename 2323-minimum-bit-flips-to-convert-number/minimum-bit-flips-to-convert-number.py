class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        n1=str(bin(start)[2:])
        n2=str(bin(goal)[2:])
        l1=len(n1)
        l2=len(n2)
        l=-1
        if l1>l2:
            n2='0'*(l1-l2) + n2
            l=l1
        else:
            n1='0'*(l2-l1) + n1
            l=l2
        c=0
        for i in range(l):
            if n1[i]!=n2[i]:
                c+=1
        return c