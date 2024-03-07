"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        res = []
        stack = []
        curr = root

        while curr or stack:
            while(curr):
                res.append(curr.val)
                queue = deque()
                for i in range(1, len(curr.children)):
                    queue.append(curr.children[i])
                
                stack.append(queue)

                if curr.children:
                    curr = curr.children[0]
                else:
                    stack.pop()
                    curr = None
            
            if stack and stack[-1]:
                curr = stack[-1].popleft()
            elif stack:
                stack.pop()
                curr = None
        
        return res