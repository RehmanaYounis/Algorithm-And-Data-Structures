class Solution(object):
    def searchMatrix(self, matrix, target):
        rows=len(matrix)
        cols=len(matrix[0])    
        start=0
        end=rows-1
        
        while start<=end:
            row = (start+end)//2
            if target>matrix[row][-1]:
                start=row+1
            elif target < matrix[row][0]:
                end=row-1
            else:
                break
        
        if not (start<=end):
            return False
        row=(start+end)//2
        start=0
        end= cols -1
        print(row)
        
        
        while start<=end:
            col= (start+end)//2
            if target<matrix[row][col]:
                end=col-1
            elif target>matrix[row][col]:
                start=col+1
            else:
                return True
        return False
                
  