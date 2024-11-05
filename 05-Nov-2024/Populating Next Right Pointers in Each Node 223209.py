# Problem: Populating Next Right Pointers in Each Node - https://leetcode.com/problems/populating-next-right-pointers-in-each-node/

"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':

        def connect_siblings(root):
            if not root:
                return
            
            if root.left:
                root.left.next = root.right

            if root.right and root.next:
                root.right.next = root.next.left

            connect_siblings(root.left)
            connect_siblings(root.right)

        connect_siblings(root)
        
        return root