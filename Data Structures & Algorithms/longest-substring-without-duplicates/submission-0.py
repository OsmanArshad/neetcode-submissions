class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        char_set = set()
        ans = 0

        for right in range(len(s)):
            c = s[right]
            while left < right and c in char_set:
                char_set.remove(s[left])
                left += 1
            ans = max(ans, right - left + 1)
            char_set.add(c)
        return ans