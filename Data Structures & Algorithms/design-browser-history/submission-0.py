class Node:
    def __init__(self, val: str, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next


class BrowserHistory:

    def __init__(self, homepage: str):
        self.current = Node(homepage)

    def visit(self, url: str) -> None:
        self.current.next = Node(url, self.current)
        self.current = self.current.next

    def back(self, steps: int) -> str:
        for _ in range(steps):
            if self.current.prev:
                self.current = self.current.prev
        return self.current.val

    def forward(self, steps: int) -> str:
        for _ in range(steps):
            if self.current.next:
                self.current = self.current.next
        return self.current.val
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)