class Solution:
    def numOfSubarrays(self, arr: list[int], k: int, threshold: int) -> int:
        ans = left = 0
        target = threshold * k
        total = sum(arr[:k])

        if total >= target:
            ans += 1
        
        for right in range(k, len(arr)):
            total -= arr[left]
            total += arr[right]

            if total >= target:
                ans += 1
            left += 1
        return ans