class Solution:
    def climbStairs(self, n: int) -> int:
        if n==0 or n==1:
            return 1
        res=0
        prev=1
        prev2=1
        for i in range(1,n):
            res=prev+prev2
            prev2=prev
            prev=res
        return res
        