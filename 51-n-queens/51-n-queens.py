class Solution(object):
    def solveNQueens(self, n):
        grid= [["."]*n for i in range(n)]
        res=[] 
        def isValid(row, col):
            for c in range(n):
                if grid[row][c]=="Q":
                    return False
            r=row
            c=col
            while r>=0 and c>=0:
                if grid[r][c]=="Q":
                    return False
                r-=1
                c-=1
            
            r=row
            c=col
            while r<n and c>=0:
                if grid[r][c]=="Q":
                    return False
                r+=1
                c-=1
            return True            
                
        
        
        def Queen(col):
            if col==n:
                copy=["".join(row) for row in grid]
                res.append(copy)
                return
            for row in range(n):
                if isValid(row, col):
                    grid[row][col]="Q"
                    Queen(col+1)
                    grid[row][col]="."
        Queen(0)
        return res