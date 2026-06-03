class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        def backtrack(index,current_xor=0):
            if index==len(nums):
                return current_xor
            include=backtrack(index+1,current_xor^nums[index])
            exclude=backtrack(index+1,current_xor)
            return include + exclude
        return backtrack(0)