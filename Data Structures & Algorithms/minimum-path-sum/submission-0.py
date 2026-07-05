class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        memo = {}

        def dp(x, y):
            if (x, y) == (m - 1, n - 1):
                return grid[x][y]
            if x >= m or y >= n:
                return float("inf")
            if (x, y) in memo:
                return memo[(x, y)]
            
            ans = min(dp(x + 1, y), dp(x, y + 1)) + grid[x][y]
            memo[(x, y)] = ans
            return ans
        return dp(0, 0)