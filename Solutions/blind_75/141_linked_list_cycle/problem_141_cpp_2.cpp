#include <../utils/listNode.h>
#include <cmath>

class Solution {
public:
    bool hasCycle(ListNode *head) {
        if(head == NULL || head->next == NULL) return false;

        while(head != NULL && head->val != 1000000) {
            head->val = 1000000;
            head = head->next;
        }
        return head != NULL;
    }
};