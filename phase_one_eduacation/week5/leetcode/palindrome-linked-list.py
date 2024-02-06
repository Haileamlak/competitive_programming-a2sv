# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        stack = []
        temp = head

        while temp:
            stack.append(temp.val)
            temp = temp.next
        
        i = 0
        while head:
            if head.val != stack[len(stack) - 1 - i]:
                return False
            
            i += 1
            head = head.next
        
        return True