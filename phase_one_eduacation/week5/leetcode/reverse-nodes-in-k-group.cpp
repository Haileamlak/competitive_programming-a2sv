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
    ListNode* reverseKGroup(ListNode* head, int k) {
        ListNode* kthNode = getKthNode(head, k);
        if(!kthNode)
            return head;

        ListNode* kPlusOneTh = kthNode->next;
        kthNode->next = nullptr;

        ListNode* newHead = reverseList(head);
        head->next = reverseKGroup(kPlusOneTh, k);

        return newHead;

    }

    ListNode* getKthNode(ListNode* head, int k){
        while(head && --k)
            head = head->next;
        
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