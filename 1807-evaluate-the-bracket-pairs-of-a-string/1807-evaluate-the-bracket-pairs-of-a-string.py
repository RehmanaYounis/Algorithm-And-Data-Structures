class Solution:
    def evaluate(self, s: str, knowledge: List[List[str]]) -> str:
        i=0
        t=''
        wordMap=defaultdict(str)
        
        for key, val in knowledge:
            wordMap[key]=val
        print(wordMap)
        while i < len(s):
            j=i+1
            if s[i] =='(':
                while s[i] != ')':
                    i+=1
                word=s[j:i]
                replac= wordMap[word] if word in wordMap else '?'
                #print('word to replace', replac)

                t+=replac
            else:
                t+=s[i]
            i+=1
        return t
                