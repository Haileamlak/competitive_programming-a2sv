# Problem: Populating Next Right Pointers in Each Node - https://leetcode.com/problems/populating-next-right-pointers-in-each-node/

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