# Problem: Maximum Twin Sum of a Linked List - https://leetcode.com/problems/maximum-twin-sum-of-a-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        
        def get_length(head):
            curr = head
            count = 0
            while curr:
                count += 1
                curr = curr.next
            
            return count

        stack = []
        length = get_length(head)
        curr = head
        while len(stack) < length // 2:
            stack.append(curr)
            curr = curr.next
        
        res = 0
        while curr:
            res = max(res, curr.val + stack.pop().val)
            curr = curr.next
        
        return res