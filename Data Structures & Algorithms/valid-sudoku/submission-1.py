class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Divide into 3 components first, then we will see if there is a scope to do anything combined
        n=9
        for i in range(9):
            # Horizontal traversal
            j=0
            counter1={}
            for j in range(9):
                if board[i][j]!='.':
                    if board[i][j] not in counter1:
                        counter1[board[i][j]]=1
                    else:
                        return False
            counter2={}
            # Vertical Traversal
            for j in range(9):  
                if board[j][i]!='.':
                    if board[j][i] not in counter2:
                        counter2[board[j][i]]=1
                    else:
                        return False
            # Square Traversal
            counter3={}
            for j in range(9):
                row = 3 * (i // 3) + (j // 3)
                col = 3 * (i % 3) + (j % 3)
                if board[row][col]!='.':
                    if board[row][col] not in counter3:
                        counter3[board[row][col]]=1
                    else:
                        return False
        return True



