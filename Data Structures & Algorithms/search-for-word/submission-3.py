class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS = len(board)
        COLS = len(board[0])

        def dfs(r, c, i, visited):
            if i == len(word):
                return True
            if r < 0 or c < 0 or r >= ROWS or c >= COLS or (r, c) in visited:
                return False

            if board[r][c] != word[i]:
                return False

            visited.add((r, c))

            found = (dfs(r + 1, c, i + 1, visited) or 
                    dfs(r, c + 1, i + 1, visited) or 
                    dfs(r - 1, c, i + 1, visited) or 
                    dfs(r, c - 1, i + 1, visited))
            
            visited.remove((r, c))
            return found

            
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == word[0]:
                    if dfs(r, c, 0, set()):
                        return True
        return False