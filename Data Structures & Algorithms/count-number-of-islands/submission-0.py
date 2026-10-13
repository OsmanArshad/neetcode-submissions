class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def is_valid(x, y):
            return 0 <= x < m and 0 <= y < n and grid[x][y] == "1"
        
        def dfs(x, y):
            for dx, dy in directions:
                nx, ny = dx + x, dy + y
                if is_valid(nx, ny) and (nx, ny) not in seen:
                    seen.add((nx, ny))
                    dfs(nx, ny)
        
        directions = [(0,1), (1,0), (-1,0), (0,-1)]
        m, n = len(grid), len(grid[0])
        seen = set()
        ans = 0

        for x in range(m):
            for y in range(n):
                if (x, y) not in seen and grid[x][y] == "1":
                    seen.add((x, y))
                    dfs(x, y)
                    ans += 1
        return ans