class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        rowStart=0
        colStart=0
        rowEnd=len(matrix)
        colEnd=len(matrix[0])
        
        res=[]
        
        while rowStart< rowEnd and colStart< colEnd:
            
            for col in range(colStart,colEnd):
                
                res.append(matrix[rowStart][col])
            
            rowStart+=1
            for row in range(rowStart, rowEnd):     
                res.append(matrix[row][colEnd-1])
            colEnd-=1
            
            if rowStart< rowEnd:
                for col in range(colEnd-1, colStart-1, -1):
                    res.append(matrix[rowEnd-1][col])
            
            rowEnd-=1
            if colStart<colEnd:
                for row in range(rowEnd-1, rowStart-1, -1):
                    res.append(matrix[row][colStart])
            colStart+=1        
        return res