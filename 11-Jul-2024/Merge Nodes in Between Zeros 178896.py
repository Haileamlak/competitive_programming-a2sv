# Problem: Merge Nodes in Between Zeros - https://leetcode.com/problems/merge-nodes-in-between-zeros

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy_tail = dummy_head = ListNode()

        curr = head.next
        curr_sum = 0
        while curr:
            if curr.val == 0:
                dummy_tail.next = ListNode(curr_sum)
                dummy_tail = dummy_tail.next
                curr_sum = 0
            else:
                curr_sum += curr.val
            
            curr = curr.next
        
        return dummy_head.next