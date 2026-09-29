class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS = len(board)
        COLS = len(board[0])
        visited = set()
        converted = set()

        def dfs(r, c):
            # Base Case - out of board and element = 'X'
            if (r < 0 or c < 0 or r >= ROWS or c >= COLS or 
                board[r][c] == 'X' or (r, c) in visited):
                return

            visited.add((r, c))

            
            # Check dfs for border
            dfs(r + 1, c)
            dfs(r, c + 1)
            dfs(r - 1, c)
            dfs(r, c - 1)
                

        for r in range(ROWS):
            for c in range(COLS):
               if (r in (0, ROWS - 1) or c in (0, COLS - 1)) and board[r][c] == 'O':
                   dfs(r, c)

        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) not in visited and board[r][c] == 'O':
                    board[r][c] = 'X'

                
