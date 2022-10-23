class Solution(object):
    def partition(self, s):
        res=[]
        stack=[]
        def dfs(s):
            # print(s)
            if s=='':
                res.append(stack[::])
                return True
            for i in range(len(s)):
                cur=s[:i+1]
                # print(cur, self.isPalindrome(cur))
                if self.isPalindrome(s[:i+1]):
                    stack.append(s[:i+1])
                    # print(stack)
                    dfs(s[i+1:])
                    stack.pop()
        dfs(s)
        return res
    
    def isPalindrome(self, string):
        l=0
        r=len(string)-1
        while l<r:
            if string[l] !=string[r]:
                return False
            l+=1
            r-=1
        return True
        