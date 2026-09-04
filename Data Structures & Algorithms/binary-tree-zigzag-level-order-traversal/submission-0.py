# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        queue = collections.deque([(root)])
        reverse = False
        ans = []
        
        while queue:
            current = []
            for _ in range(len(queue)):
                node = queue.popleft()
                current.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            if reverse:
                ans.append(current[::-1])
            else:
                ans.append(current[:])
            reverse = not reverse
        return ans
