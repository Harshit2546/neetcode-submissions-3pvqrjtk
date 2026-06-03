class Solution:
    def combinationSum2(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        # Step 1: Sort the numbers first to easily manage duplicates
        nums.sort()
        
        def backtrack(index, subset, subsetsum):
            # Base Case 1: If we reached our target sum
            if subsetsum == target:
                res.append(list(subset))
                return
            
            # Base Case 2: If we exceed target or run out of numbers, stop
            if subsetsum > target or index == len(nums):
                return
            
            # Step 2: Loop through candidates to branch out
            for i in range(index, len(nums)):
                # Skip duplicate elements at the same depth level
                if i > index and nums[i] == nums[i - 1]:
                    continue
                
                # Include nums[i]
                subset.append(nums[i])
                backtrack(i + 1, subset, subsetsum + nums[i])
                
                # Backtrack (Exclude nums[i])
                subset.pop()

        backtrack(0, [], 0)
        return res