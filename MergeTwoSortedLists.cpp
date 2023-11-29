/*
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.

 

Example 1:

Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]
  
Example 2:

Input: list1 = [], list2 = []
Output: []
  
Example 3:

Input: list1 = [], list2 = [0]
Output: [0]
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
    ListNode* mergeTwoLists(ListNode* list1, ListNode* list2) {
        ListNode *res, *head;

        if(!list1)
            return list2;
        else if(!list2) 
            return list1;
        
        else if(list1->val < list2->val)
        {
            res = head = list1;
            list1 = list1->next;
        }
        else 
        {
            res = head = list2;
            list2 = list2->next;
        }
        
        while(list1 && list2){
            if(list1->val < list2->val)
            {
                res->next = list1;
                list1 = list1->next;
            }
            else {
                res->next = list2;
                list2 = list2->next;
            }
            res = res->next;
        }
        if(list1)
            res->next = list1;
        if(list2)
            res->next = list2;

        return head;
    }
};
