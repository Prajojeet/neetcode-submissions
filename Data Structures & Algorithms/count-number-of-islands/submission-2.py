class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(r, c):
            if (r < 0 or c < 0 or 
                r >= ROWS or c >= COLS or
                (r, c) in visited or 
                grid[r][c] == '0'):
                return

            visited.add((r, c))

            dfs(r, c + 1)
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c - 1)
            return 

        ROWS = len(grid)
        COLS = len(grid[0])
        visited = set()

        island = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == '1' and (r, c) not in visited:
                    dfs(r, c)
                    island += 1
        
        return island

