class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for i in range(len(matrix)):
            if matrix[i][0] <= target <= matrix[i][-1]:
                l = 0
                r = len(matrix[i]) - 1 
                while(l <= r):
                    mid = (l + r)//2
                    ele = matrix[i][mid]
                    if target == ele:
                        return True
                    elif target > ele:
                        l = mid + 1
                    else:
                        r = mid - 1
            else:
                continue

        return False