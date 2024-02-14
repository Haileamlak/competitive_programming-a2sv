# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.url = x
        self.next = None
        self.prev = None

        

class BrowserHistory:

    def __init__(self, homepage: str):
        self.curr = ListNode(homepage)
       
    def visit(self, url: str) -> None:
        newpage = ListNode(url)

        self.curr.next = newpage
        newpage.prev = self.curr
        self.curr = newpage
    def back(self, steps: int) -> str:
        temp = self.curr
        while temp.prev and steps:
            temp = temp.prev
            steps -= 1
        self.curr = temp
        return temp.url

        

    def forward(self, steps: int) -> str:
        temp = self.curr
        while temp.next and steps:
            temp = temp.next
            steps -= 1
        self.curr = temp
        return temp.url


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)