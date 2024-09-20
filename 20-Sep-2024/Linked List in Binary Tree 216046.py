# Problem: Linked List in Binary Tree - https://leetcode.com/problems/linked-list-in-binary-tree/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        def bfs(list_head, tree_head):
            queue = deque([(list_head, tree_head)])
            while queue:
                curr1, curr2 = queue.popleft()
                if curr1.val != curr2.val:
                    continue
                
                if not curr1.next:
                    return True

                if curr2.left:
                    queue.append((curr1.next, curr2.left))
                
                if curr2.right:
                    queue.append((curr1.next, curr2.right))

            return False

        queue = deque([root])
        while queue:
            curr = queue.popleft()
            if bfs(head, curr):
                return True

            if curr.left:
                queue.append(curr.left)

            if curr.right:
                queue.append(curr.right)

        return False