class Solution(object):
    def isPathCrossing(self, path):
        """
        :type path: str
        :rtype: bool
        """
        x,y=0,0
        pos=[[0,0]]
        for i in path:
            if i=='N':
                y+=1
            elif i=='S':
                y-=1
            elif i=='E':
                x+=1
            elif i=='W':
                x-=1
            if [x,y] in pos:
                return True
            pos.append([x,y])
        return False
