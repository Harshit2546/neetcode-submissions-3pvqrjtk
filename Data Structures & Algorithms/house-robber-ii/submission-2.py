class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)<=1:
            return nums[0]
        res=0
        for j in range(0,2):
            prev1=nums[j]
            prev2=0
            for i in range(1+j,len(nums)+j-1):
                include=nums[i]+prev2
                not_include=prev1
                curri=max(not_include,include)
                prev2=prev1
                prev1=curri
            res=max(res,prev1)
        return res