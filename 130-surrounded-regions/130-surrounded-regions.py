class Solution(object):
    def solve(self, board):
        rows=len(board)
        cols=len(board[0])
        visited=set()
        def dfs(r,c,board):
            if r<0 or c<0 or r==rows or c == cols or (r,c) in visited or board[r][c] !='O':
                return
            board[r][c]='R'
            dfs(r+1,c,board)
            dfs(r-1,c,board)
            dfs(r,c+1,board)
            dfs(r,c-1,board)
        for c in range(cols):
            if board[0][c]=='O':
                dfs(0,c,board)
            if board[rows-1][c]=='O':
                dfs(rows-1,c,board)
        for r in range(rows):
            if board[r][0]=='O':
                dfs(r,0,board)
            if board[r][cols-1]=='O':
                dfs(r,cols-1,board)
                
        for r in range(rows):
            for c in range(cols):
                if board[r][c]!='R':
                    board[r][c]='X'
        for r in range(rows):
            for c in range(cols):
                if board[r][c]=='R':
                    board[r][c]='O'