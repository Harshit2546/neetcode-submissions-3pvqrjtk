class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack=[]
        res=[0]*len(temperatures)
        stack.append((temperatures[-1],len(temperatures)-1))
        res[len(temperatures)-1]=0
        for i in range(len(temperatures)-2,-1,-1):
            if temperatures[i]<stack[-1][0]:
                res[i]=1
                stack.append((temperatures[i],i))
            elif temperatures[i]>=stack[-1][0]:
                while stack and temperatures[i]>=stack[-1][0] :
                    stack.pop()
                if  stack:
                    numbers=stack[-1][1]-i
                else:
                    numbers=0
                res[i]=numbers
                stack.append((temperatures[i],i))
        return res


        