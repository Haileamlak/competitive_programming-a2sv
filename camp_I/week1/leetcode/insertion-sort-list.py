# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        tempHead = ListNode(0, head)
        
        prev = head
        current = head.next
        while current:
            nextCurr = current.next
            prev.next = None
            temp = tempHead
            while temp.next and current.val > temp.next.val:
                temp = temp.next
            
            equal = temp.next == None

            prev.next = current.next
            current.next = temp.next
            temp.next = current
            current = nextCurr 
            if equal:              
                prev = prev.next


        return tempHead.next
