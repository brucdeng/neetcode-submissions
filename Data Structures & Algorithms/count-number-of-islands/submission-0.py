from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        adj = {}
        for r in range(len(grid)):
            for c, val in enumerate(grid[r]):
                if val=="1":
                    adj[(r, c)] = []
                    n = [(r, c-1), (r-1, c), (r+1, c), (r, c+1)]
                    for x in n:
                        if x[0] >= 0 and x[0] < len(grid) and x[1] >=0 and x[1] < len(grid[0]) and grid[x[0]][x[1]] == "1":
                            adj[(r, c)].append(x)
        nodes = list(adj.keys())
        visited = set()
        queue = deque()
        ans = 0
        for x in nodes:
            if x in visited:
                continue
            visited.add(x)
            queue.append(x)
            ans+=1
            while (queue):
                k = queue.popleft()
                for item in adj[k]:
                    if item not in visited:
                        queue.append(item)
                        visited.add(item)
        return ans

