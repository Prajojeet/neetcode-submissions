class Solution:

    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        path = set()

        def bt_dfs(r, c, i):
            # Base Case (Matched)
            if i == len(word):
                return True

            # Base Case 2
            if (r < 0 or c < 0 or r >= ROWS or c >= COLS or 
                board[r][c] != word[i] or 
                (r,c) in path):
                return False
                
            path.add((r, c)) # To reject already visited units
            res = (bt_dfs(r-1, c, i+1) or 
                bt_dfs(r, c-1, i+1) or
                bt_dfs(r+1, c, i+1) or
                bt_dfs(r, c+1, i+1))     
            path.remove((r, c)) # Remove the visited unite from the memory!
            return res

        for r in range(ROWS):
            for c in range(COLS):
                if bt_dfs(r,c,0):
                    return True
        return False