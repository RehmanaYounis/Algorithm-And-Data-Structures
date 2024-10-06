class Solution:
    def isPalindrome(self, s: str) -> bool:
        def isvalidCh(ch):
            if (ord('0') <= ord(ch) <= ord('9')) \
            or (ord('a') <= ord(ch) <= ord('z')) \
            or (ord('A') <= ord(ch) <= ord('Z')):
                return True
            return False
        s= s.lower()
        l, r = 0, len(s)-1
        while l<=r:
            while l<=r and not isvalidCh(s[l]):
                l+=1
            while l<=r and not isvalidCh(s[r]):
                r-=1
            if l<r and s[l]!=s[r]:
                return False
            l+=1
            r-=1
        return True
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         s=s.lower()
#         left,right=0,len(s)-1
#         while left <=right:
#             while left<right and not self.isChar(s[left]):
#                 left+=1
#             while left<right and not self.isChar(s[right]):
#                 right-=1
#             # print(left, right, s[left],s[right])
#             if self.isChar(s[left]) and self.isChar(s[right]) and s[right]!= s[left]:
#                 return False
#             else:
#                 left+=1
#                 right-=1
#         return True
        
#     def isChar(self,c):
#         if (ord('0') <= ord(c) <= ord('9')) or (ord('a') <= ord(c) <= ord('z')) or (ord('A') <= ord(c) <= ord('Z')):
#             return True
#         return False
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         s=s.lower()
#         def isAlpha(c):
#             if ord('a')<= ord(c) <= ord('z') or ord('0') <=ord(c) <= ord('9'): return True
#             return False
#         l=0
#         r=len(s)-1
        
#         while l<r:
#             while l<r and not isAlpha(s[l]):
#                     l+=1
#             while l<r and not isAlpha(s[r]):
#                     r-=1
#             if s[l] != s[r]:
#                 return False
#             l+=1
#             r-=1
#         return True
                