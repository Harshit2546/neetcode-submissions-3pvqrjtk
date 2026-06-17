class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        memo = {}
        def helper(index):
            # Base Case: If we reach or pass the top, it costs 0 more to finish
            if index >= len(cost):
                return 0

            # If we already calculated the cost for this step, return it immediately
            if index in memo:
                return memo[index]

            # Recurrence relation: 
            # Cost of current step + min cost of the paths ahead
            cost_step_1 = helper(index + 1)
            cost_step_2 = helper(index + 2)

            memo[index] = cost[index] + min(cost_step_1, cost_step_2)
            return memo[index]

            # The problem allows us to start at either index 0 or index 1
        return min(helper(0), helper(1))
        