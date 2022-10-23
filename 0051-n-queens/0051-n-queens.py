class Solution(object):
    def solveNQueens(self, n):
        matrix=[['.' for x in range(n)] for row in range(n) ]
        rows=n
        cols=n
        res=[]
        stack=[]
        
        ######################################
        def isValid(row,col):
            for c in range(cols):
                if matrix[row][c]=='Q':
                    return False
            curRow=row
            curCol=col
            while curRow>=0 and curCol>=0:
                if matrix[curRow][curCol]=='Q':
                    return False
                curRow-=1
                curCol-=1

            curRow=row
            curCol=col
            while curRow<n and curCol>=0:
                if matrix[curRow][curCol]=='Q':
                    return False
                curRow+=1
                curCol-=1
            return True
         #################################################
        
        def dfs(col):
            if col == n:
                cur=[''.join(row) for row in matrix]
                res.append(cur)
                return
            for row in range(n):
                if isValid(row, col):
                    matrix[row][col]='Q'
                    dfs(col+1)
                    matrix[row][col]='.'
        dfs(0)
        return res
        
    