class Solution {
public:
    ListNode* swapPairs(ListNode* head) {
        ListNode dummy(0, head);
        ListNode* prev = &dummy;

        while (prev->next && prev->next->next) {
            ListNode* first  = prev->next;
            ListNode* second = first->next;

            first->next  = second->next;  // 1 -> 3
            second->next = first;         // 2 -> 1
            prev->next   = second;        // prev -> 2

            prev = first;                 // move to the end of the swapped pair
        }
        return dummy.next;
    }
};