"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        visited = {}
        visited[node] = Node(node.val)
        q = deque([node])

        while len(q) != 0:
            v = q.popleft()

            for i in v.neighbors:
                if i not in visited:
                    q.append(i)
                    visited[i] = Node(i.val)
                visited[v].neighbors.append(visited[i])
            
        return visited[node]