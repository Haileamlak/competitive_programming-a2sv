# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseListHelper(self, head):
        if not head or not head.next:
            return head

        temp = self.reverseListHelper(head.next)
        temp.next = head
        head.next = None

        return head

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def tailOfList(head):
            while head and head.next:
                head = head.next
                
            return head

        newHead = tailOfList(head)
        self.reverseListHelper(head)

        return newHead