class Solution(object):
    def numSpecial(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: int
        """
        c=0
        for i in range(len(mat)):
            o=0
            for j in range(len(mat[0])):
                if mat[i][j]==1:
                    o+=1
                    x=j
            if o==1:
                o=0
                for k in range(len(mat)):
                    if mat[k][x]==1:
                        o+=1
            if o==1:
                c+=1
        return c