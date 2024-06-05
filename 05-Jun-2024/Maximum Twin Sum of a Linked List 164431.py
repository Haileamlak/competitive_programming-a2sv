# Problem: Maximum Twin Sum of a Linked List - https://leetcode.com/problems/maximum-twin-sum-of-a-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
    
        stack = []
        slow = fast = head
        while fast:
            stack.append(slow)
            slow = slow.next
            fast = fast.next.next
        
        res = 0
        while slow:
            res = max(res, slow.val + stack.pop().val)
            slow = slow.next
        
        return res