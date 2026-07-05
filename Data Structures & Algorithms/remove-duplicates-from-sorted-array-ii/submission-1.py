class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        num_counts = collections.defaultdict(int)
        left = right = 0

        while right < len(nums):
            num = nums[right]
            if num_counts[num] < 2:
                num_counts[num] += 1
                print(num, left)
                nums[left] = num
                left += 1
                right += 1
            else:

                while right < len(nums) and num == nums[right]:
                    right += 1

        return left
