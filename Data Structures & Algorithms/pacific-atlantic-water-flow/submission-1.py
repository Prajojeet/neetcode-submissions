class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        ROWS = len(heights)
        COLS = len(heights[0])

        pacific = set()
        atlantic = set()

        q_pacific = deque()
        q_atlantic = deque()

        def check_pacific(r, c, prev):
            if r < 0 or c < 0 or r >= ROWS or c>= COLS or (r, c) in pacific:
                return 

            if prev <= heights[r][c]:
                q_pacific.append([r, c])
                return

        def check_atlantic(r, c, prev):
            if r < 0 or c < 0 or r >= ROWS or c>= COLS or (r, c) in atlantic:
                return 

            if prev <= heights[r][c]:
                q_atlantic.append([r, c])
                return

        for r in range(ROWS):
            for c in range(COLS):
                if r == 0 or c == 0:
                    q_pacific.append([r, c])
                
                if r == ROWS - 1 or c == COLS - 1:
                    q_atlantic.append([r, c])

        # Pacific elements
        while q_pacific:
            length = len(q_pacific)
            for i in range(length):
                r, c = q_pacific.popleft()
                pacific.add((r, c))
                check_pacific(r + 1, c, heights[r][c])
                check_pacific(r, c + 1, heights[r][c])
                check_pacific(r - 1, c, heights[r][c])
                check_pacific(r, c - 1, heights[r][c])

        while q_atlantic:
            length = len(q_atlantic)
            for i in range(length):
                r, c = q_atlantic.popleft()
                atlantic.add((r, c))
                check_atlantic(r + 1, c, heights[r][c])
                check_atlantic(r, c + 1, heights[r][c])
                check_atlantic(r - 1, c, heights[r][c])
                check_atlantic(r, c - 1, heights[r][c])

        # Both in pacific and atlantic (intersection)
        result = pacific & atlantic
        result = [list(item) for item in result]
        return result