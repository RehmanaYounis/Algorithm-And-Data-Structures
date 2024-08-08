class Solution(object):
    def spiralOrder(self, matrix):
        rowStart, rowEnd,colStart,colEnd=0, len(matrix), 0, len(matrix[0])
        res=[]
        while rowStart < rowEnd and colStart < colEnd:
            
            for col in range(colStart,colEnd):
                res.append(matrix[rowStart][col])
            rowStart+=1
            print(rowStart, rowEnd, colStart,colEnd)
            for row in range(rowStart, rowEnd):
                res.append(matrix[row][colEnd-1])
            colEnd-=1
            print(rowStart, rowEnd, colStart,colEnd)
            if not(rowStart < rowEnd and colStart<colEnd) :
                break
            for col in range(colEnd-1, colStart-1, -1):
                res.append(matrix[rowEnd-1][col])
            rowEnd-=1
            print(rowStart, rowEnd, colStart,colEnd)
            for row in range (rowEnd-1, rowStart-1, -1):
                res.append(matrix[row][colStart])
            colStart+=1
            print(rowStart, rowEnd, colStart,colEnd)
        return res
                
            