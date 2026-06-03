class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res=[]
        def backtrack(index,subset,subsetsum=0):
            if index==len(nums):
                if subsetsum==target:
                    res.append(list(subset))
                return 
            subset.append(nums[index])
            subsetsum=subsetsum+nums[index]
            if subsetsum<=target:
                backtrack(index,subset,subsetsum)
            dif=subset.pop()
            subsetsum=subsetsum-dif
            backtrack(index+1,subset,subsetsum)
        backtrack(0,[])
        return res