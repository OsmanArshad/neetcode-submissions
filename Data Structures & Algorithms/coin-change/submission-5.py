class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}

        def dp(value):
            if value in memo:
                return memo[value]
            if value == 0:
                return 0
            
            ans = float("inf")
            for coin in coins:
                if value - coin >= 0:
                    ans = min(ans, dp(value - coin) + 1)
            memo[value] = ans
            return ans
        ans = dp(amount)
        return ans if ans != float("inf") else -1