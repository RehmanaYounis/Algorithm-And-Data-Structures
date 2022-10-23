class Solution(object):
    def letterCombinations(self, digits):
        keyMap={
            '1':'',
            '2':'abc',
            '3':'def',
            '4':'ghi',
            '5':'jkl',
            '6':'mno',
            '7':'pqrs',
            '8':'tuv',
            '9':'wxyz'            
        }
        if len(digits)==0:
            return []
        res=[]
        stack=[]
        def dfs(i):
            if i >= len(digits):
                res.append(''.join(stack[::]))
                return
            for ch in keyMap[digits[i]]:
                stack.append(ch)
                dfs(i+1)
                stack.pop()
        dfs(0)
        return res
        