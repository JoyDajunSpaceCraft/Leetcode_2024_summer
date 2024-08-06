class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        col = len(grid[0])
        row = len(grid)
        res = [[0]*col for _ in range(row)]
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 0:
                    res[i][j] ==0
                if grid[i][j]==1:
                    if i==0 or (i>0 and grid[i-1][j]==0):
                        res[i][j] +=1
                    if j==0 or (j>0 and grid[i][j-1]==0):
                        res[i][j] +=1
                    if j==col-1 or (j<col-1 and grid[i][j+1]==0):
                        res[i][j]+=1
                    if i == row-1 or(i<row-1 and grid[i+1][j]==0):
                        res[i][j]+=1
        print(res)
        return sum([sum(row) for row in res])