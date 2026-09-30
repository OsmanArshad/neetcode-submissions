class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        nums_hash = collections.defaultdict(int)
        for num in nums:
            nums_hash[num] += 1
        
        heap = []
        for num, freq in nums_hash.items():
            heapq.heappush(heap, (freq, num))
            if len(heap) > k:
                heapq.heappop(heap)
        return [x[1] for x in heap]