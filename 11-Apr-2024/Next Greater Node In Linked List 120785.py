# Problem: Next Greater Node In Linked List - https://leetcode.com/problems/next-greater-node-in-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def num_of_nodes(self, head):
        count = 0
        while head:
            head = head.next
            count += 1
        
        return count

    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        length_of_list = self.num_of_nodes(head)
        answer = [0] * length_of_list

        stack = []
        curr = head
        for i in range(length_of_list):
            while stack and stack[-1][0] < curr.val:
                index = stack.pop()[1]
                answer[index] = curr.val
            
            stack.append((curr.val, i))

            curr = curr.next
        
        return answer