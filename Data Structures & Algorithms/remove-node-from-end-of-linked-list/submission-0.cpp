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
        ListNode* prevHead = new ListNode(0, head);
        ListNode* curr = prevHead;
        ListNode* fast = head;

        for(int i=0;i<n;i++){
            if(!fast) return head;
            fast = fast->next;
            //std::cout << fast->val <<"\n";
        }

        while(fast != nullptr){
            //std::cout << fast->val << ", "<< curr->val <<"\n";
            curr = curr->next;
            fast = fast->next;
        }

        curr->next = curr->next->next;

        return prevHead->next;
    }
};
