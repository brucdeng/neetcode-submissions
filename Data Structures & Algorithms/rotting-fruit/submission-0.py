from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        fresh = set()
        rotten = deque()
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c]==1:
                    fresh.add((r,c))
                elif grid[r][c]==2:
                    rotten.append((r,c))
        
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        time =0
        # add all rottens to a queue
        # go through queue, if rotten has fresh neighbor, remove from fresh, make it rotten and add to queue
        # once queue is empty, check if fresh is empty and return time, else return -1
        if len(fresh)==0:
            return 0
        while rotten:
            curs = []
            time+=1
            while rotten:
                curs.append(rotten.popleft())
            for cur in curs:
                for x, y in directions:
                    thing = (cur[0]+x, cur[1]+y)
                    if thing in fresh:
                        rotten.append(thing)
                        fresh.remove(thing)
        return time-1 if len(fresh)==0 else -1