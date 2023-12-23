/*
Given the head of a singly linked list and two integers left and right where left <= right, reverse the nodes of the list from position left to position right, and return the reversed list.

Example 1:
Input: head = [1,2,3,4,5], left = 2, right = 4
Output: [1,4,3,2,5]
  
Example 2:
Input: head = [5], left = 1, right = 1
Output: [5]
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
    ListNode* reverseBetween(ListNode* head, int left, int right) {
        ListNode* temp = new ListNode(0);
        temp->next = head;
        ListNode* tempHead = temp;
        
        int i = 1;
        for(; i < left; i++)
            tempHead = tempHead->next;
            
        ListNode* tempEnd = tempHead->next;
        for(; i < right; i++)
            tempEnd = tempEnd->next;
        
        ListNode* End = tempEnd->next;
        tempEnd->next = nullptr;
        tempEnd = tempHead->next;
        tempHead->next = reverseList(tempHead->next);

        tempEnd->next = End;

        head = temp->next;
        delete temp;
        return head;
        
    }


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
