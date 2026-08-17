class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = defaultdict(list)
        for i in prerequisites:
            adj[i[1]].append(i[0])
        inDegree = [0]*numCourses
        for vertex in adj.keys():
            for adj_vertex in adj[vertex]:
                inDegree[adj_vertex] +=1
        queue = deque()
        for idx,indegree in enumerate(inDegree):
            if indegree == 0:
                queue.append(idx)
        toposort = []
        while queue:
            node = queue.popleft()
            toposort.append(node)
            for adj_vertex in adj[node]:
                inDegree[adj_vertex] -=1
                if inDegree[adj_vertex] == 0:
                    queue.append(adj_vertex)
        if len(toposort) == numCourses:
            return toposort
        return []