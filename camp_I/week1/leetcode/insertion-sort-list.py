# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)  
        current = head

        while current:
            nextCurr = current.next
            prev = dummy

            while prev.next and current.val >= prev.next.val:
                prev = prev.next
            
            current.next = prev.next
            prev.next = current

            current = nextCurr 

        return dummy.next
