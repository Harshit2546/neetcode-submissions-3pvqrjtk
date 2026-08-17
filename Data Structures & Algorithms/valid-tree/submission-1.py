from collections import defaultdict , deque
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n-1 :
            return False
        adj = defaultdict(list)
        for edge in edges :
            adj[edge[0]].append(edge[1])
            adj[edge[1]].append(edge[0])
        visited = [0]*n
        queue = deque()
        for vertex in range(n):
            if visited[vertex] == 0:
                visited[vertex] =1
                queue.append([vertex,-1])
                while queue:
                    node,parent=queue.popleft()
                    for adjVertex in adj[node]:
                        if visited[adjVertex] == 0:
                            visited[adjVertex] = 1
                            queue.append([adjVertex,node])
                        elif (adjVertex != parent):
                            return False
        return True
