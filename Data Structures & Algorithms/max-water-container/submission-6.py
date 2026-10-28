class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left, right = 0, len(heights) - 1
        ans = 0

        while left < right:
            current = (right - left) * min(heights[left], heights[right])
            ans = max(ans, current)

            if heights[left] > heights[right]:
                right -= 1
            else:
                left += 1
        return ans