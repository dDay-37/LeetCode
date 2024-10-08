class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        row,col=len(grid),len(grid[0])
        gx3=[[0]*3*col for _ in range(3*row)]
        for i in range(row):
            for j in range(col):
                if grid[i][j]=='/':
                    gx3[i*3][j*3+2]=1
                    gx3[i*3+1][j*3+1]=1
                    gx3[i*3+2][j*3]=1
                elif grid[i][j]=='\\':
                    gx3[i*3][j*3]=1
                    gx3[i*3+1][j*3+1]=1
                    gx3[i*3+2][j*3+2]=1
        def dfs(r,c,visit):
            if (r<0 or c<0 or r==row*3 or c==col*3 or gx3[r][c]!=0 or (r,c) in visit):
                return
            visit.add((r,c))
            dfs(r-1,c,visit)
            dfs(r,c-1,visit)
            dfs(r+1,c,visit)
            dfs(r,c+1,visit)
        visit=set()
        res=0
        for i in range(row*3):
            for j in range(col*3):
                if (gx3[i][j]==0 and (i,j) not in visit):
                    dfs(i,j,visit)
                    res+=1
        return res
 