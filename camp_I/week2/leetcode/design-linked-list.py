
class ListNode:
    def __init__ (self, val, next = None):
        self.val = val
        self.next = next

class MyLinkedList:
    def __init__(self):
        self.head = None

    def get(self, index: int) -> int:
        current = self.head
        while current and index: # index means index == 0
            current = current.next
            index -= 1
    
        if current:
            return current.val
        
        return -1

    def addAtHead(self, val: int) -> None:
        self.head = ListNode(val, self.head)

    def addAtTail(self, val: int) -> None:
        dummy = ListNode(0, self.head)
        current = dummy
        
        while current.next:
            current = current.next
        
        current.next = ListNode(val, None)

        self.head = dummy.next

    def addAtIndex(self, index: int, val: int) -> None:
        dummy = ListNode(0)
        dummy.next = self.head

        previous = dummy
        while previous.next and index != 0:
            previous = previous.next
            index -= 1
        
        if index == 0:
            new_node = ListNode(val, previous.next)
            previous.next = new_node
        
        self.head = dummy.next
          
    def deleteAtIndex(self, index: int) -> None:
        dummy = ListNode(0, self.head)

        previous = dummy
        while previous.next and index != 0:
            previous = previous.next
            index -= 1
        
        if previous.next:
            previous.next = previous.next.next

        self.head = dummy.next
        
        
# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)