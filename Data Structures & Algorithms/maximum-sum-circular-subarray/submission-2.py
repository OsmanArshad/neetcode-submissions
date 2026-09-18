class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        max_sum = float("-inf")
        cur_max = float("-inf")
        for num in nums:
            cur_max = max(cur_max + num, num)
            max_sum = max(max_sum, cur_max)
        
        min_sum = float("inf")
        cur_min = float("inf")
        for num in nums:
            cur_min = min(cur_min + num, num)
            min_sum = min(min_sum, cur_min)
        
        total = sum(nums)
        if min_sum == total:
            return max_sum
        
        return max(max_sum, total - min_sum)