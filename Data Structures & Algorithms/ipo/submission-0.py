class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        projects = sorted(zip(capital, profits))
        heap = []
        i = 0
        n = len(projects)

        for _ in range(k):
            while i < n and w >= projects[i][0]:
                heapq.heappush(heap, -projects[i][1])
                i += 1
            
            if len(heap) == 0:
                return w
            
            w -= heapq.heappop(heap)
        return w