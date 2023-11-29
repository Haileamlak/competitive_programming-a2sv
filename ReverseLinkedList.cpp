/*
Given the head of a singly linked list, reverse the list, and return the reversed list.

Example 1:

Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]
  
Example 2:

Input: head = [1,2]
Output: [2,1]
  
Example 3:

Input: head = []
Output: []
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
    ListNode* reverseList(ListNode* head) {
        if(!head)
            return nullptr;
        
        ListNode* temp1 = nullptr;    
        ListNode* temp2 = head->next;

        while(temp2)
        {
            head->next = temp1;
            temp1 = head;
            head = temp2;
            temp2 = temp2->next;
        }
        
        head->next = temp1;
        return head;
    }
};  
