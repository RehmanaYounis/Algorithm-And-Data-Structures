class Node:
    def __init__ (self):
        self.children={}
        self.eof=False
class Trie:

    def __init__(self):
        self.node=Node()

    def insert(self, word: str) -> None:
        cur=self.node
        for ch in word:
            if ch not in cur.children:
                cur.children[ch]=Node()
            cur=cur.children[ch]
        cur.eof=True
        
        
       
        

    def search(self, word: str) -> bool:
        cur=self.node
        for ch in word:
            if ch not in cur.children:
                return False
            cur=cur.children[ch]
        return cur.eof
            

    def startsWith(self, prefix: str) -> bool:
        cur=self.node
        for ch in prefix:
            if ch not in cur.children:
                return False
            cur=cur.children[ch]
        return True

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)