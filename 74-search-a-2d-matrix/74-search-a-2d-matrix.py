class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        #Find the row 
        ROWS=len(matrix)
        COLS= len(matrix[0])
        firstRow=0
        lastRow=ROWS-1
        
        while firstRow <= lastRow:
            row=(firstRow+lastRow)//2
            if target<matrix[row][0]:
                lastRow = row -1
            elif target>matrix[row][-1]:
                firstRow=row+1
            else:
                break
        
        startCol=0
        lastCol = COLS -1
        print(row)
        while startCol<=lastCol:
            mid = (startCol+lastCol)//2
            if target < matrix[row][mid]:
                lastCol = mid -1
            elif target>matrix[row][mid]:
                startCol = mid+1
            else:
                return True
        return False
            
            
        