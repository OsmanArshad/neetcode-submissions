# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.counter = 0
        self.ans = None
        def dfs(node):
            if not node:
                return

            dfs(node.left)
            print(node.val)
            self.counter += 1
            if self.counter == k:
                self.ans = node.val
            dfs(node.right)
        dfs(root)
        return self.ans