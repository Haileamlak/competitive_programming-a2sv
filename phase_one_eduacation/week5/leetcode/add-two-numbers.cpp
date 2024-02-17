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
};/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */