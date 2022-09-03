class Solution(object):
    def isValidSudoku(self, board):
        rows= len(board)
        cols=len(board[0])

        def isValid(r,c, val):

            for col in range(cols):
                if col != c and board[r][col]==val:
                    print('colwrong' , val, board[r][col])
                    return False
            for row in range(rows):
                if row != r and board[row][c]==val:
                    print(' row wrong')
                    return False

            UC= (c//3) * 3
            UR = (r//3) *3
            print(UC, UR)
            for i in range(3):
                for j in range(3):
                    nr = i + UR
                    nc=   j+ UC
                    print('new coord',nr,nc)
                    if (nr != r and nc != c and board[nr][nc]==val):
                        print('Wrong cube' , r,c , val)
                        return False
            print(r,c, "Correct")
            return True

        for cr in range(rows):
            for cc in range(cols):
                if board[cr][cc] != ".":
                    print(cr,cc)
                    if not isValid(cr,cc, board[cr][cc]):
                        return False
        return True