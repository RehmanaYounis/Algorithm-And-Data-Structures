class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        phone={
               2: 'abc',
               3: 'def',
               4:'ghi',
               5: 'jkl',
               6: 'mno',
               7:'pqrs',
               8:'tuv',
               9:'wxyz'
              }
        
        stack=[]
        res=[]
        def dfs(i):
            if len(digits)==0:
                return
            if len(stack)==len(digits):
                res.append(''.join(stack[::]))
                return    
            for char in phone[int(digits[i])]:
                stack.append(char)
                dfs(i+1)
                stack.pop()
        dfs(0)
        return res