class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        for tokken in tokens:
                cur=tokken
                if cur == '+':
                    d1=stack.pop()
                    d2=stack.pop()
                    res=d2+d1
                    stack.append(res)
                elif cur == '-':
                    d1=stack.pop()
                    d2=stack.pop()
                    res=d2-d1
                    stack.append(res)
                elif cur == '*':
                    d1=stack.pop()
                    d2=stack.pop()
                    res=d2*d1
                    stack.append(res)
                elif cur == '/':
                    d1=stack.pop()
                    d2=stack.pop()
                    res=int(d2/d1)
                    stack.append(res)
                else:
                    stack.append(int(tokken))
        return stack[0]