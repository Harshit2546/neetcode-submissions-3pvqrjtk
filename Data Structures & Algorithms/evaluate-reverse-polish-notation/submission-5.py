import operator
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        if(len(tokens)==1):
             return int(tokens[0])
        list=['+','-','*','/']
        dict={'+':operator.add,'-':operator.sub,'*':operator.mul,'/':operator.truediv}
        stack=[]
        result=0
        for i in tokens:
            if i in list:
                first=stack.pop()
                second=stack.pop()
                result=int(dict[i](second,first))
                stack.append(result)
            else:
                stack.append(int(i))
        return result
            


            