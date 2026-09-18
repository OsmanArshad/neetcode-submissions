class Solution:
    def lastStoneWeight(self, stones: list[int]) -> int:
        heap = [-stone for stone in stones]
        heapq.heapify(heap)

        while len(heap) > 1:
            first = heapq.heappop(heap)
            second = heapq.heappop(heap)

            if first != second:
                new = first - second
                heapq.heappush(heap, new)
        
        return -heap[0] if heap else 0