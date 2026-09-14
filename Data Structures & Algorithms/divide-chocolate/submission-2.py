class Solution:
    def maximizeSweetness(self, sweetness: List[int], k: int) -> int:
        def check(ans):
            chunks = 0
            current = 0
            for sweet in sweetness:
                current += sweet
                if current >= ans:
                    chunks += 1
                    current = 0
            return chunks >= k

        k += 1
        left, right = 1, sum(sweetness) // k
        while left <= right:
            mid = (left + right) // 2
            if check(mid):
                left = mid + 1               
            else:
                right = mid - 1
        return right