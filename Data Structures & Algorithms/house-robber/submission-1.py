class Solution:
    def rob(self, nums: List[int]) -> int:
        prev1=nums[0]
        prev2=0
        for i in range(1,len(nums)):
            include=nums[i]+prev2
            not_include=prev1
            curri=max(not_include,include)
            prev2=prev1
            prev1=curri
        return prev1



            