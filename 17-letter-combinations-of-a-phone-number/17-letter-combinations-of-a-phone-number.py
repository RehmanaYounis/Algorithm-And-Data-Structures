class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        if len(digits)==0:
            return res
        cMap = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "qprs",
            "8": "tuv",
            "9": "wxyz",
        }
        
        stack=[]
        def dfs(i):
            if len(stack) == len(digits):
                res.append(''.join(stack[::]))
            if i>=len(digits):
                return 
            for char in cMap[digits[i]]:
                stack.append(char)
                dfs(i+1)
                stack.pop()
        dfs(0)
        return res
                