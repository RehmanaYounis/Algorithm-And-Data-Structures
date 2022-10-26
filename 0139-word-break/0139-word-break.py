class Solution(object):
    def wordBreak(self, s, wordDict):
        hashMap={}
        def dfs(sen):
            if len(sen)==0:
                return True
            if sen in hashMap:
                return hashMap[sen]
            for i in range(1, len(sen)+1):
                word=sen[:i]
                if word in wordDict:
                    if dfs(sen[i:]): 
                        hashMap[sen]=True
                        return hashMap[sen]
            hashMap[sen]=False
            return hashMap[sen]
        if dfs(s): return True
