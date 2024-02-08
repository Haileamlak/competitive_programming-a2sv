# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverse(self, head):
        if not head or not head.next:
            return head

        toBeReversed = None
        temp2 = head.next

        while temp2:
            head.next = toBeReversed
            toBeReversed = head
            head = temp2
            temp2 = temp2.next
        
        head.next = toBeReversed

        return head
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        leftHead = dummy
        i = -1
        while i < left - 2:
            leftHead = leftHead.next
            i += 1
        
        toBeReversed = leftHead.next

        rightHead = leftHead
        while i < right - 1:
            rightHead = rightHead.next
            i += 1
        
        temp2 = rightHead.next
        rightHead.next = None
        
        reversedList = self.reverse(toBeReversed)
        leftHead.next = reversedList
        toBeReversed.next = temp2

        return dummy.next


        