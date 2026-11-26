class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        ans = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c]:
                    ans+=4 - self.countNeighbors(grid, r, c)
        return ans

    def countNeighbors(self, grid, r, c):
        nei = [(r+1, c), (r-1, c), (r, c+1), (r, c-1)]
        count = 0
        for row, col in nei:
            if row <0 or row >= len(grid) or col <0 or col >=len(grid[0]):
                continue
            elif grid[row][col]:
                count+=1
        return count