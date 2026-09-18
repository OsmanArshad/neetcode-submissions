class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        left = 0
        for i in range(len(nums)):
            if i < 2 or nums[i] != nums[left - 2]:
                nums[left] = nums[i]
                left += 1
        return left