from collections import defaultdict
import heapq
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        dist  = [float("inf")]*n
        print(dist)
        adj = defaultdict(defaultdict)
        for edge in times:
            adj[edge[0]][edge[1]]=edge[2]
        dist[k-1]=0
        heap=[]
        heapq.heappush(heap,(0,k))
        while heap :
            curr_dist,node = heap[0]
            heapq.heappop(heap)
            for nieghbors in adj[node].keys():
                if curr_dist + adj[node][nieghbors] < dist[nieghbors-1] :
                    dist[nieghbors-1] = curr_dist + adj[node][nieghbors]
                    heapq.heappush(heap,(dist[nieghbors-1],nieghbors))
        if max(dist) == float("inf"):
            return -1
        return max(dist)
        