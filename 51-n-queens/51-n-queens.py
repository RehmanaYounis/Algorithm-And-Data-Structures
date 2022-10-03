class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res=[]
        rows=n
        cols=n
        grid=[]
        for row in range(rows):
            stack=[]
            for col in range(cols):
                stack.append('.')
            grid.append(stack)
        
        def isValid(row, col):
            for c in range(cols):
                if grid[row][c] =='Q':
                    return False
            r=row
            c=col
            while r>=0 and c>=0:
                if grid[r][c]=='Q':
                    return False
                r-=1
                c-=1
            r=row
            c=col
            while r<rows  and c>=0:
                if grid[r][c]=='Q':
                    return False
                r+=1
                c-=1
            return True
        
        def dfs(col):
            if col==n:
                copy=["".join(row) for row in grid]
                res.append(copy)
                return 
            
            for row in range(rows):
                if isValid(row, col):
                    grid[row][col]='Q'
                    dfs(col+1)
                    grid[row][col]='.'
        dfs(0)
        return (res)