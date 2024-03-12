# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prefix_sum = {}
        new_head = ListNode(0, head)
        curr_sum = 0
        curr = new_head
        while curr:
            curr_sum += curr.val
            
            if curr_sum in prefix_sum:
                prev = prefix_sum[curr_sum]
                temp_curr = prev.next
                temp_sum = curr_sum + temp_curr.val

                while temp_sum != curr_sum:
                    del prefix_sum[temp_sum]
                    temp_curr = temp_curr.next
                    temp_sum += temp_curr.val

                prefix_sum[curr_sum].next = curr.next
                prev.next = temp_curr.next
            else:
                prefix_sum[curr_sum] = curr

            curr = curr.next
        
        return new_head.next