class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        self.prefix = [[0 for i in range(len(matrix[0]))] for k in range(len(matrix))]
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                self.prefix[r][c] += matrix[r][c]
                if r-1 >=0:
                    self.prefix[r][c] += self.prefix[r-1][c]
                if c-1 >= 0:
                    self.prefix[r][c] += self.prefix[r][c-1]
                if c-1 >=0 and r-1 >=0:
                    self.prefix[r][c] -= self.prefix[r-1][c-1]
        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        #return self.prefix
        bigSum = self.prefix[row2][col2]
        if row1-1 >=0:
            bigSum -= self.prefix[row1-1][col2]
        if col1 -1 >=0:
            bigSum -= self.prefix[row2][col1-1]
        if row1-1 >=0 and col1-1>=0:
            bigSum += self.prefix[row1-1][col1-1]
        return bigSum


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)