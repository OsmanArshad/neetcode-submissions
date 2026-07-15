class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        cur_sum = float("-inf")
        max_sum = float("-inf")

        for num in nums:
            cur_sum = max(cur_sum + num, num)
            max_sum = max(max_sum, cur_sum)
        
        cur_min = float("inf")
        max_min = float("inf")

        for num in nums:
            cur_min = min(cur_min + num, num)
            max_min = min(cur_min, max_min)
        
        total = sum(nums)
        if total == max_min:
            return max_sum
        
        return max(max_sum, total - max_min)