class Solution:
    def tribonacci(self, n: int) -> int:
        if n==0:
            return 0
        if n==1 or n==2:
            return 1
        res=0
        prev1,prev2,prev3=1,1,0
        for i in range(2,n):
            res=prev1+prev2+prev3
            prev3=prev2
            prev2=prev1
            prev1=res
        return res
            
