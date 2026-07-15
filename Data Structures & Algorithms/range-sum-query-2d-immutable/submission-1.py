class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        m, n = len(matrix), len(matrix[0])
        self.prefix = []

        for x in range(m):
            curr = [0]
            for y in range(n):
                curr.append(curr[-1] + matrix[x][y])
            self.prefix.append(curr)
        print(self.prefix)

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        ans = 0
        x1, x2 = row1, row2
        y1, y2 = col1, col2
        for x in range(x1, x2 + 1):
            curr = self.prefix[x][y2+1] - self.prefix[x][y1]
            ans += (curr)
        return ans


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)