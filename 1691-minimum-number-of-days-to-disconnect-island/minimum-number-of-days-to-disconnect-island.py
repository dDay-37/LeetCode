class Solution:
    def minDays(self, grid: List[List[int]]) -> int:
        r,c=len(grid),len(grid[0])
        def dfs(i,j,visited):
            if (i<0 or j<0 or i==r or j==c or (i,j) in visited or grid[i][j]==0):
                return
            visited.add((i,j))
            dfs(i-1,j,visited)
            dfs(i,j-1,visited)
            dfs(i+1,j,visited)
            dfs(i,j+1,visited)
            
        def count_islands():
            visited=set()
            count=0
            for i in range(r):
                for j in range(c):
                    if grid[i][j] and (i,j) not in visited:
                        dfs(i,j,visited)
                        count+=1
            return count
        
        if count_islands()!=1:
            return 0
        
        for i in range(r):
            for j in range(c):
                if grid[i][j]==1:
                    grid[i][j]=0
                    if count_islands()!=1:
                        return 1
                    grid[i][j]=1
        return 2