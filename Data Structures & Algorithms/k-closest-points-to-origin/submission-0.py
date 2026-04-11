import math
import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distances=[]
        for i,j in points:
            distance=math.pow(i,2)+math.pow(j,2)
            heapq.heappush(distances,(int(-distance),i,j))
            if len(distances)>k:
                heapq.heappop(distances)
        res=[]
        for d,x,y in distances:
            res.append([x,y])
        return res



        