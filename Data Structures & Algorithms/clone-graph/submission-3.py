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
            return node
        adj = {}
        adj[node] = Node(node.val)
        queue = deque([node])
        while queue:
            cur = queue.popleft()
            for n in cur.neighbors:
                if n not in adj:
                    adj[n] = Node(n.val)
                    queue.append(n)
                adj[cur].neighbors.append(adj[n])
        return adj[node]