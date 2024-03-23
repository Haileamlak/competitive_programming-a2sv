# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        stack = []
        curr = head
        slow = fast = head
        while fast and fast.next:
            stack.append(slow)
            slow = slow.next
            fast = fast.next.next
        
        new_head = None

        if fast:
            new_head = slow
            slow = slow.next
            new_head.next = None
        
        while slow:
            temp1 = stack.pop()
            temp2 = slow
            slow = slow.next
            
            temp1.next = temp2
            temp2.next = new_head
            new_head = temp1
