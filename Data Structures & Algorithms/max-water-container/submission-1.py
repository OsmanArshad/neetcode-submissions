class Solution:
    def maxArea(self, heights: List[int]) -> int:
        ans = left = 0
        right = len(heights) - 1

        while left < right:
            curr = (right - left) * min(heights[left], heights[right])
            ans = max(ans, curr)

            if heights[right] > heights[left]:
                left += 1
            else:
                right -= 1
        
        return ans