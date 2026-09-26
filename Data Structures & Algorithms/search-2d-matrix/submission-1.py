class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        low = 0
        high = len(matrix)*len(matrix[0]) - 1
        nrows = len(matrix)
        ncols = len(matrix[0])
        while (low <= high):
            mid = low + (high - low)//2
            if (matrix[int(mid/ncols)][mid%ncols] > target):
                high = mid - 1
            elif (matrix[int(mid/ncols)][mid%ncols] < target):
                low = mid+1
            else:
                return True
        return False
