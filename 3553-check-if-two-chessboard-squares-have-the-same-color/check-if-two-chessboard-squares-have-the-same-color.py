class Solution:
    def checkTwoChessboards(self, c1: str, c2: str) -> bool:
        cl1='pink'
        cl2='blue'
        if c1[0] in ['a','c','e','g']:
            if int(c1[1])%2==1:
                cl1='black'
            else:
                cl1='white'
        else:
            if int(c1[1])%2==0:
                cl1='black'
            else:
                cl1='white'
        if c2[0] in ['a','c','e','g']:
            if int(c2[1])%2==1:
                cl2='black'
            else:
                cl2='white'
        else:
            if int(c2[1])%2==0:
                cl2='black'
            else:
                cl2='white'
        return cl1==cl2