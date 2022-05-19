class Solution(object):
    def isValidSudoku(self, board):
        for i in range(9):
            hashmap={}
            for j in range(9):
                val=board[i][j]
                
                if val in hashmap.keys() and val !='.':
                    return False
                else:
                    hashmap[val]=True
                    
        for i in range(9):
            hashmap={}
            for j in range(9):
                val=board[j][i]
                if val in hashmap.keys() and val !='.':
                    return False
                else:
                    hashmap[val]=True
            
        hashmap=collections.defaultdict(set)
        for i in range(9):
            for j in range(9):
                val=board[i][j]
                key=(i//3, j//3)
                if val =='.':
                    continue
                if val in hashmap[key] :
                    return False
                else:
                    hashmap[key].add(val)
        return True