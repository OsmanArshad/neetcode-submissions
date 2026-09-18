class Solution:
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:
        nums1_hash = {}
        for i, num in enumerate(nums1):
            nums1_hash[num] = i
        
        ans = [-1] * len(nums1)
        stack = []
        for num in nums2:
            while stack and num > stack[-1]:
                top = stack.pop()
                if top in nums1_hash:
                    idx = nums1_hash[top]
                    ans[idx] = num
            stack.append(num)
        return ans