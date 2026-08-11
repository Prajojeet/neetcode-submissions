class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        row_start=0
        row_end=len(matrix)-1

        col_start=0
        col_end=len(matrix[0])-1

        ans=[]
        total = (row_end+1)*(col_end+1)
        counter=0
        while(counter<total):

            for j in range(col_start, col_end+1, 1):
                ans.append(matrix[row_start][j])
                counter+=1
            row_start+=1
            if counter==total:
                break
    
            for i in range(row_start, row_end+1,1):
                ans.append(matrix[i][col_end])
                counter+=1
            col_end-=1
            if counter==total:
                break
            
            for j in range(col_end, col_start-1, -1):
                ans.append(matrix[row_end][j])
                counter+=1
            row_end-=1
            if counter==total:
                break

            for i in range(row_end, row_start-1,-1):
                ans.append(matrix[i][col_start])
                counter+=1
            col_start+=1
            if counter==total:
                break

        return ans
