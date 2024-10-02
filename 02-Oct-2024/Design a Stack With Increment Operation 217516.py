# Problem: Design a Stack With Increment Operation - https://leetcode.com/problems/design-a-stack-with-increment-operation/

class CustomStack:

    def __init__(self, maxSize: int):
        self.stack = []
        self.size = maxSize

    def push(self, x: int) -> None:
        if self.size > len(self.stack):
            self.stack.append([x, 0])

    def pop(self) -> int:
        if not len(self.stack):
            return -1
        
        item, inc = self.stack.pop()
        
        if len(self.stack):
            self.stack[-1][1] += inc

        return item + inc

    def increment(self, k: int, val: int) -> None:
        if len(self.stack):
            index = min(len(self.stack), k) - 1

            self.stack[index][1] += val

# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)