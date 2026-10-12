class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = [[] for i in range(numCourses)]
        for edge in prerequisites:
            adj[edge[1]].append(edge[0])
        res = []
        state = [0]*numCourses # 0 for unvisited, 1 for visiting, 2 for visited
        def dfs(node):
            if state[node] == 1:
                return False
            if state[node]==2:
                return True
            state[node] = 1
            for n in adj[node]:
                if not dfs(n):
                    return False
            state[node] = 2
            res.append(node)
            return True
        for n in range(numCourses):
            if state[n]==0:
                if not dfs(n):
                    return []
        return res[::-1]
                