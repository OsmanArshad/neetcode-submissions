class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.prefix = []
        m, n = len(matrix), len(matrix[0])
        for x in range(m):
            current = [0]
            for y in range(n):
                current.append(matrix[x][y] + current[-1])
            self.prefix.append(current)

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        ans = 0

        for row in range(row1, row2 + 1):
            ans += self.prefix[row][col2 + 1] - self.prefix[row][col1]
        return ans

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)