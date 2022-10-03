class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows=len(board)
        cols=len(board[0])
        directions=[[1,0],[-1,0],[0,1],[0,-1]]
        def dfs(r, c):
            if r<0 or r>=rows or c <0 or c>=cols or board[r][c]!='O':
                return
            board[r][c]='R'
            for cr, cc   in directions:
                nr=cr+r
                nc=cc+c
                dfs(nr,nc)
                
        for row in range(rows):
            for col in range(cols):
                if board[row][col] == 'O' and row in [0,rows-1] or col in [0,cols-1]:
                    dfs(row, col)
        
        for row in range(rows):
            for col in range(cols):
                if board[row][col] == 'O':
                    board[row][col] = 'X'
        
        for row in range(rows):
            for col in range(cols):
                if board[row][col] == 'R':
                    board[row][col] = 'O'            
                