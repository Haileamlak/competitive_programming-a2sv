# Problem: LFU Cache - https://leetcode.com/problems/lfu-cache/

class ListNode:

    def __init__(self, value = 0, next = None, prev = None, key = 0):
        self.key = key
        self.val = value
        self.next = next
        self.prev = prev

class LFUCache:

    def __init__(self, capacity: int):
        self.size = capacity
        self.elements = {}
        self.frequency = defaultdict(int)

        self.start = ListNode()
        self.end = ListNode()

        self.end.prev = self.start
        self.start.next = self.end

        self.last_position = {}
        self.last_position[0] = self.start

    def get(self, key: int) -> int:
        if key not in self.elements:
            return -1

        node = self.elements[key]
        count = self.frequency[key]

        last = self.last_position[count]
        
        if last == node:
            temp = last.prev

            if self.frequency[temp.key] == count:
                self.last_position[count] = temp
            else:
                del self.last_position[count]

            last = temp

        node.prev.next = node.next
        node.next.prev = node.prev

        self.frequency[key] += 1
        count += 1

        if count in self.last_position:
            last = self.last_position[count]

        node.next = last.next
        last.next = node

        node.prev = last
        node.next.prev = node
      
        self.last_position[count] = node
        
        return node.val

    def put(self, key: int, value: int) -> None:
        
        if key in self.elements:
            self.elements[key].val = value

            self.get(key)

            return

        if len(self.elements) == self.size:
            curr = self.start.next

            curr.next.prev = self.start
            self.start.next = curr.next

            count = self.frequency[curr.key]
            
            last = self.last_position[count]
            
            if last == curr:
                del self.last_position[count]

            del self.elements[curr.key] # key: ListNode
            del self.frequency[curr.key]

        curr_node = ListNode(value, None, None, key)

        self.elements[key] = curr_node
        self.frequency[key] = 1

        count = self.frequency[key]

        last = None
        if count not in self.last_position:
            last = self.start
        else:
            last = self.last_position[count]

        curr_node.next = last.next
        last.next = curr_node

        curr_node.prev = last
        curr_node.next.prev = curr_node

        self.last_position[count] = curr_node

# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)