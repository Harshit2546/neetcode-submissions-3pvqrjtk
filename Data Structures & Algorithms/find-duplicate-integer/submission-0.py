class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        index=0
        while True:
            if nums[index]<0:
                return index
            nums[index]=nums[index]*-1
            index=nums[index]*-1