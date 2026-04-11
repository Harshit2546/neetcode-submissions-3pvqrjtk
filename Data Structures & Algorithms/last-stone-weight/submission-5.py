import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # Create max-heap by negating values
        max_heap = [-s for s in stones]
        heapq.heapify(max_heap)

        while len(max_heap) > 1:
            # Pop the two largest stones
            first = heapq.heappop(max_heap)
            second = heapq.heappop(max_heap)
            
            # If they aren't equal, push the difference back
            if first != second:
                heapq.heappush(max_heap, first - second)

        # Return the last stone's absolute value, or 0 if empty
        return -max_heap[0] if max_heap else 0
        