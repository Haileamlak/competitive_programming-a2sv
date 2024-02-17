# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        # setA = set()

        # setB = set()
        # curr = headB
        # while curr:
        #     setB.add(curr)
        #     curr = curr.next
        # curr = headA
        # while curr:
        #     if curr in setB:
        #         return curr
        #     curr = curr.next
        # return None



        
        # while headA or headB:
        #     # if headA and headB:
        #     #     if h
        #     if headA:
        #         if headA in setB:
        #             return headA
                
        #         setA.add(headA)
        #         headA = headA.next
            
        #     if headB:
        #         if headB in setA:
        #             return headB
                
        #         setB.add(headB)
        #         headB = headB.next
        
        # return None


        lenA = 0
        curr = headA
        while curr:
            lenA += 1
            curr = curr.next
        
        lenB = 0
        curr = headB
        while curr:
            lenB += 1
            curr = curr.next

        d = lenA - lenB
        if d > 0:
            while d:
                headA = headA.next
                d -= 1
        elif d < 0:
            while d:
                headB = headB.next
                d += 1
        
        while headA and headB and headA != headB:
            headA = headA.next
            headB = headB.next
        
        if headA:
            return headA
        
        return None