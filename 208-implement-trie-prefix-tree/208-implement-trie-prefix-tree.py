class TreeNode():
    def __init__(self):
        self.children={}
        self.EOW=False
class Trie(object):
    def __init__(self):
        self.root=TreeNode()

    def insert(self, word):
        curr = self.root
        for i in word:            
            if i not in curr.children:
                curr.children[i] = TreeNode()
            curr = curr.children[i]
        curr.EOW= True
 
    def search(self, word):
        cur=self.root
        for c in word:
            if c not in cur.children:
                return False
            cur=cur.children[c]
        return cur.EOW
            
        

    def startsWith(self, prefix):
        cur=self.root
        for c in prefix:
            if c not in cur.children:
                return False
            cur=cur.children[c]
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)