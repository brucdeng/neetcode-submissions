class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = {}
        for a, b in prerequisites:
            if b in adj:
                adj[b].append(a)
            else:
                adj[b] = [a]
            if a not in adj:
                adj[a] = []
        color = [0] * numCourses
        def dfs(node):
            color[node] = 1
            for neighbor in adj[node]:
                if color[neighbor]==1:
                    return True
                if color[neighbor]==0:
                    if dfs(neighbor):
                        return True
            color[node] = 2
            return False
        for i in adj.keys():
            if color[i]==0:
                if dfs(i):
                    return False
        return True