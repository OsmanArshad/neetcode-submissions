# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        def merge(left, right):
            new = dummy = ListNode(-1)
            while left and right:
                if left.val < right.val:
                    new.next = left
                    left = left.next
                else:
                    new.next = right
                    right = right.next
                new = new.next
            new.next = left if left else right
            return dummy.next
                

        if not lists:
            return None
        
        while len(lists) > 1:
            merged = []

            for i in range(0, len(lists), 2):
                left = lists[i]
                right = lists[i + 1] if i + 1 < len(lists) else None
                merged.append(merge(left, right))
            lists = merged
        return lists[0]