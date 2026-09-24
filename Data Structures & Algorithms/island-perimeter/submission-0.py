class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:

        perimeter = 0
        visited = set()
        ROWS = len(grid)
        COLS = len(grid[0])

        def dfs(r, c, visited):
            # Base Case
            if r < 0 or c < 0 or r >= ROWS or c >= COLS:
                return 1
            
            if grid[r][c] != 1:
                return 1

            if (r, c) in visited:
                return 0

            # update visited
            visited.add((r,c))
            
            return (dfs(r-1, c, visited) + 
                    dfs(r, c - 1, visited) + 
                    dfs(r, c + 1, visited) + 
                    dfs(r + 1, c, visited))

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c]==1:
                    return dfs(r, c, visited)