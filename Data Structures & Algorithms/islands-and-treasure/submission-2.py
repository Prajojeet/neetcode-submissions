class Solution:
        # BFS + Recursion 
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        # We need to focus on treasures!
        # Each loop, one layer out of the treasures
        # If no treasures, we are leaving the stuff as it is

        ROWS = len(grid)
        COLS = len(grid[0])

        visited = set()
        q = deque()

        def VisitNeigh(r, c):
            # Base Case
            if (r < 0 or c < 0 or r >= ROWS or c >= COLS or
            (r, c) in visited or grid[r][c] == -1):
                return
            q.append([r, c])
            visited.add((r, c))

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append([r, c])
                    visited.add((r, c))

        dist = 0
        while q:
            length = len(q)
            for i in range(length):
                r, c = q.popleft()
                grid[r][c] = dist # Because for later iterations we will be in the
                                  # non - treasure layers and visit other layers
                VisitNeigh(r + 1, c) 
                VisitNeigh(r, c + 1)
                VisitNeigh(r - 1, c)
                VisitNeigh(r, c - 1)
            dist += 1              # Second layer compared to the previous layer
        
