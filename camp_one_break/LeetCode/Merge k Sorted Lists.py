# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None

        def merge(list1, list2):
            res = curr = ListNode()
            while list1 and list2:
                if list1.val <= list2.val:
                    curr.next = list1
                    list1 = list1.next
                else:
                    curr.next = list2
                    list2 = list2.next
                
                curr = curr.next

            if list1:
                curr.next = list1
            else:
                curr.next = list2
            
            return res.next

        def merge_list(start, end):
            if start == end:
                return lists[start]
            
            mid = start + (end - start) // 2
            left = merge_list(start, mid)
            right = merge_list(mid + 1, end)

            return merge(left, right)

        return merge_list(0, len(lists) - 1)
