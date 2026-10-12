class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj = {i:[] for i in range(n)}
        for edge in edges:
            adj[edge[0]].append(edge[1])
            adj[edge[1]].append(edge[0])
        visited = set()
        def dfs(node, par):
            if node in visited:
                return False
            visited.add(node)
            for n in adj[node]:
                if n==par:
                    continue
                if not dfs(n, node):
                    return False
            return True
        return dfs(0, -1) and len(visited)==n
