class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        visited=set()
        rows=len(board)
        cols=len(board[0])
        
        def dfs(row, col, i):
            if i == len(word):
                return True
            if  (row < 0 or row >= rows or
                col < 0 or col >= cols or
                (row, col) in visited or
                word[i] != board[row][col]):
                    return False
            visited.add((row,col))
            res=  ( dfs(row+1, col, i+1) or
                    dfs(row-1, col, i+1) or
                    dfs(row, col+1, i+1) or
                    dfs(row, col-1, i+1) )
            visited.remove((row, col))
            return res
        
        for row in range(rows):
            for col in range(cols):
                if dfs(row, col, 0):
                    return True
        return False