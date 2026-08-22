class Solution:
    def __init__(self):
        self.area=0
    def dfs(self, grid, i, j, visited):
        visited[i][j]=True
        self.area+=1
        if i-1>=0 and grid[i-1][j]==1 and not visited[i-1][j]:
            self.dfs(grid,i-1,j,visited)
        if j-1>=0 and grid[i][j-1]==1 and not visited[i][j-1]:
            self.dfs(grid,i,j-1,visited)
        if i+1<len(grid) and grid[i+1][j]==1 and not visited[i+1][j]:
            self.dfs(grid,i+1,j,visited)
        if j+1<len(grid[0]) and grid[i][j+1]==1 and not visited[i][j+1]:
            self.dfs(grid,i,j+1,visited)    

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        outer_len=len(grid)
        inner_len=len(grid[0])
        visited=[[False]*inner_len for _ in range(outer_len)]
        max_area=0
        for i in range(outer_len):
            for j in range(inner_len):
                if grid[i][j]==1 and not visited[i][j]:
                    self.area=0
                    self.dfs(grid,i,j,visited)
                    max_area=max(max_area,self.area)
        return max_area