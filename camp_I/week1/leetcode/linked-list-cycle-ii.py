# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slowPtr = fastPtr = head
        hasCycle = False
        
        while fastPtr and fastPtr.next:
            slowPtr = slowPtr.next
            fastPtr = fastPtr.next.next

            if slowPtr == fastPtr:
                hasCycle = True
                break

        if not hasCycle:
            return None

        fastPtr = head
        while slowPtr != fastPtr:
            slowPtr = slowPtr.next
            fastPtr = fastPtr.next
        
        return slowPtr