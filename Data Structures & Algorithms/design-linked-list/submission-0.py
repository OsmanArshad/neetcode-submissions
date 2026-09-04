class ListNode:

    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class MyLinkedList:

    def __init__(self):
        self.root = ListNode(-1)
        self.size = 0
        

    def get(self, index: int) -> int:
        if index >= self.size:
            return -1
        
        curr = self.root.next
        for _ in range(index):
            curr = curr.next
        return curr.val

    def addAtHead(self, val: int) -> None:
        self.addAtIndex(0, val)
        

    def addAtTail(self, val: int) -> None:
        self.addAtIndex(self.size, val)
        

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.size:
            return None
        
        curr = self.root
        for _ in range(index):
            curr = curr.next
        
        next_node = ListNode(val, curr.next)
        curr.next = next_node
        self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        if index >= self.size:
            return None
        
        curr = self.root
        for _ in range(index):
            curr = curr.next        
        
        curr.next = curr.next.next
        self.size -= 1


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)