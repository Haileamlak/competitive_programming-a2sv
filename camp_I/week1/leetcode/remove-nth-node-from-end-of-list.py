# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        endNode = dummy = ListNode(0, head)     
        i = 1
        while i <= n:
            endNode = endNode.next
            i += 1
        
        beforNthNode = dummy
        while endNode.next:
            endNode = endNode.next
            beforNthNode = beforNthNode.next
        
        beforNthNode.next = beforNthNode.next.next

        return dummy.next
        
