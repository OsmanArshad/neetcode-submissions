class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo = {}

        def dp(x, y):
            if (x, y) in memo:
                return memo[(x, y)]
            if x >= m or y >= n:
                return 0
            if (x, y) == (m - 1, n - 1):
                return 1
            
            memo[(x, y)] = dp(x + 1, y) + dp (x, y + 1)
            return memo[(x, y)]
        return dp(0, 0)