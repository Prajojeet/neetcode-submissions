class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [['.' for _ in range(n)] for _ in range(n)]
        COLS = set()
        POS_DIAG = set() # r+c
        NEG_DIAG = set() # r-c
        result = []
        
        def bt_dfs(r):
            # Base Case
            if r == n:
                copy = ["".join(rows) for rows in board]
                result.append(copy)
                return 

            # Iterative Case
            for c in range(n):
                if c in COLS or (r+c) in POS_DIAG or (r-c) in NEG_DIAG:
                    continue
                COLS.add(c)
                POS_DIAG.add(r+c)
                NEG_DIAG.add(r-c)
                board[r][c] = 'Q'

                # Moving to the next row
                bt_dfs(r+1)

                # Deleting changes (Core backtracking)
                COLS.remove(c)
                POS_DIAG.remove(r+c)
                NEG_DIAG.remove(r-c)
                board[r][c] = '.'

        bt_dfs(0)
        return result