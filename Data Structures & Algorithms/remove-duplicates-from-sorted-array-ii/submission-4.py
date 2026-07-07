class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        left = 0
        for right, num in enumerate(nums):
            if left < 2 or num != nums[left - 2]:
                nums[left] = num
                left += 1
        return left