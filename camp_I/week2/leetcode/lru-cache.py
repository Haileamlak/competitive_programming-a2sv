class Node():
    def __init__(self,key=0, value=0,prev=None,next=None):
        self.key = key
        self.val = value
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.count = 0
        self.head = Node()
        self.tail = Node()
        self.cache = {}

        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]

            node.next.prev = node.prev
            node.prev.next = node.next

            node.next = self.tail
            node.prev = self.tail.prev

            self.tail.prev = node
            node.prev.next = node

            return node.val
        
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]

            node.prev.next = node.next
            node.next.prev = node.prev

            node.next = self.tail
            node.prev = self.tail.prev
            self.tail.prev = node
            node.prev.next = node

            node.val = value

        elif self.capacity == self.count:
            least = self.head.next

            least.next.prev = self.head
            self.head.next = least.next 

            node = Node(key, value)

            node.prev = self.tail.prev
            node.next = self.tail
            self.tail.prev = node
            node.prev.next = node

            self.cache[key] = node

            del self.cache[least.key]

        else:
            
            node = Node(key, value)

            node.prev = self.tail.prev
            node.next = self.tail
            self.tail.prev = node
            node.prev.next = node
            
            self.cache[key] = node

            self.count += 1



# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)