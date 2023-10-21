/*
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

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
        
        stack<int> number1;
        stack<int> number2;

        while(l1){
            number1.push(l1->val);
            l1 = l1->next;
        }

        while(l2){
            number2.push(l2->val);
            l2 = l2->next;
        }

        int carry = 0;
        ListNode* sum = nullptr;

        while(!number1.empty() || !number2.empty() || carry){

            if(!number1.empty()){
                carry += number1.top();
                number1.pop();

            }
            if(!number2.empty()){
                carry += number2.top();
                number2.pop();
            }

            ListNode *newNode = new ListNode(carry%10);
            newNode->next = sum;
            sum = newNode;  
            carry /= 10;
        }

        return sum;
    }
};
