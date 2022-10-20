class TreeNode:
    
    def __init__(self):
        self.children={}
        self.EOF=False

class Trie:

    def __init__(self):
        self.root= TreeNode()

    def insert(self, word: str) -> None:
        if len(word)==0:
            return
        cur=self.root
        for ch in word:
            if ch not in cur.children:
                cur.children[ch]=TreeNode()
            cur=cur.children[ch]
        cur.EOF=True

    def search(self, word: str) -> bool:
        if len(word)==0:
            return True
        cur=self.root
        for ch in word:
            if ch not in cur.children:
                return False
            cur=cur.children[ch]
        return cur.EOF

    def startsWith(self, prefix: str) -> bool:
        cur=self.root
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