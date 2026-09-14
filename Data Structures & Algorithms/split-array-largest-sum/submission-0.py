class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def check(ans):
            subs = 1
            current = 0

            for num in nums:
                if current + num > ans:
                    subs += 1
                    current = num
                    if subs > k:
                        return False
                else:
                    current += num
            return True

        left, right = max(nums), sum(nums)
        while left <= right:
            mid = (left + right) // 2
            if check(mid):
                right = mid - 1
            else:
                left = mid + 1
        return left