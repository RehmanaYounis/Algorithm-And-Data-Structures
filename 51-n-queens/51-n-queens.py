class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res=[]
        grid= [["."]*n for i in range(n)]
        
        def Queen( col):
            if col == n:
                copy=["".join(row) for row in grid]
                print(copy)
                res.append(copy)
                
                return 
            
            for row in range(len(grid)):
                if isValid(row, col):
                    grid[row][col]='Q'
                    Queen(col+1)
                    grid[row][col]='.'
        
        def isValid(x,y):
            # check no Queen Exist in any column in that row
            for col in range(len(grid)):
                if grid[x][col]=='Q':
                    return False
            r = x; c=y;
            # Check for diagonal
            while r>=0 and c>=0:
                if grid[r][c]=='Q':
                    return False
                r-=1
                c-=1
            
            r = x; c=y;
            while r<len(grid) and c>=0:
                if grid[r][c]=='Q':
                    return False
                r+=1
                c-=1
            return True
        Queen(0)
        return res
        
        