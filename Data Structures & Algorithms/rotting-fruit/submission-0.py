class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        def is_valid(x, y):
            return 0 <= x < m and 0 <= y < n and grid[x][y] == 1
        
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        m, n = len(grid), len(grid[0])
        queue = collections.deque()
        seen = set()
        fresh = 0

        for x in range(m):
            for y in range(n):
                if grid[x][y] == 1:
                    fresh += 1
                elif grid[x][y] == 2:
                    queue.append((x, y))
                    seen.add((x, y))
        if fresh == 0:
            return 0
        
        minutes = 0
        while queue:
            if fresh == 0:
                return minutes
            for _ in range(len(queue)):
                x, y = queue.popleft()

                for dx, dy in directions:
                    nx, ny = dx + x, dy + y

                    if is_valid(nx, ny) and (nx, ny) not in seen:
                        seen.add((nx, ny))
                        queue.append((nx, ny))
                        fresh -= 1
            minutes += 1
        return -1