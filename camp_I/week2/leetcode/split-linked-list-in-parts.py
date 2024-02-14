# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        length = 0
        curr = head
        while curr:
            length += 1
            curr = curr.next
        
        size = length // k
        rem = length % k
        
        curr = head

        res = []
        while curr:
            size += 1 if rem else 0
            i = 0
            newHead = curr
            while curr.next and (i < size - 1 ):
                curr = curr.next
                i += 1
            
            nextCurr = curr.next
            curr.next = None
            res.append(newHead)
            curr = nextCurr

            size -= 1 if rem else 0
            rem -= 1 if rem else 0
        
        while len(res) < k:
            res.append(ListNode(val=''))
        
        return res