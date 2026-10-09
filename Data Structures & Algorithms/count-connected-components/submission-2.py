class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = {i: [] for i in range(n)}
        for edge in edges:
            adj[edge[0]].append(edge[1])
            adj[edge[1]].append(edge[0])

        visited = set()
        stack = []
        ans = 0
        for i in list(adj.keys()):
            if i in visited:
                continue
            ans+=1
            stack.append(i)
            while stack:
                cur = stack.pop()
                for neighbor in adj[cur]:
                    if neighbor not in visited:
                        stack.append(neighbor)
                        visited.add(neighbor)
        return ans