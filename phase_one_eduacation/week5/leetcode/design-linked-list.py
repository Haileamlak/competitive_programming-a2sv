
class ListNode:
    def __init__ (self, val, next):
        self.val = val
        self.next = next

class MyLinkedList:
    def __init__(self):
        self.head = None

    def get(self, index: int) -> int:
        i = 0
        current = self.head
        while current and i < index:
            current = current.next
            i += 1
    
        if current:
            return current.val
        else:
            return -1

    def addAtHead(self, val: int) -> None:
        self.head = ListNode(val, self.head)

    def addAtTail(self, val: int) -> None:
        current = self.head
        if not current:
            self.head = ListNode(val, None)
        else:
            while current.next:
                current = current.next
            
            current.next = ListNode(val, None)

    def addAtIndex(self, index: int, val: int) -> None:
        current = self.head
        previous = ListNode(0, current)
        # self.head = previous
        i = 0
        while current and i < index:
            current = current.next
            previous = previous.next
            i += 1
        
        if i == index:
            previous.next = ListNode(val, current)
            if i == 0:
                self.head = previous.next
        
        # self.head = self.head.next
          
    def deleteAtIndex(self, index: int) -> None:
        current = self.head
        previous = ListNode(0, current)
        # self.head = previous

        i = 0
        while current and i < index:
            current = current.next
            previous = previous.next
            i += 1
        
        if current:
            previous.next = current.next
            if i == 0:
                self.head = previous.next
        
        
        # self.head = self.head.next

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)