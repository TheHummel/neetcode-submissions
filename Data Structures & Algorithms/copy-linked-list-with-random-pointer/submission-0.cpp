/*
// Definition for a Node.
class Node {
public:
    int val;
    Node* next;
    Node* random;
    
    Node(int _val) {
        val = _val;
        next = NULL;
        random = NULL;
    }
};
*/

class Solution {
public:
    Node* copyRandomList(Node* head) {
        if (!head) return nullptr;

        Node* curr = head->next;
        Node* newHead = new Node(head->val);
        Node* newCurr = newHead;

        //std::map<Node*, Node*> randomsMap = {}; // random field: newNode -> oldNode
        std::map<Node*, Node*> nodesMap = {{head, newHead}}; // oldNode -> newNode

        while(curr) {
            newCurr->next = new Node(curr->val);
            newCurr = newCurr->next;
            nodesMap.insert({curr, newCurr});

            curr = curr->next;
        }

        newCurr = newHead;
        curr = head;

        while(newCurr) {
            Node* oldRandom = curr->random;
            newCurr->random = nodesMap[oldRandom];
            
            newCurr = newCurr->next;
            curr = curr->next;
        }

        return newHead;
    }
};
