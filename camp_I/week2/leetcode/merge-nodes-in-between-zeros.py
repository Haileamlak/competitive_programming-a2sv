# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy_head = ListNode()
        dummy_tail = dummy_head

        curr = head.next
        currSum = 0
        while curr:
            if curr.val == 0:
                dummy_tail.next = ListNode(currSum)
                dummy_tail = dummy_tail.next
                currSum = 0
            else:
                currSum += curr.val
            
            curr = curr.next
        
        return dummy_head.next