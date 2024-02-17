class Node():
    def __init__(self, val):
        self.val = val
        self.next = None

def arrayFromLinkedList():
    a = Node(1)
    b = Node(2)
    c = Node(3)
    a.next = b
    b.next = c

    head = a
    res = []
    while head:
        res.append(head.val)
        head = head.next
    
    return res

print(arrayFromLinkedList())
