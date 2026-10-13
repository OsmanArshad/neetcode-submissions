class Solution:
    def combine(self, n: int, k: int) -> list[list[int]]:
        def backtrack(curr, i):
            if len(curr) == k:
                ans.append(curr[:])
                return
            
            for j in range(i, n + 1):
                curr.append(j)
                backtrack(curr, j + 1)
                curr.pop()
        
        ans = []
        backtrack([], 1)
        return ans