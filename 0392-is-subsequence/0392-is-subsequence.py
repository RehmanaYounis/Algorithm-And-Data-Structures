class Solution(object):
    def isSubsequence(self, s, t):
        if len(s) >len(t):
            return False
        if s =="":
            return True
        left=0
        for right in t:
            if left < len(s) and s[left]==right:
                left+=1
        if left==len(s):
            return True
        return False
        