class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        n = len(nums)
        prefix = [nums[0]]
        for i in range(1, n):
            prefix.append(nums[i] + prefix[-1])
        
        for i in range(n):
            left = prefix[i-1] if i != 0 else 0
            right = prefix[n-1] - prefix[i]

            if left == right:
                return i
        return -1 


