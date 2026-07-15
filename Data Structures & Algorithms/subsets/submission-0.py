class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def backtrack(curr, i):
            if len(curr) > len(nums):
                return
            ans.append(curr[:])

            for j in range(i, len(nums)):
                if nums[j] not in curr:
                    curr.append(nums[j])
                    backtrack(curr, j + 1)
                    curr.pop()
        
        ans = []
        backtrack([], 0)
        return ans