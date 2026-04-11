import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if len(stones)==1:
            return stones[0]
        stones=[-x for x in stones]
        heapq.heapify(stones)
        while len(stones)>1:
            x=heapq.heappop(stones)
            y=heapq.heappop(stones)
            if x<y:
                result=x-y
            else:
                result=y-x
            if result==0:
                continue
            heapq.heappush(stones,result)
        if len(stones)==1:
            return stones[0]*-1
        return 0
        