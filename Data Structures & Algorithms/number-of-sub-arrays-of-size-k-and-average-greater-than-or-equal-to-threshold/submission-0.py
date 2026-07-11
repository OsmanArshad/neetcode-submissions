class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        ans, left = 0, 0
        n = len(arr)
        curr = sum(arr[0:k])
        target = threshold * k

        if curr >= target:
            ans += 1

        for i in range(k, n):
            curr = curr + arr[i] - arr[i - k]
            if curr >= target:
                ans += 1
        return ans