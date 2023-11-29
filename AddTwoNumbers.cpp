/*
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself

Example 1:

Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.
  
Example 2:

Input: l1 = [0], l2 = [0]
Output: [0]
  
Example 3:

Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]
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
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        
        int num = l1->val + l2->val;
        ListNode* res = new ListNode(num%10);   
        ListNode* head = res;
        
        num/=10;
        l1 = l1->next;
        l2 = l2->next;

        while(l1 || l2)
        {
            if(l1){
                num += l1->val;
                l1 = l1->next;
            }
            if(l2){
                num += l2->val;
                l2 = l2->next;
            }
            
            res->next = new ListNode(num%10);
            res = res->next;

            num /= 10;
        }

        if(num)
            res->next = new ListNode(num);
        return head;
    }
};
