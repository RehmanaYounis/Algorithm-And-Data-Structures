class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]  
        for r in range(len(tokens)):
            if tokens[r]=='+':
                a=int(stack.pop())
                b=int(stack.pop())
                res=a+b
                stack.append(res)
            elif tokens[r]=='-':
                a=int(stack.pop())
                b=int(stack.pop())
                res=b-a
                stack.append(res)
            elif tokens[r]=='*':
                a=int(stack.pop())
                b=int(stack.pop())
                res=a*b
                stack.append(res)
            elif tokens[r]=='/':
                a=int(stack.pop())
                b=int(stack.pop())
                res=int(b/a)
                stack.append(res)
            else:
                stack.append(tokens[r])
        return stack[0]
            
        