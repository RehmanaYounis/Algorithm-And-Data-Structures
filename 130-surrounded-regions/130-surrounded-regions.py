class Solution(object):
    def solve(self, board):
        
        rows= len(board)
        cols=len(board[0])
        
        direction=[[1,0],[-1,0],[0,1],[0,-1]]
        
        def dfs(row, col):
            # global board
            # print(row,col)

            if row<0 or col <0 or row>=rows or col>=cols or board[row][col]!='O':
                return
            # print(row,col)
            board[row][col]='2'
            for d in direction:
                newrow=row+d[0]
                newcol=col+d[1]
                dfs(newrow, newcol)
            
        
        for col in range(cols):
            if board[0][col]=='O':
                dfs(0,col)
            if board[rows-1][col] =='O':
                dfs(rows-1, col)
        
        
        for row in range(rows):
            if board[row][0] == 'O':
                dfs(row, 0)
            if board[row][cols-1] == 'O':
                dfs(row, cols-1)
                
        for row in range(rows):
            for col in range(cols):
                if board[row][col]=='2':
                    board[row][col]='O'
                else:
                    board[row][col]='X'
        return board
                    