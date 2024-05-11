class Solution(object):
    def isValid(self, s):
        brackets={")":"(", "}":"{", "]":"["}
        stack=[]
        for b in s:
            if stack and b in brackets:
                if brackets[b] == stack[-1]:
                    stack.pop()    
                else:
                    return False
            else:
                stack.append(b)
        return True if not stack else False