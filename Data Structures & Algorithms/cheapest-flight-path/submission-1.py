from collections import defaultdict,deque
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj = defaultdict(list)
        for source,dest,price in flights:
            adj[source].append([dest,price])
        finalPrice = [float("inf")]*(n+1)
        queue = deque([[0,0,src]])
        while queue:
            curr_stop_count,curr_price,node=queue.popleft()
            if curr_stop_count == k+1:
                continue
            for neighbors,flight_price in adj[node]:
                if finalPrice[neighbors] > flight_price + curr_price :
                    finalPrice[neighbors] = flight_price + curr_price 
                    queue.append([curr_stop_count+1,finalPrice[neighbors],neighbors])
        return finalPrice[dst] if finalPrice[dst]!=float("inf") else -1
