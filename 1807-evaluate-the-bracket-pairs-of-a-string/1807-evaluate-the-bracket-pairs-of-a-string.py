class Solution:
    def evaluate(self, s: str, knowledge: List[List[str]]) -> str:
        kmap=defaultdict(str)
        for key,val in knowledge:
            kmap[key]=val
        l=0
        res=''
        flag=0
        for r, ch in enumerate(s):
            if ch == '(':
                l=r+1
                flag=1
            elif ch == ')':
                if s[l:r] not in kmap:
                    word='?'
                else:
                    word=kmap[s[l:r]]
                res+=word
                flag=0
            elif flag==0:
                res+=ch
        return res
            