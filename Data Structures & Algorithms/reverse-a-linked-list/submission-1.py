# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode | None) -> ListNode | None:
        def reverse(prev, node):
            if not node:
                return prev
            
            next_node = node.next
            node.next = prev
            prev = node
            return reverse(prev, next_node)
        
        return reverse(None, head)