class Solution:
    def longestPalindrome(self, s: str) -> str:
        res=''
        resLen=[0]
        def chkpal(l,r):
            nonlocal res
            while l>=0 and r <len(s) and s[l]==s[r]:
                if (r-l+1) > resLen[0]:
                    resLen[0]= r-l +1
                    res=s[l:r+1]
                l-=1
                r+=1
                
    
        for i in range(len(s)):
            l,r=i,i
            chkpal(l,r)
            l,r=i,i+1
            chkpal(l,r)
        return res
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         maxLen=0
#         maxStr=''
#         for i in range(len(s)):
#             l,r=i,i
#             while l>=0 and r<len(s) and s[l]==s[r]:
#                 if maxLen<r-l+1:
#                     maxLen=r-l+1
#                     maxStr=s[l:r+1]
#                 l-=1
#                 r+=1
#         for i in range(len(s)):
#             l,r=i,i+1
#             while l>=0 and r<len(s) and s[l]==s[r]:
#                 if maxLen<r-l+1:
#                     maxLen=r-l+1
#                     maxStr=s[l:r+1]
#                 l-=1
#                 r+=1
#         return maxStr
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         maxLen=0
#         stack=[]
#         maxStr=''
#         def dfs(s):
#             nonlocal maxLen
#             if len(s)=='':
#                 return True
#             for i in range(len(s)):
#                 if isValid(s[:i+1]):
#                     if len(s[:i+1])>=maxLen:                  
#                         maxLen=len(s[:i+1])
#                         stack.append(s[:i+1])
#                     dfs(s[i+1:])
#         def isValid(s):
#             l=0
#             r=len(s)-1
#             while l<r:
#                 if s[l]!=s[r]:
#                     return False
#                 l+=1
#                 r-=1
#             return True
#         dfs(s)
#         return stack[-1]
                
            
        