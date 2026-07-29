#include "../utils/listNode.h"
#include <iostream>
using namespace std;

class Solution {
public:
    ListNode* reverseList(ListNode* head) {
        if(head == NULL) return head;
        ListNode* previous = nullptr;
        while(head->next != NULL) {
            ListNode* temp = head->next;
            head->next = previous;
            previous = head;
            head = temp;
        }
        head->next = previous;
        return head;
    }
};