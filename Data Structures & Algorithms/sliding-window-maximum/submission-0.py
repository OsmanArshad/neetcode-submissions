class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        ans = []
        queue = collections.deque()

        for i, num in enumerate(nums):
            while queue and nums[queue[-1]] <= num:
                queue.pop()
            queue.append(i)

            if i - k == queue[0]:
                queue.popleft()
            
            if i >= k - 1:
                ans.append(nums[queue[0]])
        return ans
            
