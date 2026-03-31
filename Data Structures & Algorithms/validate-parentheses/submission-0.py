class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        top=0;
        for i in s:
            if stack and stack[-1]=='(' and i==')':
                stack.pop()
                top-=1
            elif stack and stack[-1]=='[' and i==']':
                stack.pop()
                top-=1
            elif stack and stack[-1]=='{' and i=='}':
                stack.pop()
                top-=1
            else:
                stack.append(i)
                top+=1
        if(len(stack)==0):
            return True
        return False            
        