class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        left = 0
        nums_set = set()
        
        for right in range(len(nums)):
            while right - left > k:
                nums_set.remove(nums[left])
                left += 1

            if nums[right] in nums_set:
                return True
            
            nums_set.add(nums[right])
        return False
