class TrieNode():
    def __init__(self):
        self.children={}
        self.eow=False

    def addword(self, word):
        cur=self
        for c in word:
            if c not in cur.children:
                cur.children[c]=TrieNode()
            cur=cur.children[c]
        cur.eow=True
        
class Solution(object):
    def findWords(self, board, words):
        root=TrieNode()
        for word in words:
            root.addword(word)
        visit=set()
        ROWS=len(board)
        COLS=len(board[0])
        res=set()
        def dfs(r,c,node,curword):
            if r<0 or c<0 or r==ROWS or c == COLS or (r,c) in visit or board[r][c] not in node.children:
                return
            visit.add((r,c))
            node=node.children[board[r][c]]
            curword+=board[r][c]
            if node.eow:
                res.add(curword)
            dfs(r+1,c,node,curword)
            dfs(r-1,c,node,curword)
            dfs(r,c+1,node,curword)
            dfs(r,c-1,node,curword)
            visit.remove((r,c))
        
        for r in range(ROWS):
            for c in range(COLS):
                dfs(r,c,root, "")
        return list(res)
        