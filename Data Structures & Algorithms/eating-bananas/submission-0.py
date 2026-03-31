import math
class Solution:
    def helper(self,piles: List[int],h:int,t:int)->int:
        hours=0
        for i in piles:
            hours+=math.ceil(i/t)
        return hours
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        maxi=max(piles)
        if(len(piles)==h):
            return maxi
        l=1
        result=0
        while l<=maxi:
            mid=(l+maxi)//2
            if self.helper(piles,h,mid)<=h:
                result=mid
                maxi=mid-1
            elif self.helper(piles,h,mid)>h:
                l=mid+1
        return result
        



        