/*
Given the head of a linked list, remove the nth node from the end of the list and return its head.
  
Example:
Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]
Example 2:

Input: head = [1], n = 1
Output: []
Example 3:

Input: head = [1,2], n = 1
Output: [1]
  */

 /**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */

class Solution {
public:
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        ListNode* end = head;
        ListNode* nMinusOneThFromEnd = head;

        if(!head)
            return nullptr;

        while(end && n){
            end = end->next;
            n--;
        }

        if(n)
            return nullptr;

        if(end){  
            end = end->next;  
        }
        else{
            end = head;
            cout<<end->val;
            head = head->next;
            delete end;
            return head;
        }

        while(end)
        {
            nMinusOneThFromEnd = nMinusOneThFromEnd->next;
            end = end->next;
        }
        
        end = nMinusOneThFromEnd->next;
        nMinusOneThFromEnd->next = nMinusOneThFromEnd->next->next;
        delete end;

        return head;
    }
};
