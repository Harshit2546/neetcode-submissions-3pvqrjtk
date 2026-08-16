"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
from collections import deque

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        # Map original node -> cloned node
        old_to_new = {node: Node(node.val)}
        queue = deque([node])

        while queue:
            curr = queue.popleft()

            for neighbor in curr.neighbors:
                if neighbor not in old_to_new:
                    # Clone unvisited node and queue it
                    old_to_new[neighbor] = Node(neighbor.val)
                    queue.append(neighbor)
                
                # Connect the cloned neighbor to the cloned current node
                old_to_new[curr].neighbors.append(old_to_new[neighbor])

        return old_to_new[node]


