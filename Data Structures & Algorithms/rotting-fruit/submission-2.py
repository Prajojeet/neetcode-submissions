class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        ROWS = len(grid)
        COLS = len(grid[0])

        visited = set()
        all_visited = set()
        q = deque()

        def VisitNeigh(r, c):
            # Base Case 1
            if (r < 0 or c < 0 or r >= ROWS or c >= COLS 
            or (r, c) in visited):
                return 
            # Base Case 2 - Saving time on empty ones
            if grid[r][c] == 0:
                visited.add((r, c))
                return 
            
            visited.add((r, c))
            q.append([r, c])

        for r in range(ROWS):
            for c in range(COLS):
                all_visited.add((r, c))
                if grid[r][c] == 2:
                    q.append([r, c])
                    visited.add((r, c))
                elif grid[r][c] == 0:
                    visited.add((r, c))

        time = -1
        while(q):
            print(q)
            length = len(q)
            for i in range(length):
                r, c = q.popleft()

                VisitNeigh(r + 1, c)
                VisitNeigh(r, c + 1)
                VisitNeigh(r - 1, c)
                VisitNeigh(r, c - 1)
            time += 1
        
        return max(0, time) if all_visited == visited else -1

        
