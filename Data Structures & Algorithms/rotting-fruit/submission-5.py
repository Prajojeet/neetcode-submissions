class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        ROWS = len(grid)
        COLS = len(grid[0])

        visited = set()
        glob_visited = set()
        q = deque()


        def VisitNeigh(r, c):
            # Base Case
            if (r < 0 or c < 0 or 
                r >= ROWS or c >= COLS or (r, c) in visited 
                or grid[r][c] == 0):
                return 

            visited.add((r, c))
            q.append((r, c))

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    continue

                if grid[r][c] == 2:
                    q.append((r, c))
                    visited.add((r, c))

                glob_visited.add((r, c))

        minute = -1
        while(q):
            print(q)
            l = len(q)
            for i in range(l):
                r, c = q.popleft()
                VisitNeigh(r + 1, c)
                VisitNeigh(r, c + 1)
                VisitNeigh(r - 1, c)
                VisitNeigh(r, c - 1)   
            minute += 1

        return max(0, minute) if glob_visited == visited else -1        

            
