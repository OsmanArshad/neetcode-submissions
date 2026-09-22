class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        char_counts = collections.defaultdict(int)
        ans = left = 0

        for right, c in enumerate(s):
            char_counts[c] += 1

            while (right - left + 1) - max(char_counts.values()) > k:
                char_counts[s[left]] -= 1
                left += 1
            ans = max(ans, right - left + 1)
        return ans